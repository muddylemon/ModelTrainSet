from typing import List, Dict, Any
from ..base import DataProcessor



class SentimentAnalysisProcessor(DataProcessor):
    def process_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        from textblob import TextBlob
        for item in data:
            text = item.get(config['text_field'], '')
            sentiment = TextBlob(text).sentiment.polarity
            item['sentiment'] = sentiment
        return data