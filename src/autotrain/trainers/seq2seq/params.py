from typing import Optional

from pydantic import Field

from autotrain.trainers.common import AutoTrainParams


class Seq2SeqParams(AutoTrainParams):
    data_path: str = Field(None, title="Data path")
    model: str = Field("google/flan-t5-base", title="Model name")
    username: Optional[str] = Field(None, title="Hugging Face Username")
    seed: int = Field(42, title="Seed")
    train_split: str = Field("train", title="Train split")
    valid_split: Optional[str] = Field(None, title="Validation split")
    project_name: str = Field("project-name", title="Output directory")
    token: Optional[str] = Field(None, title="Hub Token")
    push_to_hub: bool = Field(False, title="Push to hub")
    text_column: str = Field("text", title="Text column")
    target_column: str = Field("target", title="Target text column")
    repo_id: Optional[str] = Field(None, title="Repo ID")
    lr: float = Field(5e-5, title="Learning rate")
    epochs: int = Field(3, title="Number of training epochs")
    max_seq_length: int = Field(128, title="Max sequence length")
    max_target_length: int = Field(128, title="Max target sequence length")
    batch_size: int = Field(8, title="Training batch size")
    warmup_ratio: float = Field(0.1, title="Warmup proportion")
    gradient_accumulation: int = Field(1, title="Gradient accumulation steps")
    optimizer: str = Field("adamw_torch", title="Optimizer")
    scheduler: str = Field("linear", title="Scheduler")
    weight_decay: float = Field(0.0, title="Weight decay")
    max_grad_norm: float = Field(1.0, title="Max gradient norm")
    logging_steps: int = Field(-1, title="Logging steps")
    evaluation_strategy: str = Field("epoch", title="Evaluation strategy")
    auto_find_batch_size: bool = Field(False, title="Auto find batch size")
    mixed_precision: Optional[str] = Field(None, title="fp16, bf16, or None")
    save_total_limit: int = Field(1, title="Save total limit")
    save_strategy: str = Field("no", title="Save strategy")
    token: Optional[str] = Field(None, title="Hub Token")
    push_to_hub: bool = Field(False, title="Push to hub")
    peft: bool = Field(False, title="Use PEFT")
    quantization: Optional[str] = Field("int4", title="int4, int8, or None")
    lora_r: int = Field(16, title="LoRA-R")
    lora_alpha: int = Field(32, title="LoRA-Alpha")
    lora_dropout: float = Field(0.05, title="LoRA-Dropout")
    target_modules: str = Field("all-linear", title="Target modules for PEFT")
