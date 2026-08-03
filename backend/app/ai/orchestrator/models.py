from dataclasses import dataclass, field

from app.ai.agents.models import AgentResult


@dataclass(slots=True)
class OrchestratorResult:

    success: bool

    results: list[AgentResult] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)