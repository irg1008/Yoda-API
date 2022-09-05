from typing import TypedDict, Union


class _CompletionArgsBase(TypedDict):
    model: str


class CompletionArgs(_CompletionArgsBase, total=False):
    prompt: str
    suffix: str
    max_tokens: int
    temperature: float
    top_p: float
    n: int
    stream: bool
    logprobs: int
    echo: bool
    stop: Union[str, list[str]]
    presence_penalty: float
    frequency_penalty: float
    best_of: int
    logit_bias: dict[str, float]
    user: str


class CompletionChoice(TypedDict):
    text: str
    index: int
    logprobs: int
    finish_reason: str


class CompletionUsage(TypedDict):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class CompletionResponse(TypedDict):
    id: str
    object: str
    created: int
    model: str
    choices: list[CompletionChoice]
    usage: CompletionUsage
