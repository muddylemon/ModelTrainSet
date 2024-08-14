class Config:
    def __init__(self, config_dict):
        self.model_name = config_dict.get('model_name')
        self.max_seq_length = config_dict.get('max_seq_length')
        self.load_in_4bit = config_dict.get('load_in_4bit', False)
        self.r = config_dict.get('r')
        self.target_modules = config_dict.get('target_modules')
        self.lora_alpha = config_dict.get('lora_alpha')
        self.lora_dropout = config_dict.get('lora_dropout')
        self.bias = config_dict.get('bias')
        self.use_gradient_checkpointing = config_dict.get(
            'use_gradient_checkpointing', False)
        self.random_state = config_dict.get('random_state')
        self.per_device_train_batch_size = config_dict.get(
            'per_device_train_batch_size')
        self.gradient_accumulation_steps = config_dict.get(
            'gradient_accumulation_steps')
        self.warmup_steps = config_dict.get('warmup_steps')
        self.num_train_epochs = config_dict.get('num_train_epochs')
        self.max_steps = config_dict.get('max_steps')
        self.learning_rate = config_dict.get('learning_rate')
        self.logging_steps = config_dict.get('logging_steps')
        self.weight_decay = config_dict.get('weight_decay')
        self.dataset_num_proc = config_dict.get('dataset_num_proc')
        self.packing = config_dict.get('packing', False)
        self.output_dir = config_dict.get('output_dir')
        self.push_to_hub = config_dict.get('push_to_hub', False)
        self.hf_username = config_dict.get('hf_username')
        self.trained_model_name = config_dict.get('trained_model_name')
        self.dataset_file = config_dict.get('dataset_file')

    def __repr__(self):
        return f"Config({self.__dict__})"
