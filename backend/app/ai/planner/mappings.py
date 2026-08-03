from app.ai.planner.models import (
    AgentType,
    ConceptType,
)

# ==========================================================
# Concept Detection Keywords
# ==========================================================

CONCEPT_KEYWORDS = {

    ConceptType.AUTHENTICATION: {
        "jwt",
        "token",
        "access_token",
        "refresh_token",
        "oauth",
        "login",
        "logout",
        "password",
        "bcrypt",
        "hash",
        "verify",
        "authenticate",
        "authorization",
        "cookie",
        "session",
    },

    ConceptType.DATABASE: {
        "select",
        "insert",
        "update",
        "delete",
        "cursor",
        "query",
        "execute",
        "commit",
        "rollback",
        "mongodb",
        "mongoose",
        "sql",
        "postgres",
        "mysql",
        "find_one",
        "find",
    },

    ConceptType.NETWORKING: {
        "requests",
        "httpx",
        "axios",
        "fetch",
        "socket",
        "websocket",
        "api",
        "post",
        "get",
        "put",
        "delete",
        "response",
        "request",
    },

    ConceptType.FILESYSTEM: {
        "open",
        "write",
        "read",
        "remove",
        "mkdir",
        "path",
        "pathlib",
        "os.path",
        "shutil",
    },

    ConceptType.CONCURRENCY: {
        "async",
        "await",
        "thread",
        "lock",
        "mutex",
        "parallel",
        "multiprocessing",
        "queue",
    },

    ConceptType.CRYPTOGRAPHY: {
        "encrypt",
        "decrypt",
        "aes",
        "rsa",
        "sha256",
        "md5",
        "cipher",
        "crypto",
        "secret",
        "key",
    },

    ConceptType.API: {
        "router",
        "endpoint",
        "route",
        "fastapi",
        "express",
        "flask",
        "request",
        "response",
        "status_code",
    },

    ConceptType.VALIDATION: {
        "validate",
        "validator",
        "schema",
        "required",
        "regex",
        "pydantic",
        "zod",
        "joi",
    },

    ConceptType.ERROR_HANDLING: {
        "try",
        "except",
        "catch",
        "finally",
        "raise",
        "throw",
        "error",
        "exception",
    },

    ConceptType.PERFORMANCE: {
        "cache",
        "memo",
        "sort",
        "loop",
        "for",
        "while",
        "recursion",
        "iterate",
        "optimization",
    },
}

# ==========================================================
# Concept → Agent Mapping
# ==========================================================

CONCEPT_TO_AGENTS = {

    ConceptType.AUTHENTICATION: [
        AgentType.SECURITY,
        AgentType.BUG,
        AgentType.BEST_PRACTICES,
    ],

    ConceptType.DATABASE: [
        AgentType.SECURITY,
        AgentType.BUG,
        AgentType.PERFORMANCE,
    ],

    ConceptType.NETWORKING: [
        AgentType.BUG,
        AgentType.PERFORMANCE,
    ],

    ConceptType.FILESYSTEM: [
        AgentType.BUG,
        AgentType.BEST_PRACTICES,
    ],

    ConceptType.CONCURRENCY: [
        AgentType.BUG,
        AgentType.PERFORMANCE,
    ],

    ConceptType.CRYPTOGRAPHY: [
        AgentType.SECURITY,
        AgentType.BEST_PRACTICES,
    ],

    ConceptType.API: [
        AgentType.BUG,
        AgentType.BEST_PRACTICES,
    ],

    ConceptType.VALIDATION: [
        AgentType.SECURITY,
        AgentType.BUG,
    ],

    ConceptType.ERROR_HANDLING: [
        AgentType.BUG,
        AgentType.BEST_PRACTICES,
    ],

    ConceptType.PERFORMANCE: [
        AgentType.PERFORMANCE,
        AgentType.BEST_PRACTICES,
    ],
}

# ==========================================================
# Default Agents
# (Fallback if LLM fails)
# ==========================================================

DEFAULT_AGENTS = {

    "python": [
        AgentType.BUG,
        AgentType.BEST_PRACTICES,
    ],

    "javascript": [
        AgentType.BUG,
        AgentType.BEST_PRACTICES,
    ],

    "typescript": [
        AgentType.BUG,
        AgentType.BEST_PRACTICES,
    ],

    "java": [
        AgentType.BUG,
        AgentType.PERFORMANCE,
    ],

    "cpp": [
        AgentType.BUG,
        AgentType.PERFORMANCE,
    ],

    "go": [
        AgentType.BUG,
        AgentType.PERFORMANCE,
    ],
}

# ==========================================================
# Confidence Threshold
# ==========================================================

CONFIDENCE_THRESHOLD = 0.75