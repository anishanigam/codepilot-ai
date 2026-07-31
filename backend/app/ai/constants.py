from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".py": "python",
    ".js": "javascript",
    ".jsx": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".java": "java",
    ".cpp": "cpp",
    ".c": "c",
    ".cs": "csharp",
    ".go": "go",
    ".rs": "rust",
    ".php": "php",
    ".rb": "ruby",
    ".swift": "swift",
    ".kt": "kotlin",
    ".html": "html",
    ".css": "css",
    ".scss": "scss",
    ".sql": "sql",
    ".json": "json",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".sh": "shell",
    ".md": "markdown",
}

IGNORED_FILENAMES = {
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
}

IGNORED_DIRECTORIES = {
    "node_modules",
    "dist",
    "build",
    ".next",
    "coverage",
}

MAX_PATCH_LINES = 300
CHUNK_OVERLAP = 40
BOUNDARY_SEARCH_WINDOW = 50


def get_extension(filename: str):
    return Path(filename).suffix.lower()