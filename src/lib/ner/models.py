from pydantic import BaseModel
from .inference import Entities


class NERInferenceModel(BaseModel):
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
