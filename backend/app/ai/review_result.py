from dataclasses import dataclass, field

from app.ai.models import (
    ReviewStatistics,
    SkippedFile,
)

from app.ai.postprocessor.models import (
    MergedFinding,
)

from app.ai.summary.models import (
    ExecutiveSummary,
)


@dataclass(slots=True)
class ReviewResult:

    statistics: ReviewStatistics

    skipped_files: list[SkippedFile] = field(
        default_factory=list
    )

    summary: ExecutiveSummary | None = None

    merged_findings: list[MergedFinding] = field(
        default_factory=list
    )

    errors: list[str] = field(
        default_factory=list
    )