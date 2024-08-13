from ..base import BaseDatasetCreator, DataLoader, DataProcessor, DataFormatter
from ..loaders.csv_loader import CSVLoader
from ..loaders.excel_loader import ExcelLoader
from ..loaders.json_loader import JSONLoader
from ..loaders.sql_loader import SQLLoader
from ..loaders.xml_loader import XMLLoader
from ..processors.text_cleaner_processor import TextCleanerProcessor
from ..processors.sentiment_analysis_processor import SentimentAnalysisProcessor
from ..formatters.conversation_formatter import ConversationFormatter


class GenericDatasetCreator(BaseDatasetCreator):
    def get_loader(self) -> DataLoader:
        loader_type = self.config.get('loader_type', '').lower()
        loaders = {
            'json': JSONLoader,
            'csv': CSVLoader,
            'excel': ExcelLoader,
            'xml': XMLLoader,
            'sql': SQLLoader
        }
        loader_class = loaders.get(loader_type)
        if loader_class:
            return loader_class()
        else:
            raise ValueError(f"Unknown loader type: {loader_type}")

    def get_processor(self) -> DataProcessor:
        processor_type = self.config.get('processor_type', '').lower()
        processors = {
            'text_cleaner': TextCleanerProcessor,
            'sentiment_analysis': SentimentAnalysisProcessor
        }
        processor_class = processors.get(processor_type)
        if processor_class:
            return processor_class()
        else:
            return DataProcessor()  # Default processor

    def get_formatter(self) -> DataFormatter:
        formatter_type = self.config.get('formatter_type', '').lower()
        formatters = {
            'conversation': ConversationFormatter
        }
        formatter_class = formatters.get(formatter_type)
        if formatter_class:
            return formatter_class()
        else:
            return DataFormatter()  # Default formatter
