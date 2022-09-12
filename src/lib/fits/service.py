import numpy as np
from .gpt.client.openai import OpenAIClient
from .gpt.config.const import config, fine_tune_config
from .gpt.utils.tokenizer import encode
from .gpt.utils.prices import price_per_n_tokens
from .gpt.utils.tokenizer import get_tokenizer, encode, decode


class FitsService:
    def __init__(self):
        self.tokenizer = get_tokenizer()
        self.client = OpenAIClient()

    def _encode(self, text: str):
        return encode(self.tokenizer, text)

    def _decode(self, tokens: list[int]):
        return decode(self.tokenizer, tokens)

    def _get_infer_price(self, n_tokens: int) -> float:
        return price_per_n_tokens(fine_tune_config["model_base"], n_tokens, "inference")

    def get_max_tokens_for_prompt(self, prompt: str) -> int:
        final_prompt = prompt + config["completion_end"]

        n_tokens = len(self._encode(final_prompt))
        token_downsample = np.floor(config["max_token_downsample"] * n_tokens)
        max_tokens = np.clip(
            token_downsample, config["min_tokens"], config["max_tokens"]
        )

        return int(max_tokens)

    def infer(self, text: str) -> tuple[str, float]:
        completion, n_tokens = self.client.infer(
            {
                "prompt": f"${config['prompt_start']}${text}${config['prompt_end']}",
                "model": config["model_name"],
                "max_tokens": self.get_max_tokens_for_prompt(text),
                "stop": config["completion_end"],
                "temperature": 0.2,
                "top_p": 0.5,
                "echo": False,
            },
        )
        completion = completion.replace(config["completion_start"], "")
        price = self._get_infer_price(n_tokens)
        return completion, price
