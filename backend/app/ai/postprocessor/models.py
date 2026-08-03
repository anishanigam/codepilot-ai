from dataclasses import dataclass, field

from app.ai.agents.models import (
    ReviewFinding,
)

from app.ai.common.enums import AgentType


@dataclass(slots=True)
class MergedFinding:

    finding: ReviewFinding

    reported_by: list[AgentType] = field(
        default_factory=list
    )

@dataclass(slots=True)
class TopConcern:
    title: str
    severity: str
    reported_by: list[AgentType]


@dataclass(slots=True)
class ReviewSummary:

    overall_risk: str

    total_findings: int

    critical: int

    high: int

    medium: int

    low: int

    top_concerns: list[TopConcern]