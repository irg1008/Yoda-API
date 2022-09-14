from typing import Optional, Union

from pydantic import Field
from utils.models import Model

Color = list[str]
Size = list[Union[str, int]]


class Entities(Model):
    color: Optional[Color] = Field(example=["red", "blue"])
    size: Optional[Size] = Field(example=["small", "large", "43,5"])
