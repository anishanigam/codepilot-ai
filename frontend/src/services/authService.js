const API_URL = "http://localhost:8000";

export function login() {
    window.location.href =
        `${API_URL}/api/auth/github/login`;
}

export function enablePrivateRepos() {
    window.location.href =
        `${API_URL}/api/auth/github/login/private`;
}