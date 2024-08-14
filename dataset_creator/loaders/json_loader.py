import json
from typing import List, Dict, Any, Callable
from ..base import DataLoader


class JSONLoader(DataLoader):
    def load_data(self, config: Dict[str, Any], progress_callback: Callable[[int], None] = None) -> List[Dict]:
        with open(config['input_file'], 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not isinstance(data, list):
            data = [data]

        if progress_callback:
            for i, item in enumerate(data):
                progress_callback(int((i + 1) / len(data) * 100))

        return data
