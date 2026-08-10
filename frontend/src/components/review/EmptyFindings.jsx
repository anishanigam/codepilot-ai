import { PartyPopper } from "lucide-react";

function EmptyFindings() {
  return (
    <div className="rounded-2xl border bg-green-50 p-10 text-center shadow-sm">

      <PartyPopper
        size={50}
        className="mx-auto text-green-600"
      />

      <h2 className="mt-5 text-2xl font-bold text-green-700">
        No Issues Detected 🎉
      </h2>

      <p className="mt-3 text-gray-700">
        All reviewed files passed the AI review.
      </p>

      <p className="mt-2 text-gray-500">
        This pull request is ready to merge.
      </p>

    </div>
  );
}

export default EmptyFindings;