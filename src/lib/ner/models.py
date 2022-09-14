from typing import Optional, Union

from pydantic import Field
from utils.models import Model

Entity = list[str]


class Entities(Model):
    color: Optional[Entity] = Field(example=["red", "blue"])
    size: Optional[Entity] = Field(example=["small", "large", "43,5"])
