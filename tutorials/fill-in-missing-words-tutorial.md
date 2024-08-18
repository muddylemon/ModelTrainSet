# Tutorial: Creating a 'Fill in the Missing Words' Dataset

This tutorial will guide you through the process of creating a dataset for training language models using the "fill in the missing word(s)" strategy. We'll use the ModelTrainSet project to accomplish this task.

## Prerequisites

- Python 3.7 or higher
- Git
- Basic knowledge of command-line operations

## Step 1: Set Up the Environment

1. Clone the ModelTrainSet repository:

   ```bash
   git clone https://github.com/muddylemon/ModelTrainSet.git
   cd ModelTrainSet
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Step 2: Prepare the Input Data

1. Create a directory for your input text files:

   ```bash
   mkdir -p data/text_files
   ```

2. Add your text files to this directory. For example:

   ```bash
   echo "This is a sample sentence. It will be used to create our dataset." > data/text_files/sample.txt
   ```

## Step 3: Create the Configuration File

Create a new file named `fill_in_missing_words_config.yaml` in the `config` directory with the following content:

```yaml
creator_type: FillInMissingWordsCreator
input_directory: ./data/text_files
output_file: ./datasets/fill_in_missing_words_dataset.json
min_sentence_length: 10
words_to_remove: 1
formatter_type: conversation
style: fill_in_the_blank
```

## Step 4: Implement the FillInMissingWordsProcessor

Create a new file `dataset_creator/processors/fill_in_missing_words_processor.py`:

```python
from typing import List, Dict, Any
import random
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from ..base import DataProcessor

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

class FillInMissingWordsProcessor(DataProcessor):
    def __init__(self, min_sentence_length: int = 10, words_to_remove: int = 1):
        self.min_sentence_length = min_sentence_length
        self.words_to_remove = words_to_remove
        self.stop_words = set(stopwords.words('english'))

    def process_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        processed_data = []
        for item in data:
            sentences = sent_tokenize(item['text'])
            for sentence in sentences:
                words = word_tokenize(sentence)
                if len(words) >= self.min_sentence_length:
                    content_words = [word for word in words if word.lower() not in self.stop_words]
                    if len(content_words) >= self.words_to_remove:
                        words_to_remove = random.sample(content_words, self.words_to_remove)
                        masked_sentence = ' '.join(['___' if word in words_to_remove else word for word in words])
                        processed_data.append({
                            'input': masked_sentence,
                            'output': sentence
                        })
        return processed_data
```

## Step 5: Implement the FillInMissingWordsCreator

Create a new file `dataset_creator/creators/fill_in_missing_words_creator.py`:

```python
from ..base import BaseDatasetCreator, DataLoader, DataProcessor, DataFormatter
from ..loaders.text_loader import TextLoader
from ..processors.fill_in_missing_words_processor import FillInMissingWordsProcessor
from ..formatters.conversation_formatter import ConversationFormatter

class FillInMissingWordsCreator(BaseDatasetCreator):
    def get_loader(self) -> DataLoader:
        return TextLoader()

    def get_processor(self) -> DataProcessor:
        return FillInMissingWordsProcessor(
            min_sentence_length=self.config.get('min_sentence_length', 10),
            words_to_remove=self.config.get('words_to_remove', 1)
        )

    def get_formatter(self) -> DataFormatter:
        return ConversationFormatter()
```

## Step 6: Update the Main Script

Ensure that the `main.py` file includes the new creator. Add the following import:

```python
from dataset_creator.creators.fill_in_missing_words_creator import FillInMissingWordsCreator
```

And update the `get_creator` function to include the new creator:

```python
def get_creator(config):
    creator_type = config['creator_type']
    if creator_type == 'FillInMissingWordsCreator':
        return FillInMissingWordsCreator(config)
    # ... (other creator types)
```

## Step 7: Run the Dataset Creation Process

Execute the following command to create your dataset:

```bash
python main.py --mode dataset --config config/fill_in_missing_words_config.yaml
```

This will process your input text files and create a dataset in the specified output file.

## Step 8: Verify the Output

Check the contents of the output file (`datasets/fill_in_missing_words_dataset.json`) to ensure it contains the expected data. It should look something like this:

```json
[
  {
    "conversations": [
      {
        "role": "user",
        "content": "Fill in the blank in the following sentence:\n\nThis is a sample ___. It will be used to create our dataset."
      },
      {
        "role": "assistant",
        "content": "sentence"
      }
    ]
  }
]
```

## Conclusion

You have now successfully created a dataset using the "fill in the missing word(s)" strategy. This dataset can be used to train language models to predict missing words based on context. You can adjust the configuration parameters (such as `min_sentence_length` and `words_to_remove`) to create datasets of varying difficulty and complexity.

Remember to experiment with different input texts and configuration settings to create the most suitable dataset for your specific use case.
