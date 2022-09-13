from transformers.models.gpt2.tokenization_gpt2_fast import GPT2TokenizerFast
from os import path
import logging


def get_tokenizer():
    cache_dir = path.abspath(
        path.join(path.dirname(__file__), "../../../../../models", "tokenizers")
    )
    if not path.exists(cache_dir):
        logging.info(f"Creating cache dir {cache_dir} for tokenizer")
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2", cache_dir=cache_dir)
    return tokenizer


def encode(tokenizer: GPT2TokenizerFast, text: str) -> list[int]:
    tokens = tokenizer.encode(text)
    return tokens


def decode(tokenizer: GPT2TokenizerFast, tokens: list[int]) -> str:
    text = tokenizer.decode(tokens)
    return text
