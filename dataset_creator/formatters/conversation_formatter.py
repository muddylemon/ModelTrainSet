from typing import List, Dict, Any
from ..base import DataFormatter



class ConversationFormatter(DataFormatter):
    def format_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        formatted_data = []
        for item in data:
            formatted_item = {
                "conversations": [
                    {"role": "user", "content": item[config['input_field']]},
                    {"role": "assistant", "content": item[config['output_field']]}
                ]
            }
            formatted_data.append(formatted_item)
        return formatted_data