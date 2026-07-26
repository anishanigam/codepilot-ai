from fastapi import APIRouter, Query, Depends
from fastapi.responses import RedirectResponse, JSONResponse
from app.core.config import settings

from app.dependencies.auth import get_current_user
from app.services.auth_service import auth_service

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.get("/github/login")
async def github_login():

    url = auth_service.get_github_login_url()

    return RedirectResponse(url=url)


@router.get("/github/callback")
async def github_callback(
    code: str = Query(...)
):
    result = await auth_service.authenticate_with_github(code)

    response = RedirectResponse(
        url=f"{settings.FRONTEND_URL}/dashboard"
    )


    response.set_cookie(
        key="access_token",
        value=result["jwt"],
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60 * 24 * 7,
    )

    return response


@router.get("/me")
async def get_me(
    current_user=Depends(get_current_user),
):
    return {
        "id": str(current_user["_id"]),
        "github_id": current_user["github_id"],
        "username": current_user["username"],
        "name": current_user["name"],
        "avatar_url": current_user["avatar_url"],
    }


@router.post("/logout")
async def logout():
    response = JSONResponse(
        content={
            "message": "Logged out successfully"
        }
    )

    response.delete_cookie(
        key="access_token",
        httponly=True,
        secure=False,
        samesite="lax",
    )

    return response
