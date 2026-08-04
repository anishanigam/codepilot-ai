import asyncio
import logging

from app.core.config import settings

from app.ai.agents.models import (
    AgentResult,
)

from app.ai.planner.models import (
    ReviewTask,
)

from app.ai.orchestrator.registry import (
    AgentRegistry,
)

logger = logging.getLogger(__name__)


class TaskExecutor:

    async def execute(
        self,
        task: ReviewTask,
    ) -> AgentResult:

        agent = AgentRegistry.get_agent(
            task.agent
        )

        for attempt in range(
            settings.AI_MAX_RETRIES
        ):

            try:

                logger.info(
                    f"Running {task.agent.value} "
                    f"(Attempt {attempt + 1})"
                )

                return await asyncio.wait_for(
                    agent.review(task),
                    timeout=settings.AI_REQUEST_TIMEOUT,
                )

            except asyncio.TimeoutError:

                logger.warning(
                    f"{task.agent.value} timed out "
                    f"(Attempt {attempt + 1})"
                )

            except Exception as e:
                logger.exception(
                    f"{task.agent.value} failed "
                    f"(Attempt {attempt + 1})"
                )

        logger.error(
            f"{task.agent.value} failed after "
            f"{settings.AI_MAX_RETRIES} attempts."
        )

        return AgentResult(
            agent=task.agent,
            success=False,
            error=(
                f"Agent failed after "
                f"{settings.AI_MAX_RETRIES} attempts."
            ),
        )


task_executor = TaskExecutor()