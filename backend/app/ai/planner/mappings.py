from app.ai.planner.models import (
    AgentType,
    ConceptType,
    KeywordRule,
)

MAX_CONCEPT_WEIGHT = 1.0
# ==========================================================
# Concept Detection Keywords
# ==========================================================

CONCEPT_KEYWORDS = {

    ConceptType.AUTHENTICATION: [

    KeywordRule(
        keyword="jwt",
        weight=1.0,
    ),

    KeywordRule(
        keyword="oauth",
        weight=1.0,
    ),

    KeywordRule(
        keyword="access_token",
        weight=0.9,
    ),

    KeywordRule(
        keyword="refresh_token",
        weight=0.9,
    ),

    KeywordRule(
        keyword="bcrypt",
        weight=0.9,
    ),

    KeywordRule(
        keyword="authenticate",
        weight=0.8,
    ),

    KeywordRule(
        keyword="authorization",
        weight=0.8,
    ),

    KeywordRule(
        keyword="verify",
        weight=0.7,
    ),

    KeywordRule(
        keyword="password",
        weight=0.7,
    ),

    KeywordRule(
        keyword="hash",
        weight=0.6,
    ),

    KeywordRule(
        keyword="token",
        weight=0.5,
    ),

    KeywordRule(
        keyword="cookie",
        weight=0.4,
    ),

    KeywordRule(
        keyword="session",
        weight=0.4,
    ),

    KeywordRule(
        keyword="login",
        weight=0.3,
    ),

    KeywordRule(
        keyword="logout",
        weight=0.3,
    ),
],

    ConceptType.DATABASE: [

    # Very strong indicators
    KeywordRule("sql", 1.0),
    KeywordRule("mongodb", 1.0),
    KeywordRule("postgres", 1.0),
    KeywordRule("mysql", 1.0),

    # Strong indicators
    KeywordRule("query", 0.9),
    KeywordRule("execute", 0.9),
    KeywordRule("cursor", 0.9),
    KeywordRule("commit", 0.9),
    KeywordRule("rollback", 0.9),

    # Medium indicators
    KeywordRule("insert", 0.8),
    KeywordRule("update", 0.8),
    KeywordRule("delete", 0.8),
    KeywordRule("find_one", 0.8),

    # ORM-specific
    KeywordRule("mongoose", 0.7),

    # Weak indicators
    KeywordRule("find", 0.4),
    KeywordRule("select", 0.4),
],

    ConceptType.NETWORKING: [

    # Strong indicators
    KeywordRule("httpx", 1.0),
    KeywordRule("requests", 1.0),
    KeywordRule("axios", 1.0),
    KeywordRule("websocket", 1.0),
    KeywordRule("socket", 1.0),

    # Medium indicators
    KeywordRule("fetch", 0.8),

    # Weak indicators
    KeywordRule("api", 0.3),
    KeywordRule("post", 0.2),
    KeywordRule("get", 0.2),
    KeywordRule("put", 0.2),
    KeywordRule("delete", 0.2),
],

    ConceptType.FILESYSTEM: [

    # Very strong
    KeywordRule("pathlib", 1.0),
    KeywordRule("shutil", 1.0),

    # Strong
    KeywordRule("mkdir", 0.9),
    KeywordRule("remove", 0.9),

    # Medium
    KeywordRule("open", 0.8),
    KeywordRule("write", 0.8),
    KeywordRule("read", 0.8),

    # Weak
    KeywordRule("os.path", 0.6),
    KeywordRule("path", 0.3),
],

    ConceptType.CONCURRENCY: [

    # Very strong
    KeywordRule("lock", 1.0),
    KeywordRule("mutex", 1.0),
    KeywordRule("semaphore", 1.0),
    KeywordRule("asyncio.gather", 1.0),

    # Strong
    KeywordRule("thread", 0.9),
    KeywordRule("multiprocessing", 0.9),
    KeywordRule("parallel", 0.8),

    # Medium
    KeywordRule("queue", 0.6),

    # Weak
    KeywordRule("await", 0.4),
    KeywordRule("async", 0.2),
],

    ConceptType.CRYPTOGRAPHY: [

    # Very strong
    KeywordRule("aes", 1.0),
    KeywordRule("rsa", 1.0),
    KeywordRule("md5", 1.0),

    # Strong
    KeywordRule("encrypt", 0.9),
    KeywordRule("decrypt", 0.9),

    # Medium
    KeywordRule("sha256", 0.8),
    KeywordRule("cipher", 0.8),

    # Weak
    KeywordRule("crypto", 0.6),
    KeywordRule("secret", 0.4),
    KeywordRule("key", 0.3),
],

    ConceptType.API: [

    # Very strong
    KeywordRule("fastapi", 1.0),
    KeywordRule("flask", 1.0),
    KeywordRule("express", 1.0),

    # Strong
    KeywordRule("endpoint", 0.9),
    KeywordRule("route", 0.8),

    # Medium
    KeywordRule("router", 0.6),
    KeywordRule("status_code", 0.6),

    # Weak
    KeywordRule("request", 0.2),
    KeywordRule("response", 0.2),
],

    ConceptType.VALIDATION: [

    # Very strong
    KeywordRule("pydantic", 1.0),
    KeywordRule("zod", 1.0),
    KeywordRule("joi", 1.0),

    # Strong
    KeywordRule("validator", 0.9),
    KeywordRule("validate", 0.8),
    KeywordRule("schema", 0.8),

    # Medium
    KeywordRule("regex", 0.6),

    # Weak
    KeywordRule("required", 0.3),
],

    ConceptType.ERROR_HANDLING: [

    # Strong
    KeywordRule("try", 0.9),
    KeywordRule("except", 0.9),
    KeywordRule("catch", 0.9),

    KeywordRule("raise", 0.8),
    KeywordRule("throw", 0.8),

    # Medium
    KeywordRule("finally", 0.6),

    # Weak
    KeywordRule("exception", 0.4),
    KeywordRule("error", 0.2),
],

    ConceptType.PERFORMANCE: [

    # Very strong
    KeywordRule("cache", 1.0),
    KeywordRule("memo", 1.0),

    # Strong
    KeywordRule("optimization", 0.9),

    # Medium
    KeywordRule("recursion", 0.8),
    KeywordRule("sort", 0.6),

    # Weak
    KeywordRule("iterate", 0.3),
    KeywordRule("loop", 0.2),
],
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