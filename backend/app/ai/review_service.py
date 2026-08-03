from app.ai.preprocessor import preprocessor

from app.ai.planner.planner import planner
from app.ai.review_result import ReviewResult
from app.ai.orchestrator.orchestrator import orchestrator

from app.ai.postprocessor.finding_aggregator import (
    finding_aggregator,
)
from app.ai.models import (
    GitHubFile,
    ReviewableFile,
    PatchChunk,
)

from app.ai.planner.models import (
    PlannerInput,
    ReviewTask,
)


class ReviewService:

    def _build_planner_input(
        self,
        reviewable_file: ReviewableFile,
        chunk: PatchChunk,
    ) -> PlannerInput:

        return PlannerInput(
            chunk_id=chunk.chunk_id,
            filename=reviewable_file.filename,
            language=reviewable_file.language,
            git_status=reviewable_file.status,
            chunk_number=chunk.chunk_number,
            total_chunks=chunk.total_chunks,
            content=chunk.content,
        )

    async def review(
        self,
        files: list[GitHubFile],
    ):

        # -------------------------
        # Step 1
        # -------------------------

        preprocessing_result = preprocessor.process(
            files
        )

        all_tasks: list[ReviewTask] = []

        # -------------------------
        # Step 2
        # Planner
        # -------------------------

        for reviewable_file in (
            preprocessing_result.reviewable_files
        ):

            for chunk in reviewable_file.chunks:

                planner_input = (
                    self._build_planner_input(
                        reviewable_file,
                        chunk,
                    )
                )

                tasks = await planner.plan(
                    planner_input
                )

                all_tasks.extend(tasks)

        # -------------------------
        # Step 3
        # Execute
        # -------------------------

        orchestration_result = (
            await orchestrator.run(
                all_tasks
            )
        )

        merged_findings = finding_aggregator.aggregate(
            orchestration_result
        )

        summary = summary_generator.generate(
            merged_findings
        )

        
        return ReviewResult(
            statistics=preprocessing_result.statistics,
            skipped_files=preprocessing_result.skipped_files,
            summary=summary,
            merged_findings=merged_findings,
            errors=orchestration_result.errors,
        )

review_service = ReviewService()