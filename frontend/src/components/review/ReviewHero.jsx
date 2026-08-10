import { ArrowLeft, GitPullRequest, Sparkles } from "lucide-react";
import { useNavigate } from "react-router-dom";

function ReviewHero({ pr }) {
  const navigate = useNavigate();

  return (
    <div className="space-y-6">
      {/* Back Button */}
      <button
        onClick={() => navigate(-1)}
        className="flex items-center gap-2 rounded-lg border px-4 py-2 text-sm font-medium transition hover:bg-gray-100"
      >
        <ArrowLeft size={18} />
        Back to Pull Request
      </button>

      {/* Hero Card */}
      <div className="rounded-2xl border bg-white p-8 shadow-sm">
        <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">
          {/* Left */}
          <div>
            <div className="mb-3 flex items-center gap-3">
              <Sparkles className="text-blue-600" size={28} />

              <h1 className="text-4xl font-bold">AI Review Dashboard</h1>
            </div>

            <p className="text-gray-500">
              Intelligent pull request analysis powered by multiple AI review
              agents.
            </p>

            <div className="mt-6 flex flex-wrap items-center gap-3">
              <span className="rounded-full bg-blue-100 px-3 py-1 text-sm font-medium text-blue-700">
                <GitPullRequest className="mr-1 inline" size={14} />
                PR #{pr.number}
              </span>

              <span className="rounded-full bg-gray-100 px-3 py-1 text-sm text-gray-700">
                {pr.state.toUpperCase()}
              </span>
            </div>
          </div>

          {/* Right */}
          <div className="max-w-lg">
            <h2 className="text-xl font-semibold">{pr.title}</h2>

            <div className="mt-6">
              <p className="mb-3 text-sm font-semibold uppercase tracking-wide text-gray-500">
                AI Agents Used
              </p>

              <div className="flex flex-wrap gap-3">
                <span className="rounded-full bg-red-100 px-3 py-1 text-sm font-medium text-red-700">
                  🐞 Bug
                </span>

                <span className="rounded-full bg-blue-100 px-3 py-1 text-sm font-medium text-blue-700">
                  🔒 Security
                </span>

                <span className="rounded-full bg-purple-100 px-3 py-1 text-sm font-medium text-purple-700">
                  📖 Best Practices
                </span>

                <span className="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-700">
                  ⚡ Planner
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ReviewHero;
