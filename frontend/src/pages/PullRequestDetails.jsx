import { useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";

import api from "../services/api";

function PullRequestDetails() {
  const { owner, repo, pullNumber } = useParams();

  const { data: pr, isLoading } = useQuery({
    queryKey: ["pull-request", owner, repo, pullNumber],
    queryFn: async () => {
      const response = await api.get(
        `/api/github/repositories/${owner}/${repo}/pulls/${pullNumber}`
      );

      return response.data;
    },
  });

  if (isLoading) {
    return <h2>Loading pull request...</h2>;
  }

  return (
    <>
      <h2 className="text-3xl font-bold">
        PR #{pr.number}
      </h2>

      <h3 className="mt-4 text-2xl font-semibold">
        {pr.title}
      </h3>

      <p className="mt-2 text-gray-500">
        By {pr.author.login}
      </p>

      <div className="mt-6 rounded-lg border bg-white p-6">
        <p>
          <strong>Status:</strong> {pr.state}
        </p>

        <p>
          <strong>Base Branch:</strong> {pr.base_branch}
        </p>

        <p>
          <strong>Head Branch:</strong> {pr.head_branch}
        </p>

        <p>
          <strong>Commits:</strong> {pr.commits}
        </p>

        <p>
          <strong>Files Changed:</strong> {pr.changed_files}
        </p>

        <p>
          <strong>Additions:</strong> +{pr.additions}
        </p>

        <p>
          <strong>Deletions:</strong> -{pr.deletions}
        </p>
      </div>

      <div className="mt-8 rounded-lg border bg-white p-6">
        <h3 className="mb-4 text-xl font-semibold">
          Description
        </h3>

        <p className="whitespace-pre-wrap">
          {pr.body || "No description provided."}
        </p>
      </div>

      <button
        className="mt-8 rounded-lg bg-black px-6 py-3 text-white hover:bg-gray-800"
      >
        🤖 Review with AI
      </button>
    </>
  );
}

export default PullRequestDetails;