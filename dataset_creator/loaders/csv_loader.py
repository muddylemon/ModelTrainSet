import csv
from typing import List, Dict, Any
from ..base import DataLoader


class CSVLoader(DataLoader):
    def load_data(self, config: Dict[str, Any]) -> List[Dict]:
        data = []
        with open(config['input_file'], 'r', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                data.append(row)
        return data
