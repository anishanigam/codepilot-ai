import FindingCard from "./FindingCard";

function FindingsList({ findings }) {
  return (
    <div>

      <h2 className="mb-6 text-2xl font-bold">
        🐞 Review Findings
      </h2>

      <div className="space-y-6">
        {findings.map((finding, index) => (
          <FindingCard
            key={index}
            finding={finding}
          />
        ))}
      </div>

    </div>
  );
}

export default FindingsList;