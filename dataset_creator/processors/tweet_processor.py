from typing import List, Dict, Any
from ..base import DataProcessor


class TweetProcessor(DataProcessor):
    def process_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        filtered_tweets = self.filter_tweets(data, config['min_tweet_length'])
        return self.sort_tweets(filtered_tweets)

    def filter_tweets(self, tweets: List[Dict], min_length: int) -> List[Dict]:
        return [
            tweet['tweet'] for tweet in tweets
            if len(tweet['tweet']['full_text']) >= min_length
            and not tweet['tweet']['full_text'].startswith('@')
        ]

    def sort_tweets(self, tweets: List[Dict]) -> List[Dict]:
        return sorted(tweets, key=lambda x: int(x['favorite_count']) + int(x['retweet_count']), reverse=True)
