from ..base import BaseDatasetCreator, DataLoader, DataProcessor, DataFormatter
from ..loaders import JSONLoader, CSVLoader, ExcelLoader, XMLLoader, SQLLoader
from ..processors import TextCleanerProcessor, SentimentAnalysisProcessor
from ..formatters import JSONLinesFormatter, ConversationFormatter

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
            'jsonlines': JSONLinesFormatter,
            'conversation': ConversationFormatter
        }
        formatter_class = formatters.get(formatter_type)
        if formatter_class:
            return formatter_class()
        else:
            return DataFormatter()  # Default formatter