from typing import List, Dict, Any
from ..base import DataLoader
import json
import re


class TweetLoader(DataLoader):
    def load_data(self, config: Dict[str, Any]) -> List[Dict]:
        with open(config['input_file'], 'r', encoding='utf-8') as f:
            content = f.read()
            json_str = re.sub(r'^window\.YTD\.tweets\.part0 = ', '', content)
            return json.loads(json_str)
