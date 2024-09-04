import sys
import argparse
import logging

from dataset_creator.creators.tweet_creator import TweetDatasetCreator
from dataset_creator.creators.gitjira_creator import GitJiraDatasetCreator
from dataset_creator.creators.text_triplets_creator import TextTripletsDatasetCreator
from dataset_creator.creators.generic_creator import GenericDatasetCreator
from dataset_creator.creators.fill_in_missing_words_creator import FillInMissingWordsDatasetCreator
from dataset_creator.creators.rewrite_creator import ParagraphRewriteCreator
from dataset_creator.creators.instruction_creator import InstructionCreator


from model_trainer.trainer import ModelTrainer
from model_trainer.utils import load_config, load_custom_dataset

from model_trainer.hyperparameter_tuning import run_hyperparameter_tuning
from unsloth import standardize_sharegpt


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def check_dependencies():
    required_modules = ['yaml', 'git', 'jira']
    missing_modules = []

    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)

    if missing_modules:
        print("Error: The following required modules are missing:")
        for module in missing_modules:
            print(f"  - {module}")
        print("\nPlease install the missing modules using the following command:")
        print("pip install -r requirements.txt")
        sys.exit(1)


def load_config(config_file: str) -> dict:
    try:
        import yaml
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {config_file}")
        sys.exit(1)
    except yaml.YAMLError as e:
        logging.error(f"Error parsing YAML configuration: {e}")
        sys.exit(1)


def get_creator(config):
    creator_type = config['creator_type']
    if creator_type == 'TweetDatasetCreator':
        return TweetDatasetCreator(config)
    elif creator_type == 'GitJiraDatasetCreator':
        return GitJiraDatasetCreator(config)
    elif creator_type == 'GenericDatasetCreator':
        return GenericDatasetCreator(config)
    elif creator_type == 'TextTripletsDatasetCreator':
        return TextTripletsDatasetCreator(config)
    elif creator_type == 'FillInMissingWordsDatasetCreator':
        return FillInMissingWordsDatasetCreator(config)
    if creator_type == 'ParagraphRewriteCreator':
        return ParagraphRewriteCreator(config)
    if creator_type == 'InstructionCreator':
        return InstructionCreator(config)
    else:
        raise ValueError(f"Unknown creator type: {creator_type}")


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
       # dataset = standardize_sharegpt(dataset)
 
        trained_model, model, tokenizer = trainer.train(
            dataset)
        trainer.save_model(model, tokenizer)
        if config.get('export_to_ollama'):
            trainer.export_to_ollama(config['model_name'])
    elif args.mode == 'tune':
        best_params = run_hyperparameter_tuning(args.config)
        logger.info(f"Best hyperparameters: {best_params}")


if __name__ == "__main__":
    main()
