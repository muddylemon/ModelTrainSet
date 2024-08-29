# How to Cook Up a Text Completion Dataset: The Instruction Format Edition

Alright, cool cats! Grab your keyboards and put on your coding berets, 'cause we're about to embark on a groovy journey into the world of text completion datasets. We're gonna turn boring ol' text into a jazzy instruction format that'll make your AI model sing. Let's dive in!

## Step 1: Gather Your Ingredients

First things first, you'll need:

- A folder full of text files (let's call it "data/raw_texts/")
- Our ModelTrainSet project (if you don't have it, clone it faster than you can say "git")
- A computer (duh)
- A burning desire to make AIs complete sentences like a boss

## Step 2: Whip Up Your Config

Create a file named `text_completion_config.yaml` in your `config/` folder:

```yaml
creator_type: InstructionCreator
input_directory: ./data/raw_texts
output_file: ./datasets/text_completion_dataset.jsonl
min_context_length: 50
max_context_length: 200
completion_length: 50
samples_per_file: 100
```

This config is telling our system, "Hey, grab those texts, chop 'em up, and serve 'em on a silver platter for our AI to devour."

## Step 3: Create a TextCompletionProcessor

Now, let's create a new file `text_completion_processor.py` in the `dataset_creator/processors/` directory:

```python
import random
from typing import List, Dict, Any
from ..base import DataProcessor

class TextCompletionProcessor(DataProcessor):
    def process_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        processed_data = []
        for item in data:
            text = item['text']
            samples = self.create_samples(text, config)
            processed_data.extend(samples)
        return processed_data

    def create_samples(self, text: str, config: Dict[str, Any]) -> List[Dict]:
        samples = []
        words = text.split()
        for _ in range(config['samples_per_file']):
            context_length = random.randint(config['min_context_length'], config['max_context_length'])
            start_index = random.randint(0, len(words) - context_length - config['completion_length'])
            context = ' '.join(words[start_index:start_index + context_length])
            completion = ' '.join(words[start_index + context_length:start_index + context_length + config['completion_length']])
            samples.append({
                'prompt': f"Complete the following text:\n\n{context}",
                'completion': completion
            })
        return samples
```

This processor is like a DJ, sampling your text and creating sick beats... I mean, training samples.

## Step 4: Update Your InstructionCreator

Let's give our `InstructionCreator` a makeover. Open up `dataset_creator/creators/instruction_creator.py`:

```python
from ..base import BaseDatasetCreator, DataLoader, DataProcessor, DataFormatter
from ..loaders.text_loader import TextLoader
from ..processors.text_completion_processor import TextCompletionProcessor
from ..formatters.instruction_formatter import InstructionFormatter

class InstructionCreator(BaseDatasetCreator):
    def get_loader(self) -> DataLoader:
        return TextLoader()

    def get_processor(self) -> DataProcessor:
        return TextCompletionProcessor()

    def get_formatter(self) -> DataFormatter:
        return InstructionFormatter()
```

We've switched to `TextLoader` and added our new `TextCompletionProcessor`. It's like upgrading from a cassette player to a digital mixer!

## Step 5: Run This Bad Boy

Fire up your terminal and run:

```bash
python main.py --mode dataset --config config/text_completion_config.yaml
```

Sit back and watch as your computer turns into a literary food processor, chopping up text and serving it as delicious instruction-completion pairs.

## Step 6: Marvel at Your Creation

Once it's done, peek inside your `datasets/text_completion_dataset.jsonl`. You should see something like:

```json
{"messages": [{"role": "system", "content": "You are helpful"}, {"role": "user", "content": "Complete the following text:\n\nThe quick brown fox jumps over the"}, {"role": "assistant", "content": "lazy dog. It was a beautiful day in the forest, with"}]}
{"messages": [{"role": "system", "content": "You are helpful"}, {"role": "user", "content": "Complete the following text:\n\nIn a hole in the ground there lived a"}, {"role": "assistant", "content": "hobbit. Not a nasty, dirty, wet hole, filled with the"}]}
```

## Wrap It Up, Champ

And there you have it, folks! You've just created a text completion dataset that's hotter than a jalapeño popper at a Texas barbecue. With this power, you can:

- Train models to finish sentences like a mindreader
- Create writing prompts that would make Shakespeare jealous
- Finally prove to your English teacher that computers can write too

Remember, with great power comes great responsibility. Use your newfound abilities wisely. Don't go generating fake news or anything. Unless... no, nevermind. Just be cool, alright?

Now go forth and complete texts! And remember, in the words of definitely-not-AI Shakespeare: "To complete, or not to complete, that is the question... but the answer is always to complete!"

Happy formatting, you crazy cats!
