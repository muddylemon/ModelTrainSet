# ModelTrainSet Tutorial: From Data to Trained Model

Welcome to the ModelTrainSet tutorial! This guide will walk you through the process of using ModelTrainSet to create custom datasets and train machine learning models. We'll cover three main scenarios:

1. Creating a dataset from tweets
2. Creating a dataset from Git and Jira data
3. Training a model using your custom dataset

## Prerequisites

Before we begin, make sure you have:

- Python 3.7+ installed
- Git installed
- ModelTrainSet cloned and set up (follow the installation instructions in the README)

## Scenario 1: Creating a Dataset from Tweets

Let's start by creating a dataset from a Twitter archive.

### Step 1: Prepare Your Tweet Data

1. Download your Twitter archive from Twitter settings.
2. Locate the JSON file containing your tweets (usually named something like `tweet.js`).
3. Move this file to your project directory, for example: `./data/tweets/mytweets.js`

### Step 2: Configure the Dataset Creator

Create a configuration file named `tweet_config.yaml` in the `config` directory with the following content:

```yaml
creator_type: TweetDatasetCreator
formatter: TweetSubjectFormatter
input_file: ./data/tweets/mytweets.js
output_file: ./datasets/mytweets_dataset.json
twitter_username: yourusername
min_tweet_length: 25
```

### Step 3: Run the Dataset Creator

Execute the following command:

```bash
python main.py --mode dataset --config config/tweet_config.yaml
```

This will process your tweets and create a dataset in the specified output file.

## Scenario 2: Creating a Dataset from Git and Jira Data

Now, let's create a dataset using Git commit history and Jira ticket information.

### Step 1: Prepare Your Git and Jira Data

1. Ensure you have a local Git repository you want to use.
2. Have your Jira server URL and API token ready.

### Step 2: Configure the Dataset Creator

Create a configuration file named `gitjira_config.yaml` in the `config` directory:

```yaml
creator_type: GitJiraDatasetCreator
repo_path: /path/to/your/local/repo
jira_server: https://your-jira-instance.atlassian.net
jira_email: your-email@example.com
jira_api_token: your-jira-api-token
jira_prefix: PROJECTKEY
output_file: ./datasets/gitjira_dataset.json
```

Replace the placeholders with your actual information.

### Step 3: Run the Dataset Creator

Execute the following command:

```bash
python main.py --mode dataset --config config/gitjira_config.yaml
```

This will process your Git commits and Jira tickets to create a dataset.

## Scenario 3: Training a Model Using Your Custom Dataset

Now that we have created custom datasets, let's train a model using one of them.

### Step 1: Prepare Your Training Configuration

Create a configuration file named `train_config.yaml` in the `config` directory:

```yaml
model_name: mistralai/Mistral-7B-Instruct-v0.2
max_seq_length: 2048
load_in_4bit: true
r: 16
target_modules: 
  - q_proj
  - k_proj
  - v_proj
  - o_proj
  - gate_proj
  - up_proj
  - down_proj
lora_alpha: 16
lora_dropout: 0.05
bias: none
use_gradient_checkpointing: true
per_device_train_batch_size: 4
gradient_accumulation_steps: 4
warmup_steps: 100
num_train_epochs: 3
learning_rate: 2.0e-4
logging_steps: 25
weight_decay: 0.01
dataset_num_proc: 4
packing: true
output_dir: ./outputs/trained_model
push_to_hub: false
dataset_file: ./datasets/mytweets_dataset.json
```

Adjust the `dataset_file` to point to the dataset you want to use for training.

### Step 2: Run the Training Process

Execute the following command:

```bash
python main.py --mode train --config config/train_config.yaml
```

This will start the training process using your custom dataset and the specified model configuration.

### Step 3: Monitor Training Progress

The training process will output logs showing the progress, loss, and other metrics. You can monitor these to see how your model is performing.

### Step 4: Use the Trained Model

Once training is complete, you'll find your trained model in the `output_dir` specified in your configuration file. You can now use this model for inference or further fine-tuning.

## Conclusion

Congratulations! You've now learned how to use ModelTrainSet to create custom datasets from various sources and train a model using those datasets. Here are some next steps you can take:

1. Experiment with different data sources by creating new loaders and formatters.
2. Try different model architectures and hyperparameters to improve performance.
3. Use the trained model in your applications or push it to the Hugging Face Hub for sharing.

Remember to check the ModelTrainSet documentation for more advanced features and options. Happy modeling!
