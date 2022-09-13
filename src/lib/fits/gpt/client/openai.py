import openai
from decouple import config
from .types import *


class OpenAIClient:
    def __init__(self) -> None:
        openai.api_key = config("OPENAI_API_KEY")

    def infer(self, options: CompletionArgs) -> tuple[str, int]:
        response: CompletionResponse = openai.Completion.create(**options)  # type: ignore
        return response["choices"][0]["text"], response["usage"]["total_tokens"]
