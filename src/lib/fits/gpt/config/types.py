from typing import Literal, TypedDict

Model = Literal["ada", "babbage", "curie", "davinci"]


class Config(TypedDict):
    model_name: str
    max_prompt_length: int
    min_tokens: int
    max_tokens: int
    max_token_downsample: float  # 0.0 to 1.0
    prompt_start: str
    prompt_end: str
    completion_start: str
    completion_end: str


class FineTuneConfig(TypedDict):
    model_base: Model
    model_name: str
    version: str
    batch_size: int
    epochs: int
