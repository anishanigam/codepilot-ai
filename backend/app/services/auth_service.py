from app.github.github_client import github_client
from app.repositories.user_repository import user_repository
from app.core.security import create_access_token


class AuthService:

    def get_github_login_url(self):

        return github_client.get_authorization_url()
    

    async def authenticate_with_github(self, code: str,):
        token_data = await github_client.exchange_code_for_token(code)

        if "access_token" not in token_data:
            raise Exception(f"GitHub OAuth failed: {token_data}")

        access_token = token_data["access_token"]

        github_user = await github_client.get_authenticated_user(
            access_token
        )

        user = await user_repository.upsert_user(
            github_user,
            access_token,
        )

        jwt_token = create_access_token(user)

        return {
            "jwt": jwt_token,
        }



auth_service = AuthService()