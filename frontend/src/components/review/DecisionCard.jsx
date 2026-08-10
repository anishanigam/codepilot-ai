import {
  CheckCircle,
  AlertTriangle,
  XCircle,
} from "lucide-react";

function DecisionCard({ summary }) {
  const config = {
    APPROVE: {
      icon: <CheckCircle size={30} />,
      title: "Ready to Merge",
      badge: "APPROVE",
      classes:
        "border-green-200 bg-green-50 text-green-700",
    },

    MERGE_AFTER_FIXES: {
      icon: <AlertTriangle size={30} />,
      title: "Merge After Fixes",
      badge: "MERGE AFTER FIXES",
      classes:
        "border-yellow-200 bg-yellow-50 text-yellow-700",
    },

    REQUEST_CHANGES: {
      icon: <XCircle size={30} />,
      title: "Request Changes",
      badge: "REQUEST CHANGES",
      classes:
        "border-red-200 bg-red-50 text-red-700",
    },
  };

  const current =
    config[summary.merge_recommendation];

  return (
    <div
      className={`rounded-2xl border p-6 shadow-sm ${current.classes}`}
    >
      <div className="flex items-center gap-3">
        {current.icon}

        <div>
          <h2 className="text-xl font-bold">
            {current.title}
          </h2>

          <span className="text-sm font-semibold">
            {current.badge}
          </span>
        </div>
      </div>

      <div className="mt-6">
        <h3 className="font-semibold">
          Risk Level
        </h3>

        <p className="mt-1 text-lg">
          {summary.overall_risk}
        </p>
      </div>

      <div className="mt-6">
        <h3 className="font-semibold">
          Reason
        </h3>

        <p className="mt-2">
          {summary.reason}
        </p>
      </div>
    </div>
  );
}

export default DecisionCard;