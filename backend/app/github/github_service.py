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
            }
            for repo in repos
        ]


github_service = GitHubService()