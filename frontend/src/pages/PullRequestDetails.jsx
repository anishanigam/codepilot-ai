import { useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";

import api from "../services/api";
import { reviewPullRequest } from "../services/reviewService";
import { useState } from "react";

function PullRequestDetails() {
  const { owner, repo, pullNumber } = useParams();
  const [review, setReview] = useState(null);
  const [reviewLoading, setReviewLoading] = useState(false);

  const { data: pr, isLoading } = useQuery({
    queryKey: ["pull-request", owner, repo, pullNumber],
    queryFn: async () => {
      const response = await api.get(
        `/api/github/repositories/${owner}/${repo}/pulls/${pullNumber}`,
      );

      return response.data;
    },
  });

  const { data: files = [] } = useQuery({
    queryKey: ["pull-request-files", owner, repo, pullNumber],
    queryFn: async () => {
      const response = await api.get(
        `/api/github/repositories/${owner}/${repo}/pulls/${pullNumber}/files`,
      );

      return response.data;
    },
  });

  const handleReview = async () => {
    try {
      setReviewLoading(true);

      const result = await reviewPullRequest(owner, repo, pullNumber);

      setReview(result);
    } catch (error) {
      console.error(error);
    } finally {
      setReviewLoading(false);
    }
  };

  if (isLoading) {
    return <h2>Loading pull request...</h2>;
  }

  return (
    <>
      <h2 className="text-3xl font-bold">PR #{pr.number}</h2>

      <h3 className="mt-4 text-2xl font-semibold">{pr.title}</h3>

      <p className="mt-2 text-gray-500">By {pr.author.login}</p>

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

      {/* DESCRIPTION SECTION */}
      <div className="mt-8 rounded-lg border bg-white p-6">
        <h3 className="mb-4 text-xl font-semibold">Description</h3>

        <p className="whitespace-pre-wrap">
          {pr.body || "No description provided."}
        </p>
      </div>

      {/* CHANGED FILES SECTION */}
      <div className="mt-8 rounded-lg border bg-white p-6">
        <h3 className="mb-4 text-xl font-semibold">
          Changed Files ({files.length})
        </h3>

        <div className="space-y-4">
          {files.map((file) => (
            <div key={file.filename} className="rounded-lg border p-4">
              <div className="flex items-center justify-between">
                <h4 className="font-medium">{file.filename}</h4>

                <span className="text-sm text-gray-500">{file.status}</span>
              </div>

              <div className="mt-2 flex gap-4 text-sm">
                <span className="text-green-600">+{file.additions}</span>

                <span className="text-red-600">-{file.deletions}</span>

                <span>{file.changes} changes</span>
              </div>

              {file.patch ? (
                <pre className="mt-4 overflow-x-auto rounded bg-gray-100 p-4 text-xs whitespace-pre-wrap">
                  {file.patch}
                </pre>
              ) : (
                <p className="mt-4 text-sm text-gray-500">
                  No textual diff available (binary or unsupported file).
                </p>
              )}
            </div>
          ))}
        </div>
      </div>

      <button
        onClick={handleReview}
        disabled={reviewLoading}
        className="mt-8 rounded-lg bg-black px-6 py-3 text-white hover:bg-gray-800 disabled:opacity-50"
      >
        {reviewLoading ? "Reviewing..." : "🤖 Review with AI"}
      </button>

      {/* Temporary Review JSON */}
      {review && (
        <div className="mt-8 rounded-lg border bg-gray-100 p-4">
          <h3 className="mb-4 text-lg font-semibold">AI Review Response</h3>

          <pre className="overflow-x-auto text-xs">
            {JSON.stringify(review, null, 2)}
          </pre>
        </div>
      )}
    </>
  );
}

export default PullRequestDetails;
