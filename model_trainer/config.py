class Config:
    def __init__(self, config_dict):
        self.trained_model_name = config_dict.get('trained_model_name')
        self.dataset_file = config_dict.get('dataset_file')
        # From Pretrained
        self.model_name = config_dict.get('model_name')
        self.max_seq_length = config_dict.get('max_seq_length', 2048)
        self.load_in_4bit = config_dict.get('load_in_4bit', False)
        # peft model
        self.r = config_dict.get('r', 16)
        self.target_modules = config_dict.get('target_modules', None)
        self.lora_alpha = config_dict.get('lora_alpha', 16)
        self.lora_dropout = config_dict.get('lora_dropout', 0.05)
        self.bias = config_dict.get('bias', 'none')
        self.use_gradient_checkpointing = config_dict.get(
            'use_gradient_checkpointing', False)
        self.random_state = config_dict.get('random_state', 4237)
        # Training Arguments
        self.optim = config_dict.get('optim', 'adamw_8bit')
        self.output_dir = config_dict.get('output_dir')
        self.learning_rate = config_dict.get('learning_rate', 2.0e-4)
        self.per_device_train_batch_size = config_dict.get(
            'per_device_train_batch_size', 4)
        self.gradient_accumulation_steps = config_dict.get(
            'gradient_accumulation_steps', 1)
        self.num_train_epochs = config_dict.get('num_train_epochs', 1)
        self.weight_decay = config_dict.get('weight_decay', 0.0)
        self.warmup_ratio = config_dict.get('warmup_ratio', 0.1)
        self.lr_scheduler_type = config_dict.get('lr_scheduler_type', 'linear')
        self.warmup_steps = config_dict.get('warmup_steps', 10)
        self.logging_steps = config_dict.get('logging_steps', 100)
        # SFT Trainer
        self.max_seq_length = config_dict.get('max_seq_length', 2048)
        self.dataset_num_proc = config_dict.get('dataset_num_proc', 4)
        self.packing = config_dict.get('packing', False)
        self.eval_steps = config_dict.get('eval_steps', 100)
        self.evaluation_strategy = config_dict.get('evaluation_strategy', 'steps')
        self.save_strategy = config_dict.get('save_strategy', 'steps')
        self.save_steps = config_dict.get('save_steps', 100)
        self.load_best_model_at_end = config_dict.get('load_best_model_at_end', True)
        # Others
        self.max_steps = config_dict.get('max_steps', None)
        self.push_to_hub = config_dict.get('push_to_hub', False)
        self.hf_username = config_dict.get('hf_username')

    def __repr__(self):
        return f"Config({self.__dict__})"
