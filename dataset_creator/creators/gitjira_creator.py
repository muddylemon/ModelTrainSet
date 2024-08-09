from ..base import BaseDatasetCreator, DataLoader, DataProcessor, DataFormatter
from ..loaders.gitjira_loader import GitJiraLoader
from ..formatters.gitjira_formatter import GitJiraFormatter


class GitJiraDatasetCreator(BaseDatasetCreator):
    def get_loader(self) -> DataLoader:
        return GitJiraLoader()

    def get_processor(self) -> DataProcessor:
        return DataProcessor()  # Use base class if no processing is needed

    def get_formatter(self) -> DataFormatter:
        return GitJiraFormatter()
