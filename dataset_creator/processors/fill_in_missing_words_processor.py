from typing import List, Dict, Any
import random
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from ..base import DataProcessor

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)


class FillInMissingWordsProcessor(DataProcessor):
    def __init__(self, min_sentence_length: int = 10, words_to_remove: int = 1):
        self.min_sentence_length = min_sentence_length
        self.words_to_remove = words_to_remove
        self.stop_words = set(stopwords.words('english'))

    def process_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        processed_data = []
        for item in data:
            sentences = sent_tokenize(item['text'])
            for sentence in sentences:
                words = word_tokenize(sentence)
                if len(words) >= self.min_sentence_length:
                    content_words = [
                        word for word in words if word.lower() not in self.stop_words]
                    if len(content_words) >= self.words_to_remove:
                        words_to_remove = random.sample(
                            content_words, self.words_to_remove)
                        masked_sentence = ' '.join(
                            ['___' if word in words_to_remove else word for word in words])
                        processed_data.append({
                            'input': masked_sentence,
                            'output': sentence
                        })
        return processed_data
