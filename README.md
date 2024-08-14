# 🚂 ModelTrainSet: All Aboard the ML Express! 🚂

Welcome to ModelTrainSet, your one-stop-shop for creating custom datasets and training machine learning models! Whether you're a data scientist, a machine learning engineer, or just someone who likes to play with big data and bigger models, ModelTrainSet has got your back!

## 🎭 What's This All About?

ModelTrainSet is like a Swiss Army knife for your data needs. It can:

- 📥 Load data from various sources (JSON, CSV, Excel, XML, SQL, Git/Jira, Twitter)
- 🧹 Clean and process your data
- 🎨 Format your data for different ML tasks
- 🚀 Train models using the latest techniques

It's perfect for when you need to wrangle your data into shape and then teach a model to do tricks with it!

## 🎟️ Getting Your Ticket to Ride

Before you hop on the ModelTrainSet express, make sure you have:

- Python 3.7+ installed (we're not cavemen, after all)
- Git (for version control and looking cool)
- Access to a Jira instance (if you're into that sort of thing)
- Linux for training. (Blame triton)

## 🧳 Packing Your Bags (Installation)

We've upgraded our luggage handling system! Now you can choose between the classic pip setup or our new first-class Conda/Mamba experience.

### 🌟 First Class: Conda/Mamba Setup (Recommended)

1. If you haven't already, install Miniconda or Anaconda. For an even faster setup, install Mamba.

2. Clone our luxury liner:

   ```bash
   git clone https://github.com/muddylemon/ModelTrainSet.git
   cd ModelTrainSet
   ```

3. Create and activate your environment:

   Using Conda:

   ```bash
   conda env create -f environment.yml
   conda activate modeltrainset
   ```

   Or, for a faster setup with Mamba:

   ```bash
   mamba env create -f environment.yml
   mamba activate modeltrainset
   ```

4. You're all set! Enjoy your first-class ML journey!

#### 🛠️ Manual Setup (if you encounter issues)

If you experience any problems with the automatic setup, you can try the following manual steps:

```bash
conda create --name modeltrainset python=3.10
conda activate modeltrainset

conda install pytorch cudatoolkit torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

conda install xformers -c xformers

pip install bitsandbytes

pip install "unsloth[conda] @ git+https://github.com/unslothai/unsloth.git"

pip install transformers datasets accelerate tqdm pyyaml nltk pandas openpyxl sqlalchemy gitpython jira python-dotenv peft trl
```

Replace `conda` with `mamba` in the above commands if you're using Mamba for faster installation.

### 🚶‍♂️ Economy Class: Pip Setup

If you prefer the classic experience, follow these steps:

1. Clone this bad boy:

   ```bash
   git clone https://github.com/muddylemon/ModelTrainSet.git
   cd ModelTrainSet
   ```

2. Set up your virtual environment (because we're responsible adults):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the necessities:

   ```bash
   pip install -r requirements.txt
   ```

## 🚂 All Aboard! (Usage)

1. Create a YAML config file (like `config.yaml`) for your journey. Here are some example destinations:

   For a Twitter dataset:

   ```yaml
   creator_type: TweetDatasetCreator
   formatter: TweetSubjectFormatter
   input_file: path/to/tweet_archive.json
   output_file: ./data/tweets/username-subject-dataset.json
   twitter_username: username
   min_tweet_length: 25
   ```

   For a Git/Jira adventure:

   ```yaml
   creator_type: GitJiraDatasetCreator
   repo_path: path/to/local/repo
   jira_server: https://your-jira-instance.atlassian.net
   jira_email: your-email@example.com
   jira_api_token: your-jira-api-token
   jira_prefix: PROJECTKEY
   output_file: ./data/gitjira/repo-name-dataset.json
   ```

   For training a model:

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
   per_device_train_batch_size: 32
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
   dataset_file: ./datasets/your_dataset.json
   ```

2. Start your engines:

   For dataset creation:

   ```bash
   python main.py --mode dataset --config your_dataset_config.yaml
   ```

   For model training:

   ```bash
   python main.py --mode train --config your_training_config.yaml
   ```

   For hyperparameter tuning:

   ```bash
   python main.py --mode tune --config your_config.yaml
   ```

3. Watch the magic happen! Your dataset will be created or your model will be trained faster than you can say "overfitting"!

4. Need more feedback? Add these flags:
   - `--verbose`: Get chatty with detailed logs
   - `--no-progress`: Silence those progress bars (but why would you want to?)

   Example:

   ```bash
   python main.py --mode train --config your_training_config.yaml --verbose
   ```

5. After training, find your model in the `output_dir` specified in your config. It's like a graduation ceremony for your AI!

6. If you set `push_to_hub: true` in your config, your model will automatically be uploaded to the Hugging Face Hub. Fame and glory await!

Remember, whether you're creating datasets or training models, ModelTrainSet has got your back. Now go forth and let your data science dreams run wild! 🚂💨

2. Start your engines:

   ```bash
   python main.py --mode dataset --config your_config.yaml
   ```

3. Watch the magic happen! Your dataset will be created faster than you can say "overfitting"!

## 🚀 Advanced Features

### Hyperparameter Tuning

ModelTrainSet now supports automatic hyperparameter tuning using Optuna! To tune your model's hyperparameters:

```bash
python main.py --mode tune --config your_hyperparameter_config.yaml
```

This will run a series of trials to find the best hyperparameters for your model. The results will be saved in `best_params.json`.

### Exporting to Ollama

After training your model, you can now export it directly to Ollama! Just set `export_to_ollama: true` in your config file, and we'll handle the rest.

## 🛤️ Extending Your Journey

Want to add a new stop on the ModelTrainSet line? Here's how:

1. Create new loader, processor, or formatter classes in `dataset_creator/`.
2. Add a new creator class in `dataset_creator/creators/`.
3. Update `get_creator()` in `main.py` to recognize your new creation.

## 🆘 Help! I'm Lost

If you find yourself in a dark tunnel:

1. Check your Python version (`python --version`).
2. Make sure you've installed all the requirements (`pip install -r requirements.txt`).
3. Double-check your config file. Typos are the bane of every data scientist's existence!

## 🤝 Join the Crew

Contributions are welcome! Whether you're fixing bugs, adding features, or just making our jokes funnier, we'd love to have you on board!

## 📜 The Fine Print

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. (It's basically "use it however you want, just don't blame us if something goes wrong".)

Remember, in the world of ModelTrainSet, every day is training day! Now go forth and model responsibly! 🚂💨
