from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection,
)
from motor.core import AgnosticCollection
from decouple import config

client = AsyncIOMotorClient(config("MONGO_URI"))
print("Connected to DB")


db: AsyncIOMotorDatabase = client["yoda-db"]

# Check "AgnosticCollection" for type completion. 😿

api_keys: AsyncIOMotorCollection = db["api_keys"]
generations: AsyncIOMotorCollection = db["generations"]
suggestions: AsyncIOMotorCollection = db["suggestions"]
users: AsyncIOMotorCollection = db["users"]
