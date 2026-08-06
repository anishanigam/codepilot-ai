from app.ai.postprocessor.models import MergedFinding


class RecommendationEngine:

    def recommend(
        self,
        findings: list[MergedFinding],
    ):

        critical = 0
        high = 0
        medium = 0
        low = 0

        for finding in findings:

            severity = finding.severity.value

            if severity == "critical":
                critical += 1

            elif severity == "high":
                high += 1

            elif severity == "medium":
                medium += 1

            else:
                low += 1

        # -----------------------------------
        # Request Changes
        # -----------------------------------

        if critical > 0:

            return {
                "recommendation": "REQUEST_CHANGES",
                "overall_risk": "HIGH",
                "reason": f"{critical} critical issue(s) detected.",
                "blocking_issues": critical + high,
                "suggestions": medium + low,
            }

        if high >= 3:

            return {
                "recommendation": "REQUEST_CHANGES",
                "overall_risk": "HIGH",
                "reason": f"{high} high severity issues detected.",
                "blocking_issues": high,
                "suggestions": medium + low,
            }

        # -----------------------------------
        # Merge After Fixes
        # -----------------------------------

        if high > 0:

            return {
                "recommendation": "MERGE_AFTER_FIXES",
                "overall_risk": "MEDIUM",
                "reason": f"{high} high severity issue(s) should be fixed before merging.",
                "blocking_issues": high,
                "suggestions": medium + low,
            }

        if medium >= 5:

            return {
                "recommendation": "MERGE_AFTER_FIXES",
                "overall_risk": "MEDIUM",
                "reason": f"{medium} medium severity issues detected.",
                "blocking_issues": 0,
                "suggestions": medium + low,
            }

        # -----------------------------------
        # Approve
        # -----------------------------------

        return {
            "recommendation": "APPROVE",
            "overall_risk": "LOW",
            "reason": "No blocking issues were detected.",
            "blocking_issues": 0,
            "suggestions": medium + low,
        }


recommendation_engine = RecommendationEngine()