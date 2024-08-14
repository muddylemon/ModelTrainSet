from unsloth import FastLanguageModel, standardize_sharegpt, is_bfloat16_supported
from transformers import TrainingArguments
from trl import SFTTrainer


class ModelTrainer:
    def __init__(self, config):
        self.config = config

    def prepare_dataset(self, data):
        return standardize_sharegpt(data)

    def load_model(self):
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=self.config.model_name,
            max_seq_length=self.config.max_seq_length,
            load_in_4bit=self.config.load_in_4bit,
        )
        # ... (rest of model loading code)
        return model, tokenizer

    def train(self, dataset):
        model, tokenizer = self.load_model()
        training_args = TrainingArguments(
            # ... (training arguments from your existing code)
        )
        trainer = SFTTrainer(
            # ... (trainer setup from your existing code)
        )
        trainer.train()
        return trainer, model, tokenizer

    def save_model(self, trainer, model, tokenizer):
        # ... (model saving code)

    def push_to_hub(self, model, tokenizer):
        # ... (hub pushing code)
