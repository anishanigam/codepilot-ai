from typing import TypedDict
from datetime import datetime


class UserDocument(TypedDict):

    github_id: int

    username: str

    name: str | None

    email: str | None

    avatar_url: str

    github_access_token: str

    created_at: datetime

    updated_at: datetime