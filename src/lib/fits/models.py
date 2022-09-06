from typing import Literal
from pydantic import BaseModel


class Completion(BaseModel):
    title: str
    estimated_price: float
    price_unit: Literal["USD"]

    class Config:
        schema_extra = {
            "example": {
                "title": "This a shorter text for title",
                "estimated_price": 0.0001,
                "price_unit": "USD",
            }
        }
