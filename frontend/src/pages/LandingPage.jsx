function LandingPage() {
  const handleLogin = () => {
    window.location.href =
      "http://localhost:8000/api/auth/github/login";
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-6">

      <h1 className="text-5xl font-bold">
        CodePilot AI
      </h1>

      <p className="text-gray-500">
        Autonomous Multi-Agent Code Review Platform
      </p>

      <button
        onClick={handleLogin}
        className="rounded-lg bg-black px-6 py-3 text-white"
      >
        Continue with GitHub
      </button>

    </div>
  );
}

export default LandingPage;