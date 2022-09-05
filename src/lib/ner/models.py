from pydantic import BaseModel
from typing import Optional, Union

Entity = list[Union[str, int]]


class Entities(BaseModel):
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
