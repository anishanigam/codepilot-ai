from app.github.github_client import github_client
from app.repositories.user_repository import user_repository
from app.core.security import create_access_token
from app.core.logger import get_logger

logger = get_logger(__name__)


class AuthService:

    PUBLIC_SCOPE = "read:user user:email public_repo"

    PRIVATE_SCOPE = "read:user user:email repo"

    def get_github_login_url(self):
        return github_client.get_authorization_url(
            scope=self.PUBLIC_SCOPE,
            state="login",
        )
    
    async def github_private_login(self):
        return github_client.get_authorization_url(
            scope = self.PRIVATE_SCOPE,
            state="private_access"
        )

    async def authenticate_with_github(self, code: str,):
        token_data = await github_client.exchange_code_for_token(code)
        logger.info("Token received")

        if "access_token" not in token_data:
            raise Exception(f"GitHub OAuth failed: {token_data}")

        access_token = token_data["access_token"]

        logger.info("Fetching GitHub user...")

        github_user = await github_client.get_authenticated_user(
            access_token
        )
        logger.info("User fetched")

        github_scopes = await github_client.get_github_scopes(
        access_token
    )

        user = await user_repository.upsert_user(
            github_user=github_user,
            access_token=access_token,
            github_scopes=github_scopes,
        )

        jwt_token = create_access_token(user)

        return {
            "jwt": jwt_token,
        }



auth_service = AuthService()