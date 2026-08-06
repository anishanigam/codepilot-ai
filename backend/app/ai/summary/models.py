from dataclasses import dataclass


@dataclass(slots=True)
class ExecutiveSummary:

    pr_summary: str

    modules_changed: list[str]

    executive_summary: str

    overall_risk: str

    merge_recommendation: str

    reason: str

    blocking_issues: int

    suggestions: int