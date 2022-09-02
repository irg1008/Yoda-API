from transformers.models.gpt2.tokenization_gpt2_fast import GPT2TokenizerFast


def get_tokenizer():
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    return tokenizer


def encode(tokenizer: GPT2TokenizerFast, text: str) -> list[int]:
    tokens = tokenizer.encode(text)
    return tokens


def decode(tokenizer: GPT2TokenizerFast, tokens: list[int]) -> str:
    text = tokenizer.decode(tokens)
    return text
