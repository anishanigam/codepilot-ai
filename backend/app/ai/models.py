from dataclasses import dataclass, field


@dataclass
class GitHubFile:
    filename: str
    status: str
    patch: str | None
    additions: int
    deletions: int
    changes: int

@dataclass
class ReviewableFile:
    filename: str
    language: str
    status: str
    additions: int
    deletions: int
    changes: int
    chunks: list[str] = field(default_factory=list)


@dataclass
class SkippedFile:
    filename: str
    reason: str
    details: str | None = None


@dataclass
class ReviewStatistics:
    total_files: int
    reviewable_files: int
    skipped_files: int


@dataclass
class PreprocessorResult:
    reviewable_files: list[ReviewableFile]
    skipped_files: list[SkippedFile]
    statistics: ReviewStatistics

