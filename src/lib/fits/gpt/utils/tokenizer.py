from transformers.models.gpt2.tokenization_gpt2 import GPT2Tokenizer
from os import path


def get_tokenizer():
    cache_dir = path.abspath(
        path.join(path.dirname(__file__), "../../../../../models", "tokenizers")
    )
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2", cache_dir=cache_dir)
    return tokenizer


def encode(tokenizer: GPT2Tokenizer, text: str) -> list[int]:
    tokens = tokenizer.encode(text)
    return tokens


def decode(tokenizer: GPT2Tokenizer, tokens: list[int]) -> str:
    text = tokenizer.decode(tokens)
    return text
