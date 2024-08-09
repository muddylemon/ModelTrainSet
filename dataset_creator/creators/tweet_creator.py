from ..base import BaseDatasetCreator, DataLoader, DataProcessor, DataFormatter
from ..loaders.tweet_loader import TweetLoader
from ..processors.tweet_processor import TweetProcessor
from ..formatters.tweet_formatter import TweetSubjectFormatter, TweetCompletionFormatter


class TweetDatasetCreator(BaseDatasetCreator):
    def get_loader(self) -> DataLoader:
        return TweetLoader()

    def get_processor(self) -> DataProcessor:
        return TweetProcessor()

    def get_formatter(self) -> DataFormatter:
        if self.config['formatter'] == 'TweetSubjectFormatter':
            return TweetSubjectFormatter()
        elif self.config['formatter'] == 'TweetCompletionFormatter':
            return TweetCompletionFormatter()
        else:
            raise ValueError(f"Unknown formatter: {self.config['formatter']}")
