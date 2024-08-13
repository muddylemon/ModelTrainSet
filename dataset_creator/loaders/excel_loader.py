from typing import List, Dict, Any
from ..base import DataLoader

class ExcelLoader(DataLoader):
    def load_data(self, config: Dict[str, Any]) -> List[Dict]:
        import pandas as pd
        df = pd.read_excel(config['input_file'])
        return df.to_dict('records')
