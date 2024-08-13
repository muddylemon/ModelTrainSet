from typing import List, Dict, Any
from ..base import DataLoader



class XMLLoader(DataLoader):
    def load_data(self, config: Dict[str, Any]) -> List[Dict]:
        import xml.etree.ElementTree as ET
        tree = ET.parse(config['input_file'])
        root = tree.getroot()
        return [elem.attrib for elem in root]
