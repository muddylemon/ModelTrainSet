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

For detailed instructions on how to use ModelTrainSet, check out our [comprehensive tutorial](docs/modeltrainset-tutorial.md). It covers everything from creating datasets to training your own models!
We also provide a tutorial for [Fill In Missing Word style datasets](tutorials/fill-in-missing-words-tutorial.md) and [TextTriplets style datasets](tutorials/text-triplets-tutorial.md).

## 🛤️ Extending Your Journey

Want to add a new stop on the ModelTrainSet line? Here's how:

1. Create new loader, processor, or formatter classes in `dataset_creator/`.
2. Add a new creator class in `dataset_creator/creators/`.
3. Update `get_creator()` in `main.py` to recognize your new creation.

For more details on contributing to ModelTrainSet, please read our [contribution guide](CONTRIBUTING.md).

## 🆘 Help! I'm Lost

If you find yourself in a dark tunnel:

1. Check your Python version (`python --version`).
2. Make sure you've installed all the requirements (`pip install -r requirements.txt`).
3. Double-check your config file. Typos are the bane of every data scientist's existence!

## 🤝 Join the Crew

Contributions are welcome! Whether you're fixing bugs, adding features, or just making our jokes funnier, we'd love to have you on board! Check out our [contribution guide](CONTRIBUTING.md) to get started.

## 📜 The Fine Print on Your Ticket Stub

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. (It's basically "use it however you want, just don't blame us if something goes wrong".)

Remember, in the world of ModelTrainSet, every day is training day! Now go forth and model responsibly! 🚂💨
