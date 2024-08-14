import optuna
import json
import logging
from datasets import load_dataset
from unsloth import FastLanguageModel, SFTTrainer
from trl import SFTTrainer
from transformers import TrainingArguments

from .trainer import ModelTrainer
from .utils import load_config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def load_and_prepare_data(config):
    with open(config['dataset_file'], 'r') as f:
        data = json.load(f)

    prepared_data = []
    for item in data:
        for conv in item['conversations']:
            prepared_data.append({
                'instruction': conv['content'] if conv['role'] == 'user' else '',
                'input': '',
                'output': conv['content'] if conv['role'] == 'assistant' else ''
            })

    dataset = load_dataset("json", data={"train": prepared_data})
    return dataset.train_test_split(test_size=0.1)  # 10% for validation


def objective(trial, base_config, dataset):
    config = base_config.copy()

    # Define the hyperparameters to optimize
    config.update({
        'learning_rate': trial.suggest_loguniform('learning_rate', 1e-5, 1e-3),
        'per_device_train_batch_size': trial.suggest_categorical('per_device_train_batch_size', [4, 8, 16]),
        'gradient_accumulation_steps': trial.suggest_int('gradient_accumulation_steps', 1, 4),
        'num_train_epochs': trial.suggest_int('num_train_epochs', 1, 5),
        'warmup_ratio': trial.suggest_uniform('warmup_ratio', 0.0, 0.2),
        'r': trial.suggest_int('r', 8, 32),
        'lora_alpha': trial.suggest_int('lora_alpha', 16, 64),
    })

    trainer = ModelTrainer(config)
    model, tokenizer = trainer.load_model()

    # Prepare the dataset
    train_dataset = FastLanguageModel.apply_chat_template(
        dataset['train'],
        tokenizer=tokenizer,
        chat_template=config['chat_template'],
    )
    eval_dataset = FastLanguageModel.apply_chat_template(
        dataset['test'],
        tokenizer=tokenizer,
        chat_template=config['chat_template'],
    )

    # Set up training arguments
    training_args = TrainingArguments(
        output_dir=f"./results/{trial.number}",
        learning_rate=config['learning_rate'],
        per_device_train_batch_size=config['per_device_train_batch_size'],
        gradient_accumulation_steps=config['gradient_accumulation_steps'],
        num_train_epochs=config['num_train_epochs'],
        warmup_ratio=config['warmup_ratio'],
        logging_dir=f"./logs/{trial.number}",
        logging_steps=10,
        evaluation_strategy="steps",
        eval_steps=100,
        save_strategy="steps",
        save_steps=100,
        load_best_model_at_end=True,
    )

    # Initialize the trainer
    sft_trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        dataset_text_field="text",
        max_seq_length=config['max_seq_length'],
        dataset_num_proc=config['dataset_num_proc'],
        packing=config['packing'],
        args=training_args,
    )

    # Train the model
    sft_trainer.train()

    # Evaluate the model
    eval_results = sft_trainer.evaluate()

    return eval_results['eval_loss']


def run_hyperparameter_tuning(config_path):
    base_config = load_config(config_path)
    dataset = load_and_prepare_data(base_config)

    study = optuna.create_study(direction='minimize')
    study.optimize(lambda trial: objective(trial, base_config, dataset),
                   n_trials=base_config['hyperparameter_tuning']['n_trials'])

    logger.info(f"Best trial:")
    logger.info(f"  Value: {study.best_trial.value}")
    logger.info(f"  Params: ")
    for key, value in study.best_trial.params.items():
        logger.info(f"    {key}: {value}")

    # Save the best parameters
    with open('best_params.json', 'w') as f:
        json.dump(study.best_trial.params, f, indent=2)

    return study.best_trial.params
