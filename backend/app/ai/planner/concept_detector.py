from app.ai.planner.models import (
    PlannerInput,
    DetectedConcept,
    Evidence,
    KeywordRule,
)

from app.ai.planner.mappings import (
    CONCEPT_KEYWORDS,
    MAX_CONCEPT_WEIGHT,
)

import re


class ConceptDetector:

    def detect(
        self,
        planner_input: PlannerInput,
    ) -> list[DetectedConcept]:
        """
        Detect high-level programming concepts
        present inside a code chunk.
        """

        detected: list[DetectedConcept] = []

        lines = planner_input.content.splitlines()

        lower_lines = [
            line.lower()
            for line in lines
        ]

        for concept, keywords in CONCEPT_KEYWORDS.items():

            evidence, total_weight = self._build_evidence(
                lower_lines,
                keywords,
            )

            if not evidence:
                continue

            confidence = self._calculate_confidence(
                total_weight,
            )

            detected.append(
                DetectedConcept(
                    concept=concept,
                    confidence=confidence,
                    match_count=len(evidence),
                    evidence=evidence,
                )
            )

        return detected

    def _build_evidence(
        self,
        lines: list[str],
        keywords: list[KeywordRule],
    ) -> tuple[list[Evidence], float]:
        """
        Find all keyword occurrences inside the chunk.
        and accumulate their weights.
        """

        evidence: list[Evidence] = []

        total_weight = 0.0
        
        for line_number, line in enumerate(
            lines,
            start=1,
        ):

            for rule in keywords:

                pattern = (
                    rf"\b{re.escape(rule.keyword.lower())}\b"
                )

                if re.search(pattern, line):

                    if not any(
                        e.keyword == rule.keyword
                        and e.line_number == line_number
                        for e in evidence
                    ):

                        evidence.append(
                            Evidence(
                                keyword=rule.keyword,
                                line_number=line_number,
                            )
                        )

                        total_weight += rule.weight

        return evidence, total_weight

    def _calculate_confidence(
        self,
        total_weight: float,
    ) -> float:
        """
        Calculate confidence based on the total weight
        of the matched keywords.

        Confidence is capped at 1.0.
        """

        return min(
            total_weight,
            MAX_CONCEPT_WEIGHT
        )


concept_detector = ConceptDetector()