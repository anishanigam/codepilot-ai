from fastapi import APIRouter, Query, Depends, HTTPException #type:ignore
from fastapi.responses import RedirectResponse, JSONResponse #type:ignore
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


@router.get("/github/login/private")
async def github_private_login():
    url = await auth_service.github_private_login()
    return RedirectResponse(url)


@router.get("/github/callback")
async def github_callback(
    code: str = Query(...),
    state: str = Query(...),
):
    VALID_STATES = {
        "login",
        "private_access",
    }

    if state not in VALID_STATES:
        raise HTTPException(
            status_code=400,
            detail="Invalid OAuth state",
        )
    result = await auth_service.authenticate_with_github(code)

    if state == "login":
        redirect_url = f"{settings.FRONTEND_URL}/dashboard"
    else:
        redirect_url = f"{settings.FRONTEND_URL}/repositories"

    response = RedirectResponse(url=redirect_url)


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
        "has_private_repo_access": "repo" in current_user.get("github_scopes", []),
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
