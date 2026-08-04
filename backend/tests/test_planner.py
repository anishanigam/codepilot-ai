import asyncio

from app.ai.planner.planner import planner
from app.ai.planner.models import PlannerInput


planner_input = PlannerInput(
    chunk_id="chunk_1",
    filename="auth.py",
    language="python",
    git_status="modified",
    chunk_number=1,
    total_chunks=1,
    content="""
    def add(a, b):
    return a + b
""",
)


async def main():

    tasks = await planner.plan(planner_input)

    print("=" * 70)
    print("Generated Review Tasks")
    print("=" * 70)

    print(f"\nTotal Tasks: {len(tasks)}\n")

    for task in tasks:

        print(f"Task ID       : {task.task_id}")
        print(f"Agent         : {task.agent.value}")
        print(f"Source        : {task.source}")
        print(f"Reason        : {task.routing_reason}")

        print("Detected Concepts:")

        for concept in task.concepts:
            print(
                f"  • {concept.concept.value}"
                f" | confidence={concept.confidence:.2f}"
                f" | matches={concept.match_count}"
            )

        print("-" * 70)


if __name__ == "__main__":
    asyncio.run(main())