from app.ai.planner.models import (
    PlannerInput,
    DetectedConcept,
    Evidence,
    ConceptType,
)

from app.ai.planner.mappings import (
    CONCEPT_KEYWORDS,
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

            evidence = self._build_evidence(
                lower_lines,
                keywords,
            )

            if not evidence:
                continue

            confidence = self._calculate_confidence(
                len(evidence)
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
        keywords: set[str],
    ) -> list[Evidence]:
        """
        Find all keyword occurrences inside the chunk.

        Uses word-boundary regex matching to avoid
        false positives like:

            token     ❌ tokenizer
            jwt       ❌ jwtManager
            password  ❌ passwordHash
        """

        evidence: list[Evidence] = []

        for line_number, line in enumerate(
            lines,
            start=1,
        ):

            for keyword in keywords:

                pattern = (
                    rf"\b{re.escape(keyword.lower())}\b"
                )

                if re.search(pattern, line):

                    if not any(
                        e.keyword == keyword
                        and e.line_number == line_number
                        for e in evidence
                    ):

                        evidence.append(
                            Evidence(
                                keyword=keyword,
                                line_number=line_number,
                            )
                        )

        return evidence

    def _calculate_confidence(
        self,
        matches: int,
    ) -> float:
        """
        Confidence heuristic.

        1 match  -> 0.33
        2 matches -> 0.66
        >=3 matches -> 1.0
        """

        return min(
            matches / 3,
            1.0,
        )


concept_detector = ConceptDetector()