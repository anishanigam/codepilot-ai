from dataclasses import dataclass, field
from enum import Enum


# ==========================================================
# Agent Types
# ==========================================================

class AgentType(str, Enum):
    BUG = "bug"
    SECURITY = "security"
    PERFORMANCE = "performance"
    STYLE = "style"
    BEST_PRACTICES = "best_practices"


# ==========================================================
# Code Concepts
# ==========================================================

class ConceptType(str, Enum):
    AUTHENTICATION = "authentication"
    DATABASE = "database"
    NETWORKING = "networking"
    FILESYSTEM = "filesystem"
    CONCURRENCY = "concurrency"
    CRYPTOGRAPHY = "cryptography"
    API = "api"
    VALIDATION = "validation"
    ERROR_HANDLING = "error_handling"
    PERFORMANCE = "performance"


# ==========================================================
# Evidence
# ==========================================================

@dataclass(slots=True)
class Evidence:
    keyword: str
    line_number: int


# ==========================================================
# Keyword Rule
# ==========================================================

@dataclass(frozen=True, slots=True)
class KeywordRule:

    keyword: str

    weight: float = 1.0


# ==========================================================
# Planner Input
# ==========================================================

@dataclass(slots=True)
class PlannerInput:

    filename: str

    language: str

    git_status: str

    chunk_id: str

    chunk_number: int

    total_chunks: int

    content: str


# ==========================================================
# Detected Concept
# ==========================================================

@dataclass(slots=True)
class DetectedConcept:

    concept: ConceptType

    confidence: float

    match_count: int

    evidence: list[Evidence] = field(default_factory=list)

    


# ==========================================================
# Review Task
# ==========================================================

@dataclass(slots=True)
class ReviewTask:

    task_id: str

    planner_input: PlannerInput

    agent: AgentType

    concepts: list[DetectedConcept]

    routing_reason: str

    source: str

@dataclass(slots=True)
class RuleEngineResult:

    use_llm: bool

    agents: list[AgentType]

    reason: str    


@dataclass(slots=True)
class LLMRoutingResult:
    success: bool
    agents: list[AgentType]

    reason: str
