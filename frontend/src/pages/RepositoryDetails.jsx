import { useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import api from "../services/api";
import { Link } from "react-router-dom";

function RepositoryDetails() {
  const { owner, repo } = useParams();

  const { data: pullRequests = [], isLoading } = useQuery({
    queryKey: ["pulls", owner, repo],
    queryFn: async () => {
      const response = await api.get(
        `/api/github/repositories/${owner}/${repo}/pulls`
      );
      return response.data;
    },
  });

  if (isLoading) {
    return <p>Loading pull requests...</p>;
  }

  return (
    <>
      <h2 className="text-3xl font-bold">
        {owner} / {repo}
      </h2>

      <div className="mt-8 space-y-4">
        {pullRequests.length === 0 ? (
          <p>No open pull requests.</p>
        ) : (
          pullRequests.map((pr) => (
            <Link
                key={pr.number}
                to={`/repositories/${owner}/${repo}/pulls/${pr.number}`}
                className="block rounded-lg border bg-white p-4 shadow transition hover:shadow-md"
              >
              <h3 className="font-semibold">
                #{pr.number} {pr.title}
              </h3>

              <p className="text-sm text-gray-500">
                By {pr.author}
              </p>
            </Link>
          ))
        )}
      </div>
    </>
  );
}

export default RepositoryDetails;