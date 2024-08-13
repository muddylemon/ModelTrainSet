import logging
from dataset_creator.creators.tweet_creator import TweetDatasetCreator
from dataset_creator.creators.gitjira_creator import GitJiraDatasetCreator
from dataset_creator.creators.text_triplets_creator import TextTripletsDatasetCreator
from dataset_creator.creators.generic_creator import GenericDatasetCreator

import sys


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


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
    else:
        raise ValueError(f"Unknown creator type: {creator_type}")


def main():
    check_dependencies()

    config_file = input("Enter the path to your configuration file: ")
    config = load_config(config_file)

    creator = get_creator(config)

    logging.info("Creating dataset...")
    dataset = creator.create_dataset()

    logging.info(f"Saving dataset to {config['output_file']}...")
    creator.save_dataset(dataset, config['output_file'])

    logging.info(
        f"Process complete. Created dataset with {len(dataset)} entries.")


if __name__ == "__main__":
    main()
