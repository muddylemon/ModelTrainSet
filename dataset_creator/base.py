from abc import ABC, abstractmethod
from typing import List, Dict, Any, Callable
from tqdm import tqdm


class DataLoader(ABC):
    @abstractmethod
    def load_data(self, config: Dict[str, Any], progress_callback: Callable[[int], None] = None) -> List[Dict]:
        pass


class DataProcessor(ABC):
    @abstractmethod
    def process_data(self, data: List[Dict], config: Dict[str, Any], progress_callback: Callable[[int], None] = None) -> List[Dict]:
        pass


class DataFormatter(ABC):
    @abstractmethod
    def format_data(self, data: List[Dict], config: Dict[str, Any], progress_callback: Callable[[int], None] = None) -> List[Dict]:
        pass


class BaseDatasetCreator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.loader = self.get_loader()
        self.processor = self.get_processor()
        self.formatter = self.get_formatter()

    @abstractmethod
    def get_loader(self) -> DataLoader:
        pass

    @abstractmethod
    def get_processor(self) -> DataProcessor:
        pass

    @abstractmethod
    def get_formatter(self) -> DataFormatter:
        pass

    def create_dataset(self, progress_callback: Callable[[int], None] = None) -> List[Dict]:
        show_progress = self.config.get('show_progress', True)

        data = self.loader.load_data(
            self.config, progress_callback if not show_progress else None)

        if show_progress:
            data = tqdm(data, desc="Processing", total=len(data))
        processed_data = self.processor.process_data(
            data, self.config, progress_callback if not show_progress else None)

        if show_progress:
            processed_data = tqdm(
                processed_data, desc="Formatting", total=len(processed_data))
        return self.formatter.format_data(processed_data, self.config, progress_callback if not show_progress else None)

    def save_dataset(self, dataset: List[Dict], output_file: str):
        import os
        import json
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)
