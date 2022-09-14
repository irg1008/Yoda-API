from typing import Optional

from pydantic import Field
from utils.models import Model

Entity = list[str]


class Entities(Model):
    color: Optional[Entity] = Field(None, example=["red", "blue"])
    size: Optional[Entity] = Field(None, example=["small", "large", "43,5"])
