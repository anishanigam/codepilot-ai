import { NavLink, Outlet } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";

function DashboardLayout() {
  const { user } = useAuth();

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="flex items-center justify-between border-b bg-white px-8 py-4 shadow-sm">
        {/* Logo */}
        <h1 className="text-2xl font-bold">CodePilot AI</h1>

        {/* Navigation */}
        <nav className="flex items-center gap-6">
          <NavLink
            to="/dashboard"
            className={({ isActive }) =>
              isActive ? "font-semibold text-blue-600" : "text-gray-600 hover:text-black"
            }
          >
            Dashboard
          </NavLink>

          <NavLink
            to="/repositories"
            className={({ isActive }) =>
              isActive ? "font-semibold text-blue-600" : "text-gray-600 hover:text-black"
            }
          >
            Repositories
          </NavLink>
        </nav>

        {/* User Info */}
        <div className="flex items-center gap-3">
          <img
            src={user.avatar_url}
            alt={user.username}
            className="h-10 w-10 rounded-full"
          />

          <div>
            <p className="font-medium">{user.name}</p>
            <p className="text-sm text-gray-500">@{user.username}</p>
          </div>
        </div>
      </header>

      {/* Page Content */}
      <main className="p-8">
        <Outlet />
      </main>
    </div>
  );
}

export default DashboardLayout;