from pydantic import BaseModel


def to_camelCase(string: str):
    return string[0].lower() + string.title()[1:].replace("_", "")


class Model(BaseModel):
    class Config:
        alias_generator = to_camelCase
        allow_population_by_field_name = True
