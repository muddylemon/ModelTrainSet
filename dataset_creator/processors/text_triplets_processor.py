from typing import List, Dict, Any
from ..base import DataProcessor
import nltk
nltk.download('punkt')


class TextTripletsProcessor(DataProcessor):
    def process_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        processed_data = []
        for item in data:
            sentences = nltk.sent_tokenize(item['text'])
            for i in range(len(sentences) - 2):
                processed_data.append({
                    'instruction': f"{sentences[i]} {sentences[i+1]}",
                    'completion': sentences[i+2],
                    'source': item['filename']
                })
        return processed_data
