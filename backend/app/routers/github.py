from fastapi import APIRouter, Depends #type:ignore

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

@router.get("/repositories/{owner}/{repo}/pulls/{pull_number}")
async def get_pull_request_details(
    owner: str,
    repo: str,
    pull_number: int,
    current_user=Depends(get_current_user),
):
    return await github_service.get_pull_request_details(
        current_user["github_access_token"],
        owner,
        repo,
        pull_number,
    )


@router.get("/repositories/{owner}/{repo}/pulls/{pull_number}/files")
async def get_pull_request_files(
    owner: str,
    repo: str,
    pull_number: int,
    current_user=Depends(get_current_user),
):
    return await github_service.get_pull_request_files(
        current_user["github_access_token"],
        owner,
        repo,
        pull_number,
    )