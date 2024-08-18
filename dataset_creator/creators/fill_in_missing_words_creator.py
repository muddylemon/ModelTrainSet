from typing import List, Dict, Any
from ..base import BaseDatasetCreator, DataLoader, DataProcessor, DataFormatter
from ..loaders.text_loader import TextLoader
from ..formatters.conversation_formatter import ConversationFormatter
from ..processors.fill_in_missing_words_processor import FillInMissingWordsProcessor


class FillInMissingWordsDatasetCreator(BaseDatasetCreator):
    def get_loader(self) -> DataLoader:
        return TextLoader()

    def get_processor(self) -> DataProcessor:
        return FillInMissingWordsProcessor(
            min_sentence_length=self.config.get('min_sentence_length', 10),
            words_to_remove=self.config.get('words_to_remove', 1)
        )

    def get_formatter(self) -> DataFormatter:
        return ConversationFormatter()
