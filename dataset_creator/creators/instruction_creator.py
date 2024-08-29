from ..base import BaseDatasetCreator, DataLoader, DataProcessor, DataFormatter
from ..loaders.json_loader import JSONLoader
from ..formatters.instruction_formatter import InstructionFormatter


class InstructionCreator(BaseDatasetCreator):
    def get_loader(self) -> DataLoader:
        return JSONLoader()

    def get_processor(self) -> DataProcessor:
        # We're keeping it simple, no processing needed
        return DataProcessor()

    def get_formatter(self) -> DataFormatter:
        return InstructionFormatter()

    def create_dataset(self):
        data = self.loader.load_data(self.config)
        # We're skipping processing for now, but you could add it here if needed
        formatted_data = self.formatter.format_data(data, self.config)
        return formatted_data

    def save_dataset(self, dataset, output_file):
        with open(output_file, 'w') as f:
            for item in dataset:
                f.write(item + '\n')
