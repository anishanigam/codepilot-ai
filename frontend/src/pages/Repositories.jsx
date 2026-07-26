import { useQuery } from "@tanstack/react-query";
import api from "../services/api";
import { Link } from "react-router-dom";

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

  if (isLoading) {
    return <h2>Loading repositories...</h2>;
  }

  if (isError) {
    return <h2>Failed to load repositories.</h2>;
  }

  return (
    <>
      <h2 className="mb-6 text-3xl font-bold">
        Your Repositories
      </h2>

      <div className="grid gap-4">
        {repositories.map((repo) => (
          <Link
  key={repo.id}
  to={`/repositories/${repo.owner.login}/${repo.name}`}
  className="block rounded-lg border bg-white p-4 shadow-sm transition hover:shadow-md"
>
  <h3 className="text-xl font-semibold">
    {repo.name}
  </h3>

  <p className="text-gray-500">
    {repo.full_name}
  </p>

  <p className="mt-2 text-sm">
    {repo.private ? "🔒 Private" : "🌍 Public"}
  </p>
</Link>
        ))}
      </div>
    </>
  );
}

export default Repositories;