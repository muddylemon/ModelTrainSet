from ..base import BaseDatasetCreator, DataLoader, DataProcessor, DataFormatter
from ..loaders import JSONLoader, CSVLoader


class GenericDatasetCreator(BaseDatasetCreator):
    def get_loader(self) -> DataLoader:
        loader_type = self.config.get('loader_type', '').lower()
        if loader_type == 'json':
            return JSONLoader()
        elif loader_type == 'csv':
            return CSVLoader()
        else:
            raise ValueError(f"Unknown loader type: {loader_type}")

    def get_processor(self) -> DataProcessor:
        # You can implement custom processors or use a default one
        return DataProcessor()

    def get_formatter(self) -> DataFormatter:
        # You can implement custom formatters or use a default one
        return DataFormatter()
