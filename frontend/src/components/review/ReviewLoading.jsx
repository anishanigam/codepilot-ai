function ReviewLoading() {
  const steps = [
    "Preprocessing Pull Request...",
    "Planning AI Review...",
    "Running Security Agent...",
    "Running Bug Detection Agent...",
    "Running Best Practices Agent...",
    "Aggregating Findings...",
    "Generating Executive Summary...",
  ];

  return (
    <div className="mt-8 rounded-xl border bg-white p-6 shadow-sm">
      <h2 className="mb-6 text-2xl font-bold">
        🤖 AI Review in Progress
      </h2>

      <div className="space-y-4">
        {steps.map((step) => (
          <div
            key={step}
            className="flex items-center gap-3"
          >
            <div className="h-3 w-3 animate-pulse rounded-full bg-blue-600"></div>

            <span>{step}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ReviewLoading;