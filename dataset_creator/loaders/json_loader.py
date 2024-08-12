import json
from typing import List, Dict, Any
from ..base import DataLoader


class JSONLoader(DataLoader):
    def load_data(self, config: Dict[str, Any]) -> List[Dict]:
        with open(config['input_file'], 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data if isinstance(data, list) else [data]
