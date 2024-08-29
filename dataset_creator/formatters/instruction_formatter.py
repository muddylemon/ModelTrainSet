from typing import List, Dict, Any
from ..base import DataFormatter
import json


class InstructionFormatter(DataFormatter):
    def format_data(self, data: List[Dict], config: Dict[str, Any]) -> List[str]:
        formatted_data = []
        system_message = config.get('system_message', "You are helpful")

        for item in data:
            conversation = {
                "messages": [
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": item['prompt']},
                    {"role": "assistant", "content": item['completion']}
                ]
            }
            formatted_data.append(json.dumps(conversation))

        return formatted_data
