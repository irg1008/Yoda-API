from enum import Enum

from pydantic import Field
from utils.models import Model


class PriceUnit(str, Enum):
    USD = "USD"


class Completion(Model):
    title: str = Field(example="A short title given a much longer one")
