from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

from app.core.config import settings


class DatabaseManager:

    def __init__(self):
        self.client: AsyncMongoClient | None = None
        self.database: AsyncDatabase | None = None

    async def connect(self):
        self.client = AsyncMongoClient(settings.MONGODB_URI)

        self.database = self.client[
            settings.DATABASE_NAME
        ]

        print("✅ MongoDB Connected")

    async def disconnect(self):
        if self.client:
            await self.client.close()
            print("❌ MongoDB Disconnected")


db = DatabaseManager()