import asyncio

from app.ai.planner.models import ReviewTask

from app.ai.orchestrator.executor import (
    task_executor,
)

from app.ai.orchestrator.models import (
    OrchestratorResult,
)


class Orchestrator:

    async def run(
        self,
        tasks: list[ReviewTask],
    ) -> OrchestratorResult:
        """
        Execute all review tasks concurrently.
        """

        execution_results  = await asyncio.gather(
            *[
                task_executor.execute(task)
                for task in tasks
            ],
            return_exceptions=True,
        )

        results = []

        errors = []

        for item in execution_results :

            if isinstance(item, Exception):

                errors.append(str(item))
                continue

            elif item.success:

                results.append(item)

            else:

                errors.append(item.error)

        return OrchestratorResult(
            success=len(errors) == 0,
            results=results,
            errors=errors,
        )


orchestrator = Orchestrator()