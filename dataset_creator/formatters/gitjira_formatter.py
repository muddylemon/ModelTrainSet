from typing import List, Dict, Any
from ..base import DataFormatter


class GitJiraFormatter(DataFormatter):
    def format_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        dataset = []
        for item in data:
            instruction = f"Given the Jira ticket '{item['jira_info'].get('title', '')}' and the previous code, implement the necessary changes. The commit message is: {item['commit_message']}"
            dataset.append({
                "conversations": [
                    {
                        "role": "user",
                        "content": f"{instruction}\n\nInput:\n{item['before']}"
                    },
                    {
                        "role": "assistant",
                        "content": item['diff']
                    }
                ]
            })
        return dataset
