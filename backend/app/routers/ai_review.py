from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user

from app.github.github_service import github_service
from app.ai.review_service import review_service

router = APIRouter(
    prefix="/api/ai",
    tags=["AI Review"],
)


@router.post(
    "/review/{owner}/{repo}/{pull_number}"
)
async def review_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    current_user=Depends(get_current_user),
):

    files = await github_service.get_pull_request_files(
        current_user["github_access_token"],
        owner,
        repo,
        pull_number,
    )

    result = await review_service.review(
        files
    )

    return result