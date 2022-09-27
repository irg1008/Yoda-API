from typing import TypedDict, Literal


class InferOptions(TypedDict, total=False):
    use_gpu: bool
    use_cache: bool
    wait_for_model: bool


# region NER


class NERInferParameters(TypedDict, total=False):
    aggregation_strategy: Literal[None, "simple", "first", "average", "max"]


class NERInferPayloadBase(TypedDict):
    inputs: str


class NERInferPayload(NERInferPayloadBase, total=False):
    parameters: NERInferParameters
    options: InferOptions


class NERResponse(TypedDict):
    entity_group: str
    score: float
    word: str
    start: int
    end: int


# endregion

# region FITS


class FITSInferParameters(TypedDict, total=False):
    min_length: int
    max_length: int
    top_k: int
    top_p: float
    temperature: float  # 0-100
    repetition_penalty: float  # 0-100
    max_time: float  # 0-120


class FITSInferPayloadBase(TypedDict):
    inputs: str


class FITSInferPayload(FITSInferPayloadBase, total=False):
    parameters: FITSInferParameters
    options: InferOptions


class FITSResponse(TypedDict):
    summary_text: str


# endregion
