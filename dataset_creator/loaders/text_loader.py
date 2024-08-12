from typing import List, Dict, Any
from ..base import DataLoader
import os
import re


class TextLoader(DataLoader):
    def load_data(self, config: Dict[str, Any]) -> List[Dict]:
        data = []
        input_dir = config['input_directory']
        for filename in os.listdir(input_dir):
            if filename.endswith('.txt'):
                with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Remove titles, headings, and extraneous content
                    cleaned_content = self.clean_text(content)
                    data.append(
                        {'text': cleaned_content, 'filename': filename})
        return data

    def clean_text(self, text: str) -> str:
        # Remove titles and headings (assuming they're on separate lines and in all caps or title case)
        text = re.sub(r'^[A-Z\s]+$', '', text, flags=re.MULTILINE)
        text = re.sub(r'^[A-Z][a-z]+([\s-][A-Z][a-z]+)*$',
                      '', text, flags=re.MULTILINE)

        # Remove extra whitespace and empty lines
        text = re.sub(r'\n+', '\n', text).strip()

        return text
