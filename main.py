import argparse
import logging
from dataset_creator import get_creator
from model_trainer.trainer import ModelTrainer
from model_trainer.utils import load_config, load_custom_dataset
from model_trainer.config import Config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Create datasets or train models for LLMs.")
    parser.add_argument(
        '--mode', choices=['dataset', 'train'], required=True, help="Are you creating a dataset or training a model?")
    parser.add_argument('--config', type=str, required=True,
                        help="Path to the YAML configuration file.")
    args = parser.parse_args()

    logger.info(f"Loading config from {args.config}")
    config_dict = load_config(args.config)

    if args.mode == 'dataset':
        creator = get_creator(config_dict)
        logger.info("Creating dataset...")
        dataset = creator.create_dataset()
        creator.save_dataset(dataset, config_dict['output_file'])
        logger.info(f"Dataset saved to {config_dict['output_file']}")
    elif args.mode == 'train':
        config = Config(config_dict)
        trainer = ModelTrainer(config)
        logger.info(f"Loading dataset from {config.dataset_file}")
        dataset = load_custom_dataset(config.dataset_file)
        logger.info("Starting model training...")
        trained_model, model, tokenizer = trainer.train(dataset)
        trainer.save_model(trained_model, model, tokenizer)
        if config.push_to_hub:
            logger.info("Pushing model to Hugging Face Hub...")
            trainer.push_to_hub(model, tokenizer)
        logger.info("Training complete!")


if __name__ == "__main__":
    main()
