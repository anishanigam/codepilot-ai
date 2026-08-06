import json
import re

from app.ai.summary.models import ExecutiveSummary


class SummaryParser:

    def parse(
        self,
        response: str,
    ) -> ExecutiveSummary:

        response = response.strip()

        # Remove markdown code fences if present
        response = response.replace("```json", "").replace("```", "").strip()

        # Extract the first JSON object
        match = re.search(r"\{.*\}", response, re.DOTALL)

        if not match:
            raise ValueError(
                f"No JSON found in response:\n{response}"
            )

        data = json.loads(match.group())

        return ExecutiveSummary(
            pr_summary=data.get("pr_summary", ""),
            executive_summary=data.get("executive_summary", ""),
            modules_changed=data.get("modules_changed", []),
            overall_risk=data.get("overall_risk", "LOW"),
            merge_recommendation=data.get("merge_recommendation", "APPROVE"),
            reason=data.get("reason", ""),
            blocking_issues=data.get("blocking_issues", 0),
            suggestions=data.get("suggestions", 0),
        )


summary_parser = SummaryParser()