from typing import Optional

from pydantic import Field
from utils.models import Model

Entity = list[str]


class Entities(Model):
    brand: Optional[Entity] = Field(example=["Apple", "Nike"])
    color: Optional[Entity] = Field(example=["red", "blue"])
    size: Optional[Entity] = Field(example=["small", "large", "43,5"])
