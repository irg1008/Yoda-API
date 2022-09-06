from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from motor.core import AgnosticDatabase, AgnosticCollection
from decouple import config

client = AsyncIOMotorClient(config("MONGO_URI"))

# Using agnostic for typing due to async not having type completion. 😿

db: AgnosticDatabase = client["yoda-db"]
