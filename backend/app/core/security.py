from datetime import datetime, timedelta, UTC
from jose import jwt
from jose import JWTError
from app.core.config import settings

def create_access_token(
    user: dict
    ):
    expire = datetime.now(UTC) + timedelta(
        days=settings.JWT_EXPIRE_DAYS
    )

    payload = {
    "sub": str(user["_id"]),
    "github_id": user["github_id"],
    "exp": expire,
}

    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )

def verify_access_token(
    token: str,
):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )

        return payload

    except JWTError:
        return None    