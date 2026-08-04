from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import db
from app.routers.auth import router as auth_router
from app.routers.github import router as github_router
from app.routers.ai_review import (
    router as ai_review_router,
)
from app.core.logger import configure_logging

configure_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):

    await db.connect()

    yield

    await db.disconnect()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# registers routers
app.include_router(auth_router)
app.include_router(github_router)
app.include_router(
    ai_review_router
)

@app.get("/")
async def root():
    return {
        "message": "Backend Running 🚀"
    }