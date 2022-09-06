from pydantic import Field
from enum import Enum
from utils.models import DBModel
from utils.pyobject import PyObjectId


class Generation(DBModel):
    input: str
    output: str
    api_key_id: PyObjectId


class Suggestion(DBModel):
    generation_id: PyObjectId
    is_correct: bool
    suggestion: str
    approved: bool = Field(default=False)


class ApiKey(DBModel):
    api_key: str
    name: str


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(DBModel):
    username: str
    email: str
    password: str
    verified: bool = Field(default=False)
    role: Role = Field(default=Role.user)
