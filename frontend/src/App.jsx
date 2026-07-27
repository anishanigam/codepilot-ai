import { Route, Routes } from "react-router-dom";

import LandingPage from "./pages/LandingPage";
import Dashboard from "./pages/Dashboard";
import PullRequestDetails from "./pages/PullRequestDetails";
import DashboardLayout from "./layouts/DashboardLayout";
import ProtectedRoute from "./components/ProtectedRoute";
import Repositories from "./pages/Repositories";
import RepositoryDetails from "./pages/RepositoryDetails";

function App() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />

      <Route
        element={
          <ProtectedRoute>
            <DashboardLayout />
          </ProtectedRoute>
        }
      >
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/repositories" element={<Repositories />} />
        <Route path="/repositories/:owner/:repo" element={<RepositoryDetails />}/>
        <Route
          path="/repositories/:owner/:repo/pulls/:pullNumber"
          element={<PullRequestDetails />}
        />
      </Route>
    </Routes>
  );
}

export default App;