from typing import TypedDict, Literal, TypeVar, Generic, Optional, Union
from typing_extensions import NotRequired


# region NER


class TokenClassInferParameters(TypedDict, total=False):
    aggregation_strategy: Literal[None, "simple", "first", "average", "max"]


class TokenClassResponse(TypedDict):
    entity_group: str
    score: float
    word: str
    start: int
    end: int


# endregion

# region FITS


class TextSumInferParameters(TypedDict, total=False):
    min_length: int
    max_length: int
    top_k: int
    top_p: float
    temperature: float  # 0-100
    repetition_penalty: float  # 0-100
    max_time: float  # 0-120


class TextSumResponse(TypedDict):
    summary_text: str


# endregion

Parameters = Union[TokenClassInferParameters, TextSumInferParameters]

TResponse = TypeVar("TResponse", TokenClassResponse, TextSumResponse)
TParameters = TypeVar("TParameters", bound=Parameters)


class InferOptions(TypedDict, total=False):
    use_gpu: bool
    use_cache: bool
    wait_for_model: bool


class Payload(TypedDict):
    inputs: str
    options: NotRequired[InferOptions]
    parameters: Optional[Parameters]
