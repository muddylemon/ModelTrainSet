from ..base import BaseDatasetCreator, DataLoader, DataProcessor, DataFormatter
from ..loaders.text_loader import TextLoader
from ..processors.text_triplets_processor import TextTripletsProcessor
from ..formatters.text_triplets_formatter import TextTripletsFormatter


class TextTripletsDatasetCreator(BaseDatasetCreator):
    def get_loader(self) -> DataLoader:
        return TextLoader()

    def get_processor(self) -> DataProcessor:
        return TextTripletsProcessor()

    def get_formatter(self) -> DataFormatter:
        return TextTripletsFormatter()
