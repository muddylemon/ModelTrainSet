# ModelTrainSet

ModelTrainSet is a Python project designed to create custom datasets for training machine learning models. It currently supports creating datasets from Twitter data and Git/Jira integration data.

## Features

- Create datasets from Twitter archives
- Create datasets from Git repositories integrated with Jira
- Extensible architecture for adding new data sources
- Configuration-based setup for easy customization

## Prerequisites

- Python 3.7 or later
- Git
- Access to a Jira instance (for Git/Jira integration)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/muddylemon/ModelTrainSet.git
   cd ModelTrainSet
   ```

2. (Optional but recommended) Create a virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Create a configuration file (e.g., `config.yaml`) for your dataset. Here are some examples:

   For Twitter dataset:

   ```yaml
   creator_type: TweetDatasetCreator
   formatter: TweetSubjectFormatter
   input_file: path/to/tweet_archive.json
   output_file: ./data/tweets/username-subject-dataset.json
   twitter_username: username
   min_tweet_length: 25
   ```

   For Git/Jira dataset:

   ```yaml
   creator_type: GitJiraDatasetCreator
   repo_path: path/to/local/repo
   jira_server: https://your-jira-instance.atlassian.net
   jira_email: your-email@example.com
   jira_api_token: your-jira-api-token
   jira_prefix: PROJECTKEY
   output_file: ./data/gitjira/repo-name-dataset.json
   ```

2. Run the script:

   ```
   python main.py
   ```

3. When prompted, enter the path to your configuration file.

4. The script will create the dataset and save it to the specified output file.

## Extending ModelTrainSet

To add support for new data sources:

1. Create new loader, processor, and formatter classes in the respective directories under `dataset_creator/`.
2. Create a new creator class in `dataset_creator/creators/`.
3. Update the `get_creator()` function in `main.py` to recognize the new creator type.

## Troubleshooting

If you encounter a "No module named..." error, make sure you've installed all required dependencies by running:

```
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
