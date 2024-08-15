from typing import List, Dict, Any
from ..base import DataFormatter
import re
from tools.subjectify import subjectify


class TweetSubjectFormatter(DataFormatter):
    def format_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        dataset = []
        for tweet in data:
            subject = self.extract_subject(tweet['full_text'])
            dataset.append({
                "conversations": [
                    {
                        "role": "user",
                        "content": f"Write a tweet in the style of @{config['twitter_username']} on this subject: {subject}"
                    },
                    {
                        "role": "assistant",
                        "content": tweet['full_text']
                    }
                ]
            })
        return dataset

    def extract_subject(self, tweet_text: str) -> str:
        tweet_text = re.sub(r'http\S+', '', tweet_text)
        tweet_text = re.sub(r'@\w+', '', tweet_text)
        subject = subjectify(tweet_text)
        return subject


class TweetCompletionFormatter(DataFormatter):
    def format_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        dataset = []
        for tweet in data:
            first_half, second_half = self.split_tweet(tweet['full_text'])
            dataset.append({
                "conversations": [
                    {
                        "role": "user",
                        "content": f"Complete this tweet in the style of @{config['twitter_username']}: {first_half}"
                    },
                    {
                        "role": "assistant",
                        "content": second_half
                    }
                ]
            })
        return dataset

    def split_tweet(self, tweet_text: str) -> tuple:
        tweet_text = re.sub(r'http\S+', '', tweet_text)
        tweet_text = re.sub(r'@\w+', '', tweet_text)
        words = tweet_text.split()
        mid = len(words) // 2
        return ' '.join(words[:mid]), ' '.join(words[mid:])
