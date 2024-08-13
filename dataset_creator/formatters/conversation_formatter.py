from typing import List, Dict, Any
from ..base import DataFormatter


class ConversationFormatter(DataFormatter):
    def format_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        formatters = {
            "sentence_completion": self._format_sentence_completion,
            "email_reply": self._format_email_reply,
            "dialogue_continuation": self._format_dialogue_continuation,
            "question_answering": self._format_question_answering,
            "text_summarization": self._format_text_summarization,
            "translation": self._format_translation,
            "sentiment_analysis": self._format_sentiment_analysis,
            "code_generation": self._format_code_generation,
            "paraphrasing": self._format_paraphrasing,
            "fill_in_the_blank": self._format_fill_in_the_blank
        }
        style = config.get("style", "sentence_completion")

        if style in formatters:
            return formatters[style](data)
        else:
            raise ValueError(f"""Unknown style: {style}""")

    def _format_sentence_completion(self, data: List[Dict]) -> List[Dict]:
        return [
            {
                "conversations": [
                    {"role": "user",
                        "content": f"""Complete the following sentence: { item['partial_sentence']}"""},
                    {"role": "assistant", "content": item['completion']}
                ]
            } for item in data
        ]

    def _format_email_reply(self, data: List[Dict]) -> List[Dict]:
        return [
            {
                "conversations": [
                    {"role": "user",
                     "content": f"""Compose a reply to the following email:\n\n{item['email_body']}"""},
                    {"role": "assistant", "content": item['reply']}
                ]
            } for item in data
        ]

    def _format_dialogue_continuation(self, data: List[Dict]) -> List[Dict]:
        return [
            {
                "conversations": [
                    {"role": "user",
                        "content": f"""Continue this dialogue: \n\nPerson A: { item['person_a']}\nPerson B: {item['person_b']}\nPerson A: """},
                    {"role": "assistant", "content": item['continuation']}
                ]
            } for item in data
        ]

    def _format_question_answering(self, data: List[Dict]) -> List[Dict]:
        return [
            {
                "conversations": [
                    {"role": "user",
                     "content": f"""Context: {   item['context']}\n\nQuestion: {item['question']}"""},
                    {"role": "assistant", "content": item['answer']}
                ]
            } for item in data
        ]

    def _format_text_summarization(self, data: List[Dict]) -> List[Dict]:
        return [
            {
                "conversations": [
                    {"role": "user", "content": f"""Summarize the following text: \n\n{
                        item['full_text']}"""},
                    {"role": "assistant", "content": item['summary']}
                ]
            } for item in data
        ]

    def _format_translation(self, data: List[Dict]) -> List[Dict]:
        return [
            {
                "conversations": [
                    {"role": "user", "content": f"""Translate the following {
                        item['source_language']} text to {item['target_language']}: \n\n{item['source_text']}"""},
                    {"role": "assistant", "content": item['translation']}
                ]
            } for item in data
        ]

    def _format_sentiment_analysis(self, data: List[Dict]) -> List[Dict]:
        return [
            {
                "conversations": [
                    {"role": "user", "content": f"""Analyze the sentiment of the following text: \n\n{
                        item['text']}"""},
                    {"role": "assistant", "content": f"""The sentiment of the text is {
                        item['sentiment']}. {item.get('explanation', '')}"""}
                ]
            } for item in data
        ]

    def _format_code_generation(self, data: List[Dict]) -> List[Dict]:
        return [
            {
                "conversations": [
                    {"role": "user",
                     "content": f"""Generate {item['language']} code for the following task: \n\n{item['task_description']}"""},
                    {"role": "assistant", "content": item['code']}
                ]
            } for item in data
        ]

    def _format_paraphrasing(self, data: List[Dict]) -> List[Dict]:
        return [
            {
                "conversations": [
                    {"role": "user", "content": f"""Paraphrase the following sentence: \n\n{
                        item['original_sentence']}"""},
                    {"role": "assistant", "content": item['paraphrase']}
                ]
            } for item in data
        ]

    def _format_fill_in_the_blank(self, data: List[Dict]) -> List[Dict]:
        return [
            {
                "conversations": [
                    {"role": "user", "content": f"""Fill in the blank in the following sentence: \n\n{
                        item['sentence_with_blank']}"""},
                    {"role": "assistant", "content": item['filled_word']}
                ]
            } for item in data
        ]
