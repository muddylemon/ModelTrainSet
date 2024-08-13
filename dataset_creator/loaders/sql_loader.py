from typing import List, Dict, Any
from ..base import DataLoader


class SQLLoader(DataLoader):
    def load_data(self, config: Dict[str, Any]) -> List[Dict]:
        import sqlite3
        conn = sqlite3.connect(config['database'])
        cursor = conn.cursor()
        cursor.execute(config['query'])
        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
