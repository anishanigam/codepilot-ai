from dataclasses import dataclass, field

from app.ai.models import (
    ReviewStatistics,
    SkippedFile,
)

from app.ai.orchestrator.models import (
    OrchestratorResult,
)

from app.ai.postprocessor.models import (
    MergedFinding,
)

from app.ai.postprocessor.models import (
    MergedFinding,
    ReviewSummary,
)


@dataclass(slots=True)
class ReviewResult:

    statistics: ReviewStatistics

    skipped_files: list[SkippedFile] = field(
        default_factory=list
    )

    summary: ReviewSummary | None = None

    merged_findings: list[MergedFinding] = field(
        default_factory=list
    )

    errors: list[str] = field(
        default_factory=list
    )