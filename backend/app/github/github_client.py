import httpx

from app.core.config import settings
from urllib.parse import urlencode


class GitHubClient:

    BASE_API_URL = "https://api.github.com"
    OAUTH_URL = "https://github.com/login/oauth/access_token"

    def __init__(self):
        self.client_id = settings.GITHUB_CLIENT_ID
        self.client_secret = settings.GITHUB_CLIENT_SECRET

        self.client = httpx.AsyncClient(
            headers={
                "Accept": "application/json"
            }
        )
    

    async def exchange_code_for_token(self, code: str):

        try:
            response = await self.client.post(
            self.OAUTH_URL,
            json={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "code": code,
            },
        )
            
        except Exception as e:
            print("EXCEPTION:", type(e).__name__)
            print(e)
            raise

        response.raise_for_status()
        
        data = response.json()
        return data
   


    async def get_authenticated_user(self,access_token: str,):

        response = await self.client.get(
            f"{self.BASE_API_URL}/user",
            headers={
                "Authorization": f"Bearer {access_token}"
            },
        )

        response.raise_for_status()

        return response.json()
    

    def get_authorization_url(self):

        params = {
           "client_id": self.client_id,
            "scope": "read:user user:email",
        }

        return (
            "https://github.com/login/oauth/authorize?"
            + urlencode(params)
        )
    

    async def get_repositories(self, access_token: str):
        response = await self.client.get(
            "https://api.github.com/user/repos",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/vnd.github+json",
            },
            params={
                "sort": "updated",
                "per_page": 100,
            },
        )

        response.raise_for_status()
        return response.json()    


    async def get_pull_requests(
        self,
        access_token: str,
        owner: str,
        repo: str,
    ):
        response = await self.client.get(
            f"https://api.github.com/repos/{owner}/{repo}/pulls",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/vnd.github+json",
            },
        )

        response.raise_for_status()
        return response.json()

    
    async def close(self):
        await self.client.aclose()



github_client = GitHubClient()