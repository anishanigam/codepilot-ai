from datetime import datetime, timezone
from bson import ObjectId

from app.core.database import db


class UserRepository:

    @property
    def collection(self):
        return db.database["users"]
    

    async def get_by_github_id(self,github_id: int,):

        return await self.collection.find_one(
        {
            "github_id": github_id
        }
    )

    async def upsert_user(self, github_user: dict,access_token: str,):

        now = datetime.now(timezone.utc)

        await self.collection.update_one(
        {
            "github_id": github_user["id"]
        },
        {
            "$set": {
                "username": github_user["login"],
                "name": github_user.get("name"),
                "email": github_user.get("email"),
                "avatar_url": github_user["avatar_url"],
                "github_access_token": access_token,
                "updated_at": now,
            },
            "$setOnInsert": {
                "created_at": now,
            },
        },
        upsert=True,
    )

        return await self.get_by_github_id(
            github_user["id"]
    )


    async def get_by_id(self, user_id: str):
        return await self.collection.find_one(
            {"_id": ObjectId(user_id)}
            )


user_repository = UserRepository()