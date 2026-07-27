import { useQuery } from "@tanstack/react-query";
import { Link } from "react-router-dom";

import api from "../services/api";
import { useAuth } from "../contexts/AuthContext";
import { enablePrivateRepos } from "../services/authService";

function Repositories() {
  const {
    data: repositories = [],
    isLoading,
    isError,
  } = useQuery({
    queryKey: ["repositories"],
    queryFn: async () => {
      const response = await api.get("/api/github/repositories");
      return response.data;
    },
  });

  const { user } = useAuth();

  const hasPrivateAccess = user?.has_private_repo_access ?? false;

  const publicRepositories = repositories.filter(
    (repo) => !repo.private
  );

  const privateRepositories = repositories.filter(
    (repo) => repo.private
  );

  if (isLoading) {
    return <h2>Loading repositories...</h2>;
  }

  if (isError) {
    return <h2>Failed to load repositories.</h2>;
  }

  return (
    <>
      <h2 className="mb-8 text-3xl font-bold">
        Your Repositories
      </h2>

      {/* ================= PUBLIC REPOSITORIES ================= */}

      <div className="rounded-xl border bg-white p-6 shadow-sm">
        <h3 className="mb-5 text-2xl font-semibold">
          🌍 Public Repositories ({publicRepositories.length})
        </h3>

        <div className="grid gap-4">
          {publicRepositories.length > 0 ? (
            publicRepositories.map((repo) => (
              <Link
                key={repo.id}
                to={`/repositories/${repo.owner.login}/${repo.name}`}
                className="block rounded-lg border p-4 transition hover:shadow-md"
              >
                <h4 className="text-xl font-semibold transition-colors hover:text-blue-600">
                  {repo.name}
                </h4>

                <p className="text-gray-500">
                  {repo.full_name}
                </p>

                {repo.description && (
                  <p className="mt-2 text-sm text-gray-600">
                    {repo.description}
                  </p>
                )}

                <p className="mt-3 text-sm font-medium text-green-600">
                  🌍 Public
                </p>
              </Link>
            ))
          ) : (
            <div className="rounded-lg border bg-gray-50 p-6 text-center">
              <p className="text-gray-500">
                No public repositories found.
              </p>
            </div>
          )}
        </div>
      </div>

      {/* ================= PRIVATE REPOSITORIES ================= */}

      {hasPrivateAccess ? (
        <div className="mt-8 rounded-xl border bg-white p-6 shadow-sm">
          <h3 className="mb-5 text-2xl font-semibold">
            🔒 Private Repositories ({privateRepositories.length})
          </h3>

          <div className="grid gap-4">
            {privateRepositories.length > 0 ? (
              privateRepositories.map((repo) => (
                <Link
                  key={repo.id}
                  to={`/repositories/${repo.owner.login}/${repo.name}`}
                  className="block rounded-lg border p-4 transition hover:shadow-md"
                >
                  <h4 className="text-xl font-semibold transition-colors hover:text-blue-600">
                    {repo.name}
                  </h4>

                  <p className="text-gray-500">
                    {repo.full_name}
                  </p>

                  {repo.description && (
                    <p className="mt-2 text-sm text-gray-600">
                      {repo.description}
                    </p>
                  )}

                  <p className="mt-3 text-sm font-medium text-red-600">
                    🔒 Private
                  </p>
                </Link>
              ))
            ) : (
              <div className="rounded-lg border bg-gray-50 p-6 text-center">
                <p className="text-gray-500">
                  No private repositories found.
                </p>
              </div>
            )}
          </div>
        </div>
      ) : (
        <div className="mt-8 rounded-xl border border-yellow-300 bg-yellow-50 p-6 shadow-sm">
          <h3 className="text-2xl font-semibold">
            🔒 Private Repositories
          </h3>

          <p className="mt-2 text-gray-700">
            Connect your GitHub account with additional permissions to review pull requests from your private repositories.
          </p>

          <button
            onClick={enablePrivateRepos}
            className="mt-5 rounded-lg bg-black px-6 py-3 text-white transition hover:bg-gray-800"
          >
            Enable Private Repository Access
          </button>
        </div>
      )}
    </>
  );
}

export default Repositories;