from app.github.github_client import github_client
from app.ai.models import GitHubFile

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

    async def get_pull_request_details(
        self,
        access_token: str,
        owner: str,
        repo: str,
        pull_number: int,
    ):
        pr = await github_client.get_pull_request_details(
            access_token,
            owner,
            repo,
            pull_number,
        )

        return {
            "number": pr["number"],
            "title": pr["title"],
            "body": pr["body"],
            "state": pr["state"],
            "draft": pr["draft"],
            "merged": pr["merged"],
            "created_at": pr["created_at"],
            "updated_at": pr["updated_at"],
            "additions": pr["additions"],
            "deletions": pr["deletions"],
            "changed_files": pr["changed_files"],
            "commits": pr["commits"],
            "base_branch": pr["base"]["ref"],
            "head_branch": pr["head"]["ref"],
            "author": {
                "login": pr["user"]["login"],
                "avatar_url": pr["user"]["avatar_url"],
            },
        }


    async def get_pull_request_files(
        self,
        access_token: str,
        owner: str,
        repo: str,
        pull_number: int,
    ) -> list[GitHubFile]:

        files = await github_client.get_pull_request_files(
            access_token,
            owner,
            repo,
            pull_number,
        )

        return [
            GitHubFile(
                filename=file["filename"],
                status=file["status"],
                patch=file.get("patch"),
                additions=file["additions"],
                deletions=file["deletions"],
                changes=file["changes"],
            )
            for file in files
        ]
    
    

github_service = GitHubService()