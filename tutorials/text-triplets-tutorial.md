# TextTriplets Workflow Tutorial

This tutorial will guide you through the TextTriplets workflow in the ModelTrainSet project, from data loading to model training. We'll examine each step of the process and discuss the design choices made.

## 1. Overview of TextTriplets

The TextTriplets workflow is designed to create a dataset for training language models on sentence prediction tasks. It works by breaking text into groups of three sentences, where the model learns to predict the third sentence given the first two.

## 2. Configuration

First, let's look at the configuration file for TextTriplets:

```yaml
creator_type: TextTripletsDatasetCreator
input_directory: ./data/text_files
output_file: ./datasets/text_triplets_dataset.json
```

This configuration specifies:

- The type of dataset creator to use
- The input directory containing text files
- The output file for the processed dataset

This design allows for easy customization and extension. You can add more parameters to the config file as needed, without changing the core code.

## 3. Data Loading

The TextTripletsDatasetCreator uses the TextLoader class to load data:

```python
class TextLoader(DataLoader):
    def load_data(self, config: Dict[str, Any]) -> List[Dict]:
        data = []
        input_dir = config['input_directory']
        for filename in os.listdir(input_dir):
            if filename.endswith('.txt'):
                with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                    cleaned_content = self.clean_text(content)
                    data.append({'text': cleaned_content, 'filename': filename})
        return data
```

The TextLoader is designed to handle multiple text files, cleaning each one as it's loaded. This approach allows for processing large datasets split across multiple files.

## 4. Data Processing

The TextTripletsProcessor class handles the core logic of creating the triplets:

```python
class TextTripletsProcessor(DataProcessor):
    def process_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        processed_data = []
        for item in data:
            sentences = nltk.sent_tokenize(item['text'])
            for i in range(len(sentences) - 2):
                processed_data.append({
                    'instruction': f"{sentences[i]} {sentences[i+1]}",
                    'completion': sentences[i+2],
                    'source': item['filename']
                })
        return processed_data
```

This processor creates overlapping triplets from the text, which allows the model to learn context across sentence boundaries. The inclusion of the source filename enables traceability and potential filtering later.

## 5. Data Formatting

The TextTripletsFormatter prepares the data for training:

```python
class TextTripletsFormatter(DataFormatter):
    def format_data(self, data: List[Dict], config: Dict[str, Any]) -> List[Dict]:
        entries = [
            {
                "conversations": [
                    {
                        "role": "user",
                        "content": f"Given the following two sentences, predict the next sentence that would logically follow:\n\n{item['instruction']}"
                    },
                    {
                        "role": "assistant",
                        "content": item['completion']
                    }
                ],
                "source": item['source']
            }
            for item in data
        ]
        import random
        random.shuffle(entries)
        return entries
```

The formatter structures the data as a conversation, making it suitable for training chatbot-style models. The random shuffling helps prevent the model from learning unintended patterns based on the order of the data.

## 6. Dataset Creation

The TextTripletsDatasetCreator ties everything together:

```python
class TextTripletsDatasetCreator(BaseDatasetCreator):
    def get_loader(self) -> DataLoader:
        return TextLoader()

    def get_processor(self) -> DataProcessor:
        return TextTripletsProcessor()

    def get_formatter(self) -> DataFormatter:
        return TextTripletsFormatter()
```

This class follows the Strategy pattern, allowing easy substitution of different loaders, processors, or formatters if needed.

## 7. Model Training

To train a model on the TextTriplets dataset, you would use a configuration like this:

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
dataset_file: ./datasets/text_triplets_dataset.json
```

This configuration uses LoRA (Low-Rank Adaptation) for efficient fine-tuning of large language models. It's set up for the Mistral 7B model, but you can easily adapt it for other models.

## 8. Running the Workflow

To create the dataset:

```bash
python main.py --mode dataset --config config/text_triplets_config.yaml
```

To train the model:

```bash
python main.py --mode train --config config/train_config.yaml
```

## Conclusion

The TextTriplets workflow demonstrates several key design principles:

1. Modularity: Each step (loading, processing, formatting) is separate and interchangeable.
2. Configuration-driven: Most parameters are set in config files, reducing the need for code changes.
3. Flexibility: The system can handle various input formats and can be extended for different tasks.
4. Efficiency: The use of LoRA and 4-bit quantization allows for fine-tuning large models on consumer hardware.

By following this workflow, you can create a custom dataset from text files and use it to fine-tune a large language model for sentence prediction tasks.
