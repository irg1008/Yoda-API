from typing import TypedDict, Literal

from ..config.types import Model
from .tokenizer import encode

priced_tokens = 1000


class Prices(TypedDict):  # Per <_price_tokens> tokens
    training: float
    inference: float


prices: dict[Model, Prices] = {
    "ada": {
        "training": 0.004,
        "inference": 0.0004,
    },
    "babbage": {
        "training": 0.005,
        "inference": 0.0005,
    },
    "curie": {
        "training": 0.02,
        "inference": 0.002,
    },
    "davinci": {
        "training": 0.2,
        "inference": 0.02,
    },
}


def price_per_n_tokens(
    model: Model, n_tokens: int, price_type: Literal["training", "inference"]
) -> float:
    price = prices[model]
    return price[price_type] / priced_tokens * n_tokens


def price_of_string(string: str, model: Model) -> Prices:
    tokens = encode(string)
    training_price = price_per_n_tokens(model, len(tokens), "training")
    inference_price = price_per_n_tokens(model, len(tokens), "inference")
    return Prices(training=training_price, inference=inference_price)
