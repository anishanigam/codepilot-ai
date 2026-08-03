from app.ai.planner.concept_detector import concept_detector
from app.ai.planner.rule_engine import rule_engine
from app.ai.planner.llm_router import llm_router

from app.ai.planner.mappings import DEFAULT_AGENTS

from app.ai.planner.models import (
    PlannerInput,
    ReviewTask,
)


class Planner:

    async def plan(
        self,
        planner_input: PlannerInput,
    ) -> list[ReviewTask]:

        concepts = concept_detector.detect(
            planner_input
        )

        routing = rule_engine.route(
            concepts
        )

        tasks: list[ReviewTask] = []

        # ---------------------------
        # Rule Engine Routing
        # ---------------------------
        if not routing.use_llm:

            for agent in routing.agents:

                tasks.append(
                    ReviewTask(
                        task_id=f"{planner_input.chunk_id}_{agent.value}",
                        planner_input=planner_input,
                        agent=agent,
                        concepts=concepts,
                        routing_reason=routing.reason,
                        source="rule_engine",
                    )
                )

            return tasks

        # ---------------------------
        # LLM Routing
        # ---------------------------
        llm_result = await llm_router.route(
            planner_input
        )

        if llm_result.success:

            for agent in llm_result.agents:

                tasks.append(
                    ReviewTask(
                        task_id=f"{planner_input.chunk_id}_{agent.value}",
                        planner_input=planner_input,
                        agent=agent,
                        concepts=concepts,
                        routing_reason=llm_result.reason,
                        source="llm",
                    )
                )

            return tasks

        # ---------------------------
        # Fallback Routing
        # ---------------------------
        fallback_agents = DEFAULT_AGENTS.get(
            planner_input.language,
            DEFAULT_AGENTS["python"],
        )

        for agent in fallback_agents:

            tasks.append(
                ReviewTask(
                    task_id=f"{planner_input.chunk_id}_{agent.value}",
                    planner_input=planner_input,
                    agent=agent,
                    concepts=concepts,
                    routing_reason="LLM routing failed. Using default agents.",
                    source="fallback",
                )
            )

        return tasks


planner = Planner()