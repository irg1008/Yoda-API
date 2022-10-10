from enum import Enum

from pydantic import Field
from utils.models import Model


class PriceUnit(str, Enum):
    USD = "USD"


class Completion(Model):
    title: str = Field(example="A short title given a much longer one")
    estimated_price: float = Field(example=4e-5)
    price_unit: PriceUnit = Field(default=PriceUnit.USD, example=PriceUnit.USD)
