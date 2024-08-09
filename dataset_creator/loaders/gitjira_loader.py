from typing import Dict, Any, List
from git import Repo
from jira import JIRA
import re
from ..base import DataLoader


class GitJiraLoader(DataLoader):
    def load_data(self, config: Dict[str, Any]) -> List[Dict]:
        repo = Repo(config['repo_path'])
        jira = JIRA(server=config['jira_server'], basic_auth=(
            config['jira_email'], config['jira_api_token']), options={'verify': False})
        data = []
        for branch in repo.branches:
            jira_info = self.get_jira_info(
                branch.name, jira, config['jira_prefix'])
            commits = list(repo.iter_commits(branch))
            for i in range(len(commits) - 1):
                current_commit = commits[i]
                previous_commit = commits[i + 1]
                diffs = previous_commit.diff(current_commit)
                for diff in diffs:
                    if diff.a_blob and diff.b_blob:
                        before = diff.a_blob.data_stream.read().decode('utf-8', errors='ignore')
                        diff_text = repo.git.diff(
                            previous_commit, current_commit, '--', diff.a_path)
                        data.append({
                            'jira_info': jira_info,
                            'commit_message': current_commit.message.strip(),
                            'before': before,
                            'diff': diff_text,
                        })
        return data

    def get_jira_info(self, branch_name: str, jira: JIRA, jira_prefix: str) -> Dict:
        ticket_match = re.match(f"{jira_prefix}-(\d+)", branch_name)
        if not ticket_match:
            return {}
        ticket_number = ticket_match.group(0)
        try:
            issue = jira.issue(ticket_number)
            return {
                "id": issue.key,
                "title": issue.fields.summary,
                "description": issue.fields.description,
                "type": str(issue.fields.issuetype),
                "priority": str(issue.fields.priority),
                "status": str(issue.fields.status),
                "comments": [comment.body for comment in issue.fields.comment.comments]
            }
        except Exception as e:
            logging.error(
                f"Error fetching Jira info for {ticket_number}: {str(e)}")
            return {}
