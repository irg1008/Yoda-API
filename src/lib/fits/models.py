from typing import TypedDict, Literal
from pydantic import BaseModel


class FitsCompletion(TypedDict):
    title: str
    estimated_price: float
    price_unit: Literal["USD"]


class FitsModel(BaseModel):
    completion: FitsCompletion

    class Config:
        schema_extra = {
            "example": {
                "completion": "This a shorter text for title",
                "estimated_price": 0.0001,
                "price_unit": "USD",
            }
        }
