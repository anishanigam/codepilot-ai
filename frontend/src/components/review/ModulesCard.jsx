import { Layers } from "lucide-react";

function ModulesCard({ modules }) {
  const moduleColors = {
    Authentication: "bg-blue-100 text-blue-700 border-blue-200",

    API: "bg-purple-100 text-purple-700 border-purple-200",

    Database: "bg-green-100 text-green-700 border-green-200",

    Documentation: "bg-orange-100 text-orange-700 border-orange-200",

    Performance: "bg-red-100 text-red-700 border-red-200",

    UI: "bg-pink-100 text-pink-700 border-pink-200",

    Security: "bg-yellow-100 text-yellow-700 border-yellow-200",
  };

  const moduleIcons = {
    Authentication: "🔐",
    API: "🌐",
    Database: "🗄",
    Documentation: "📄",
    Performance: "⚡",
    UI: "🎨",
    Security: "🛡",
  };

  return (
    <div className="rounded-2xl border bg-white p-6 shadow-sm">
      <div className="mb-5 flex items-center gap-3">
        <Layers className="text-indigo-600" size={24} />

        <h2 className="text-2xl font-bold">Modules Changed</h2>
      </div>

      {modules.length === 0 ? (
        <p className="text-gray-500">No modules detected.</p>
      ) : (
        <div className="flex flex-wrap gap-3">
          {modules.map((module) => (
            <span
              key={module}
              className={`rounded-full border px-4 py-2 text-sm font-medium ${
                moduleColors[module] ||
                "bg-gray-100 text-gray-700 border-gray-200"
              }`}
            >
              {moduleIcons[module]} {module}
            </span>
          ))}
        </div>
      )}
    </div>
  );
}

export default ModulesCard;
