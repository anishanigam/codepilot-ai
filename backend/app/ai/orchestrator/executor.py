from app.ai.planner.models import ReviewTask

from app.ai.orchestrator.registry import AgentRegistry


class TaskExecutor:

    async def execute(
        self,
        task: ReviewTask,
    ):

        agent = AgentRegistry.get_agent(
            task.agent
        )

        return await agent.review(task)


task_executor = TaskExecutor()