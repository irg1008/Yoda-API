from typing import Optional, Union
from utils.alias import Model

Entity = list[Union[str, int]]


class Entities(Model):
    color: Optional[Entity]
    size: Optional[Entity]

    class Config:
        schema_extra = {
            "example": {
                "color": ["red", "blue"],
                "size": ["s", "l", "43.5"],
                "brand": ["Zara", "Adidas"],
            }
        }
