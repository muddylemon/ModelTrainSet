from dataset_creator.base import DataProcessor
from tools.rewrite import rewrite
from typing import List, Dict, Any


class ParagraphRewriteProcessor(DataProcessor):
    def process_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        processed_data = []
        for item in data:
            paragraphs = item['text'].split('\n\n')
            for para in paragraphs:
                if len(para.strip()) > 0:
                    rewritten = rewrite(para)
                    processed_data.append({
                        'instruction': f"Rewrite the following paragraph in your own style:\n\n{rewritten}",
                        'output': para
                    })
        return processed_data
