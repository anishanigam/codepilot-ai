from app.ai.planner.models import (
    AgentType,
    DetectedConcept,
    RuleEngineResult,
)

from app.ai.planner.mappings import (
    CONCEPT_TO_AGENTS,
    CONFIDENCE_THRESHOLD,
)


class RuleEngine:

    def route(
        self,
        concepts: list[DetectedConcept],
    ) -> RuleEngineResult:

        if not concepts:

            return RuleEngineResult(
                use_llm=True,
                agents=[],
                reason="No relevant concepts detected.",
            )

        selected_agents: set[AgentType] = set()

        confident = False

        for concept in concepts:

            if concept.confidence >= CONFIDENCE_THRESHOLD:

                confident = True

                selected_agents.update(
                    CONCEPT_TO_AGENTS.get(
                        concept.concept,
                        [],
                    )
                )

        if not confident:

            return RuleEngineResult(
                use_llm=True,
                agents=[],
                reason="Low confidence concept detection.",
            )

        return RuleEngineResult(
            use_llm=False,
            agents=sorted(
                selected_agents,
                key=lambda agent: agent.value,
            ),
            reason="Rule-based routing succeeded.",
        )


rule_engine = RuleEngine()