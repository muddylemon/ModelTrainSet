from typing import List, Dict, Any
from ..base import DataProcessor


class TextCleanerProcessor(DataProcessor):
    def process_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        import re

        def clean_text(text):
            text = re.sub(r'[^\w\s]', '', text)
            return text.lower()

        for item in data:
            for key, value in item.items():
                if isinstance(value, str):
                    item[key] = clean_text(value)
        return data
