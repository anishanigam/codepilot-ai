import { Link } from "react-router-dom";

function Dashboard() {
  return (
    <>
      <h2 className="text-3xl font-bold">
        Welcome to CodePilot AI
      </h2>

      <p className="mt-2 text-gray-600">
        Start by exploring your GitHub repositories.
      </p>

      <Link
        to="/repositories"
        className="mt-6 inline-block rounded-lg bg-black px-6 py-3 text-white"
      >
        View Repositories
      </Link>
    </>
  );
}

export default Dashboard;