import {
  FileCode,
  CheckCircle2,
  SkipForward,
  Bug,
} from "lucide-react";

function StatisticsCard({ statistics, findings }) {
  const cards = [
    {
      title: "Files",
      value: statistics.total_files,
      icon: <FileCode size={26} />,
      color:
        "bg-blue-50 border-blue-200 text-blue-700",
    },

    {
      title: "Reviewed",
      value: statistics.reviewable_files,
      icon: <CheckCircle2 size={26} />,
      color:
        "bg-green-50 border-green-200 text-green-700",
    },

    {
      title: "Skipped",
      value: statistics.skipped_files,
      icon: <SkipForward size={26} />,
      color:
        "bg-yellow-50 border-yellow-200 text-yellow-700",
    },

    {
      title: "Findings",
      value: findings.length,
      icon: <Bug size={26} />,
      color:
        findings.length === 0
          ? "bg-emerald-50 border-emerald-200 text-emerald-700"
          : "bg-red-50 border-red-200 text-red-700",
    },
  ];

  return (
    <div>
      <h2 className="mb-5 text-2xl font-bold">
        📊 Review Statistics
      </h2>

      <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">

        {cards.map((card) => (

          <div
            key={card.title}
            className={`rounded-2xl border p-6 shadow-sm transition hover:shadow-md ${card.color}`}
          >
            <div className="flex items-center justify-between">

              <div>

                <p className="text-sm font-medium">
                  {card.title}
                </p>

                <h3 className="mt-3 text-4xl font-bold">
                  {card.value}
                </h3>

              </div>

              {card.icon}

            </div>
          </div>

        ))}

      </div>
    </div>
  );
}

export default StatisticsCard;