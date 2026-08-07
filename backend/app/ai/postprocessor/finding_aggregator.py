from app.ai.orchestrator.models import (
    OrchestratorResult,
)

from app.ai.postprocessor.models import (
    MergedFinding,
)


class FindingAggregator:

    def aggregate(
        self,
        result: OrchestratorResult,
    ) -> list[MergedFinding]:

        merged = {}

        for agent_result in result.results:

            for finding in agent_result.findings:

                key = finding.title.strip().lower()

                if key not in merged:

                    merged[key] = MergedFinding(
                        finding=finding,
                        reported_by=[
                            agent_result.agent
                        ],
                    )

                else:

                    if (agent_result.agent not in merged[key].reported_by
                    ):
                        merged[key].reported_by.append(
                            agent_result.agent
                        )

        return list(
            merged.values()
        )


finding_aggregator = FindingAggregator()