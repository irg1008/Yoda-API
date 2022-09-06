from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection,
)
from motor.core import AgnosticDatabase, AgnosticCollection
from decouple import config
from typing import TypedDict

client = AsyncIOMotorClient(config("MONGO_URI"))

# Using agnostic for typing due to async not having type completion. 😿

db: AsyncIOMotorDatabase = client["yoda-db"]


api_keys: AsyncIOMotorCollection = db["api_keys"]
generations: AsyncIOMotorCollection = db["generations"]
suggestions: AsyncIOMotorCollection = db["suggestions"]
users: AsyncIOMotorCollection = db["users"]
