from typing import List, Dict, Any
from ..base import DataLoader
import os
import re
import html
import unicodedata


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
        # Normalize Unicode characters
        text = unicodedata.normalize('NFKC', text)

        # Unescape HTML entities
        text = html.unescape(text)

        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)

        # Remove Markdown formatting
        text = re.sub(r'(\*|_|`|#|\[|\]|\(|\)|\{|\}|~|=|\^)', '', text)

        # Remove titles and headings (assuming they're on separate lines and in all caps or title case)
        text = re.sub(r'^[A-Z\s]+$', '', text, flags=re.MULTILINE)
        text = re.sub(r'^[A-Z][a-z]+([\s-][A-Z][a-z]+)*$',
                      '', text, flags=re.MULTILINE)

        # Remove special characters and weird punctuation, but keep some useful ones
        text = re.sub(r'[^\w\s.,!?;:()\'"-]', '', text)

        # Normalize ellipsis
        text = re.sub(r'\.{3,}', '...', text)

        # Normalize quotes
        text = re.sub(r'[""]', '"', text)
        text = re.sub(r'['']', "'", text)

        # Remove extra whitespace and empty lines
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\n\s*\n', '\n\n', text)

        # Ensure sentences end with proper punctuation
        text = re.sub(r'([.!?])\s+([A-Z])', r'\1\n\2', text)

        # Remove lone punctuation marks
        text = re.sub(r'\s([.,!?;:](?:\s|$))', r'\1', text)

        # Fix common OCR errors
        # "0" to "o" at the beginning of words
        text = re.sub(r'\b0([a-z])', r'o\1', text)

        # Remove repeated punctuation
        text = re.sub(r'([.,!?;:]){2,}', r'\1', text)

        # Normalize spacing around punctuation
        text = re.sub(r'\s+([.,!?;:])', r'\1', text)
        text = re.sub(r'([.,!?;:])\s+', r'\1 ', text)

        return text.strip()
