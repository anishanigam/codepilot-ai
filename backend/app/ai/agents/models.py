from dataclasses import dataclass, field
from enum import Enum
from app.ai.planner.models import AgentType

class Severity(str, Enum):

    CRITICAL = "critical"

    HIGH = "high"

    MEDIUM = "medium"

    LOW = "low"

    INFO = "info"


@dataclass(slots=True)
class ReviewFinding:

    title: str

    description: str

    severity: Severity

    recommendation: str

    line_start: int | None = None

    line_end: int | None = None


@dataclass(slots=True)
class AgentResult:
    
    agent: AgentType
    
    success: bool

    findings: list[ReviewFinding] = field(default_factory=list)

    error: str | None = None