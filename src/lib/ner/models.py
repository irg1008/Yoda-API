from pydantic import Field
from utils.models import Model

Entity = list[str]


class Entities(Model):
    brand: Entity = Field(example=["Apple", "Nike"], default=[])
    color: Entity = Field(example=["red", "blue"], default=[])
    size: Entity = Field(example=["small", "large", "43,5"], default=[])
    energy: Entity = Field(example=["e--", "a++"], default=[])
