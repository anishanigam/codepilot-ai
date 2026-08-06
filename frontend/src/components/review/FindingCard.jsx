import {
  AlertTriangle,
  AlertCircle,
  Info,
  ShieldAlert,
} from "lucide-react";

function FindingCard({ finding }) {
  const severityConfig = {
    CRITICAL: {
      icon: <ShieldAlert size={20} />,
      classes: "bg-red-100 border-red-300 text-red-700",
    },
    HIGH: {
      icon: <AlertTriangle size={20} />,
      classes: "bg-orange-100 border-orange-300 text-orange-700",
    },
    MEDIUM: {
      icon: <AlertCircle size={20} />,
      classes: "bg-yellow-100 border-yellow-300 text-yellow-700",
    },
    LOW: {
      icon: <Info size={20} />,
      classes: "bg-blue-100 border-blue-300 text-blue-700",
    },
  };

  const severity =
    finding.finding.severity?.toUpperCase() || "LOW";

  const current =
    severityConfig[severity] || severityConfig.LOW;

  return (
    <div className="rounded-2xl border bg-white p-6 shadow-sm">

      <div className="flex items-center justify-between">

        <h3 className="text-lg font-semibold">
          {finding.finding.title}
        </h3>

        <span
          className={`rounded-full border px-3 py-1 text-sm font-medium ${current.classes}`}
        >
          <span className="flex items-center gap-2">
            {current.icon}
            {severity}
          </span>
        </span>

      </div>

      <p className="mt-4 text-gray-700">
        {finding.finding.description}
      </p>

      <div className="mt-5 rounded-lg bg-gray-50 p-4">

        <h4 className="font-semibold">
          💡 Suggested Fix
        </h4>

        <p className="mt-2 text-gray-700">
          {finding.finding.recommendation}
        </p>

      </div>

      <div className="mt-5 flex flex-wrap items-center justify-between gap-3">

        <div className="text-sm text-gray-500">
          Lines: {finding.finding.line_start} - {finding.finding.line_end}
        </div>

        <div className="flex flex-wrap gap-2">
          {finding.reported_by.map((agent) => (
            <span
              key={agent}
              className="rounded-full bg-indigo-100 px-3 py-1 text-xs font-medium text-indigo-700"
            >
              {agent}
            </span>
          ))}
        </div>

      </div>

    </div>
  );
}

export default FindingCard;