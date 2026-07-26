from app.github.github_client import github_client

class GitHubService:

    async def get_repositories(self, access_token: str):
        repos = await github_client.get_repositories(access_token)

        return [
            {
                "id": repo["id"],
                "name": repo["name"],
                "full_name": repo["full_name"],
                "private": repo["private"],
                "default_branch": repo["default_branch"],
                "updated_at": repo["updated_at"],
                "owner": {
                    "login": repo["owner"]["login"]
                    }
            }
            for repo in repos
        ]



    async def get_pull_requests(
        self,
        access_token,
        owner,
        repo,
    ):
        pulls = await github_client.get_pull_requests(
            access_token,
            owner,
            repo,
        )

        return [
            {
                "number": pr["number"],
                "title": pr["title"],
                "state": pr["state"],
                "author": pr["user"]["login"],
                "created_at": pr["created_at"],
            }
        for pr in pulls
    ]
    
    

github_service = GitHubService()