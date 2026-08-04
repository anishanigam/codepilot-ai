import api from "./api";

export async function reviewPullRequest(
  owner,
  repo,
  pullNumber,
) {
  const response = await api.post(
    `/api/github/repositories/${owner}/${repo}/pulls/${pullNumber}/review`,
  );

  return response.data;
}