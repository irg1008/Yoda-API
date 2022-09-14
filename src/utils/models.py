from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime
from .pyobject import PyObjectId


def to_camelCase(string: str):
    return string[0].lower() + string.title()[1:].replace("_", "")


class Model(BaseModel):
    # Override dict method so "None" and "null" are ignored on response models.
    # def dict(self, *args, **kwargs):
    #     kwargs.pop("exclude_none", None)
    #     return super().dict(*args, exclude_none=True, **kwargs)

    class Config:
        alias_generator = to_camelCase
        allow_population_by_field_name = True


class DBModel(Model):
    id: str = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}
