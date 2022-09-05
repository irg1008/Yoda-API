from pydantic import BaseModel

Entities = dict[str, list[str]]


class NerModel(BaseModel):
    entities: Entities

    class Config:
        schema_extra = {
            "example": {
                "entities": {
                    "color": ["red", "blue"],
                    "size": ["s", "l", "43.5"],
                    "brand": ["Zara", "Adidas"],
                }
            }
        }
