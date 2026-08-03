import json

from app.ai.llm import llm

from app.ai.planner.models import (
    AgentType,
    PlannerInput,
    LLMRoutingResult,
)

from app.ai.planner.prompts import (
    PLANNER_SYSTEM_PROMPT,
    build_planner_prompt,
)


class LLMRouter:

    async def route(
        self,
        planner_input: PlannerInput,
    ) -> LLMRoutingResult:

        prompt = build_planner_prompt(
            filename=planner_input.filename,
            language=planner_input.language,
            chunk_number=planner_input.chunk_number,
            total_chunks=planner_input.total_chunks,
            content=planner_input.content,
        )

        try:

            response = await llm.ainvoke(
                [
                    {
                        "role": "system",
                        "content": PLANNER_SYSTEM_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ]
            )

            data = json.loads(response.content)

            agents = [
                AgentType(agent)
                for agent in data["agents"]
            ]

            return LLMRoutingResult(
                success=True,
                agents=agents,
                reason=data["reason"],
            )

        except Exception as e:

            return LLMRoutingResult(
                success=False,
                agents=[],
                reason=str(e),
            )


llm_router = LLMRouter()