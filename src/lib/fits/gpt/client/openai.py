import openai
from decouple import config
from .types import *
from transformers.models.gpt2.tokenization_gpt2_fast import GPT2TokenizerFast


class OpenAIClient:
    openai.api_key = config("OPENAI_API_KEY")

    @classmethod
    def infer(cls, options: CompletionArgs) -> tuple[str, int]:
        response: CompletionResponse = openai.Completion.create(**options)  # type: ignore
        return response["choices"][0]["text"], response["usage"]["total_tokens"]
