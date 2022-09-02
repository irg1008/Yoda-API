from typing import TypedDict, Literal
from pydantic import BaseModel


class FITSCompletion(TypedDict):
    completion: str
    estimated_price: float
    price_unit: Literal["USD"]


class FITSModel(BaseModel):
    completion: FITSCompletion

    class Config:
        schema_extra = {
            "example": {
                "completion": "This a shorter text for title",
                "estimated_price": 0.0001,
                "price_unit": "USD",
            }
        }
