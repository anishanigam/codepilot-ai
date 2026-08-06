import { useLocation, useNavigate } from "react-router-dom";

import ReviewHero from "../components/review/ReviewHero";
import ExecutiveSummaryCard from "../components/review/ExecutiveSummaryCard";
import DecisionCard from "../components/review/DecisionCard";
import ModulesCard from "../components/review/ModulesCard";
import StatisticsCard from "../components/review/StatisticsCards";
import FindingsList from "../components/review/FindingsList";
import EmptyFindings from "../components/review/EmptyFindings";

function Review() {
  const { state } = useLocation();
  const navigate = useNavigate();

  if (!state) {
    return (
      <div className="p-8">
        <h2 className="text-2xl font-bold">No review found.</h2>

        <button
          onClick={() => navigate(-1)}
          className="mt-4 rounded-lg bg-black px-4 py-2 text-white"
        >
          Go Back
        </button>
      </div>
    );
  }

  const { review, pr } = state;

  return (
    <div className="mx-auto max-w-7xl space-y-8 px-4 py-8">
      <ReviewHero pr={pr} />

      <ExecutiveSummaryCard summary={review.summary} />

      <DecisionCard summary={review.summary} />

      <ModulesCard modules={review.summary.modules_changed} />

      <StatisticsCard
        statistics={review.statistics}
        findings={review.merged_findings}
      />

      {review.merged_findings.length === 0 ? (
        <EmptyFindings />
      ) : (
        <FindingsList findings={review.merged_findings} />
      )}
    </div>
  );
}

export default Review;
