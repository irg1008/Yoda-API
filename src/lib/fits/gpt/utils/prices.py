from typing import TypedDict, Literal

from ..config.types import Model

priced_tokens = 1000


class Prices(TypedDict):  # Per <priced_tokens> tokens
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
