import subprocess
import logging

from datasets import load_dataset
from unsloth import FastLanguageModel, is_bfloat16_supported
from transformers import TrainingArguments
from trl import SFTTrainer


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


logger = logging.getLogger(__name__)


class ModelTrainer:
    def __init__(self, config):
        self.config = config

    def load_model(self):
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=self.config['model_name'],
            max_seq_length=self.config['max_seq_length'],
            load_in_4bit=self.config['load_in_4bit'],
        )

        model = FastLanguageModel.get_peft_model(
            model,
            r=self.config['r'],
            target_modules=self.config['target_modules'],
            lora_alpha=self.config['lora_alpha'],
            lora_dropout=self.config['lora_dropout'],
            bias=self.config['bias'],
            use_gradient_checkpointing=self.config['use_gradient_checkpointing'],
            random_state=self.config['random_state'],
        )

        return model, tokenizer

    def train(self, train_dataset):
        model, tokenizer = self.load_model()

        training_args = TrainingArguments(
            output_dir=self.config['output_dir'],
            learning_rate=float(self.config['learning_rate']),
            fp16=not is_bfloat16_supported(),
            bf16=is_bfloat16_supported(),
            per_device_train_batch_size=self.config['per_device_train_batch_size'],
            gradient_accumulation_steps=self.config['gradient_accumulation_steps'],
            num_train_epochs=self.config['num_train_epochs'],
            warmup_ratio=self.config['warmup_ratio'],
            logging_dir=f"{self.config['output_dir']}/logs",
            logging_steps=self.config['logging_steps'],
        )

        trainer = SFTTrainer(
            model=model,
            tokenizer=tokenizer,
            train_dataset=train_dataset,
            max_seq_length=self.config['max_seq_length'],
            dataset_num_proc=self.config['dataset_num_proc'],
            packing=self.config['packing'],
            args=training_args,
        )

        trainer.train()
        return trainer, model, tokenizer

    def save_model(self, model, tokenizer):
        model.save_pretrained(self.config['output_dir'])
        tokenizer.save_pretrained(self.config['output_dir'])

    def export_to_ollama(self, model_name):
        subprocess.run(["ollama", "create", model_name,
                       f"FROM {self.config['output_dir']}"])
        logger.info(f"Model exported to Ollama as {model_name}")
