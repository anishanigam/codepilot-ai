from app.ai.postprocessor.models import (
    MergedFinding,
    ReviewSummary,
)


class SummaryGenerator:

    def generate(
        self,
        findings: list[MergedFinding],
    ) -> ReviewSummary:

        critical = 0
        high = 0
        medium = 0
        low = 0

        concerns = []

        for item in findings:

            severity = item.finding.severity.value

            if severity == "critical":
                critical += 1

            elif severity == "high":
                high += 1

            elif severity == "medium":
                medium += 1

            else:
                low += 1

            concerns.append(item.finding.title)

        if critical:
            risk = "CRITICAL"

        elif high:
            risk = "HIGH"

        elif medium:
            risk = "MEDIUM"

        else:
            risk = "LOW"

        return ReviewSummary(
            overall_risk=risk,
            total_findings=len(findings),
            critical=critical,
            high=high,
            medium=medium,
            low=low,
            top_concerns=concerns[:5],
        )


summary_generator = SummaryGenerator()