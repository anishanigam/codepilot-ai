import { FileText } from "lucide-react";

function ExecutiveSummaryCard({ summary }) {
  return (
    <div className="rounded-2xl border bg-white p-8 shadow-sm">

      <div className="mb-6 flex items-center gap-3">
        <FileText className="text-blue-600" size={24} />

        <h2 className="text-2xl font-bold">
          Executive Summary
        </h2>
      </div>

      <p className="text-lg leading-8 text-gray-700">
        {summary.pr_summary}
      </p>

      <div className="mt-6 rounded-xl bg-blue-50 p-5 border border-blue-100">

        <h3 className="mb-2 font-semibold text-blue-900">
          AI Overview
        </h3>

        <p className="text-blue-800">
          {summary.executive_summary}
        </p>

      </div>

    </div>
  );
}

export default ExecutiveSummaryCard;