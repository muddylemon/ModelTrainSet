from typing import List, Dict, Any
from ..base import DataFormatter


class TextTripletsFormatter(DataFormatter):
    def format_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        entires = [
            {
                "conversations": [
                    {
                        "role": "user",
                        "content": f"Given the following two sentences, predict the next sentence that would logically follow:\n\n{item['instruction']}"
                    },
                    {
                        "role": "assistant",
                        "content": item['completion']
                    }
                ],
                "source": item['source']
            }
            for item in data
        ]
        # shuffle the entries
        import random
        random.shuffle(entires)
        return entires
