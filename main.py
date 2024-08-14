import argparse
import logging
from dataset_creator import get_creator
from model_trainer.trainer import ModelTrainer
from model_trainer.utils import load_config, load_custom_dataset

from model_trainer.hyperparameter_tuning import run_hyperparameter_tuning

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Create datasets or train models for LLMs.")
    parser.add_argument('--mode', choices=['dataset', 'train', 'tune'], required=True,
                        help="Are you creating a dataset, training a model, or tuning hyperparameters?")
    parser.add_argument('--config', type=str, required=True,
                        help="Path to the YAML configuration file.")
    parser.add_argument('--verbose', action='store_true',
                        help="Enable verbose output")
    parser.add_argument('--no-progress', action='store_true',
                        help="Disable progress bars")
    args = parser.parse_args()

    config = load_config(args.config)
    config['show_progress'] = not args.no_progress

    if args.mode == 'dataset':
        creator = get_creator(config)
        dataset = creator.create_dataset()
        creator.save_dataset(dataset, config['output_file'])
    elif args.mode == 'train':
        trainer = ModelTrainer(config)
        dataset = load_custom_dataset(config['dataset_file'])
        train_dataset, eval_dataset = dataset.train_test_split(
            test_size=0.1).values()
        trained_model, model, tokenizer = trainer.train(
            train_dataset, eval_dataset)
        trainer.save_model(model, tokenizer)
        if config.get('export_to_ollama'):
            trainer.export_to_ollama(config['model_name'])
    elif args.mode == 'tune':
        best_params = run_hyperparameter_tuning(args.config)
        logger.info(f"Best hyperparameters: {best_params}")


if __name__ == "__main__":
    main()
