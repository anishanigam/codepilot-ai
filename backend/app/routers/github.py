from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.github.github_service import github_service

router = APIRouter(prefix="/api/github", tags=["GitHub"])


@router.get("/repositories")
async def get_repositories(current_user=Depends(get_current_user)):
    return await github_service.get_repositories(
        current_user["github_access_token"]
    )


@router.get("/repositories/{owner}/{repo}/pulls")
async def get_pull_requests(
    owner: str,
    repo: str,
    current_user=Depends(get_current_user),
):
    return await github_service.get_pull_requests(
        current_user["github_access_token"],
        owner,
        repo,
    )