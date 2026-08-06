import json

from app.ai.summary.models import ExecutiveSummary


class SummaryParser:

    def parse(
        self,
        response: str,
    ) -> ExecutiveSummary:

        data = json.loads(response)

        return ExecutiveSummary(
            pr_summary=data["pr_summary"],
            modules_changed=data["modules_changed"],
            overall_risk=data["overall_risk"],
            merge_recommendation=data["merge_recommendation"],
            reason=data["reason"],
            blocking_issues=data["blocking_issues"],
            suggestions=data["suggestions"],
        )


summary_parser = SummaryParser()