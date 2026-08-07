import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

import ReviewHero from "../components/review/ReviewHero";
import ExecutiveSummaryCard from "../components/review/ExecutiveSummaryCard";
import DecisionCard from "../components/review/DecisionCard";
import ModulesCard from "../components/review/ModulesCard";
import StatisticsCard from "../components/review/StatisticsCards";
import FindingsList from "../components/review/FindingsList";
import EmptyFindings from "../components/review/EmptyFindings";

import { reviewPullRequest } from "../services/reviewService";
import ReviewLoading from "../components/review/ReviewLoading";

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

  const {
  owner,
  repo,
  pullNumber,
  pr,
} = state;

const [review, setReview] = useState(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);

useEffect(() => {
  async function loadReview() {
    try {
      const result = await reviewPullRequest(
        owner,
        repo,
        pullNumber
      );

      setReview(result);
    } catch (err) {
      console.error(err);
      setError("Failed to generate AI review.");
    } finally {
      setLoading(false);
    }
  }

  loadReview();
}, [owner, repo, pullNumber]);

if (loading) {
  return <ReviewLoading />;
}

if (error) {
  return (
    <div className="p-8 text-center">
      <h2 className="text-2xl font-bold text-red-600">
        {error}
      </h2>

      <button
        onClick={() => navigate(-1)}
        className="mt-5 rounded-lg bg-black px-5 py-2 text-white"
      >
        Go Back
      </button>
    </div>
  );
}

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
