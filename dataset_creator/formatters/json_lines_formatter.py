from typing import List, Dict, Any
from ..base import DataFormatter



class JSONLinesFormatter(DataFormatter):
    def format_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        import json
        formatted_data = []
        for item in data:
            formatted_data.append(json.dumps(item))
        return formatted_data
