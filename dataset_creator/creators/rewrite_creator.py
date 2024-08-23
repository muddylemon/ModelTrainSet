from dataset_creator.base import BaseDatasetCreator, DataLoader, DataProcessor, DataFormatter
from dataset_creator.loaders.text_loader import TextLoader
from dataset_creator.processors.rewrite_processor import ParagraphRewriteProcessor
from dataset_creator.formatters.conversation_formatter import ConversationFormatter


class ParagraphRewriteCreator(BaseDatasetCreator):
    def get_loader(self) -> DataLoader:
        return TextLoader()

    def get_processor(self) -> DataProcessor:
        return ParagraphRewriteProcessor()

    def get_formatter(self) -> DataFormatter:
        return ConversationFormatter()
