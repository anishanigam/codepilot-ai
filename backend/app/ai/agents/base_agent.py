import json
from abc import ABC

from app.ai.llm import llm

from app.ai.agents.models import (
    AgentResult,
    ReviewFinding,
    Severity,
)

from app.ai.planner.models import (
    ReviewTask,
    AgentType
)


class BaseAgent(ABC):

    system_prompt: str = ""

    agent_name: str = ""

    async def review(
        self,
        task: ReviewTask,
    ) -> AgentResult:
        """
        Execute AI review for a single ReviewTask.
        """

        try:

            response = await llm.ainvoke(
                [
                    {
                        "role": "system",
                        "content": self.system_prompt,
                    },
                    {
                        "role": "user",
                        "content": self._build_prompt(task),
                    },
                ]
            )

            return self._parse_response(
                response.content,
                task.agent,
            )

        except Exception as e:

            return AgentResult(
                agent=task.agent,
                success=False,
                error=str(e),
            )

    def _build_prompt(
    self,
    task: ReviewTask,
) -> str:
        """
    Build the prompt sent to the LLM.

    Includes planner metadata so the reviewing agent
    understands why it was selected and what concepts
    were already detected.
    """

        planner_input = task.planner_input

        concept_summary = []

        for concept in task.concepts:

            concept_summary.append(
            f"- {concept.concept.value}"
            f" (confidence={concept.confidence:.2f}, "
            f"matches={concept.match_count})"
           )

        detected_concepts = "\n".join(concept_summary)

        if not detected_concepts:
            detected_concepts = "None"

        return f"""
    Repository File:
    {planner_input.filename}

    Programming Language:
    {planner_input.language}

    Git Status:
    {planner_input.git_status}

    Chunk:
    {planner_input.chunk_number}/{planner_input.total_chunks}

    Planner Source:
    {task.source}

    Assigned Agent:
    {task.agent.value}

    Detected Concepts:
    {detected_concepts}

    Planner Reason:
    {task.routing_reason}

    Code:

    ```{planner_input.language}
    {planner_input.content}
```
    Instructions:

Focus ONLY on issues relevant to your assigned role.

Ignore problems outside your responsibility.

Return ONLY valid JSON.

The JSON MUST follow exactly this schema:

{{
  "findings": [
    {{
      "title": "Short title",
      "description": "Explain the issue.",
      "severity": "LOW | MEDIUM | HIGH | CRITICAL",
      "recommendation": "Suggested fix.",
      "line_start": 10,
      "line_end": 15
    }}
  ]
}}

Do not include markdown.
Do not wrap the JSON in ```json.
Do not include any explanation before or after the JSON.
    """

    def _parse_response(
        self,
        response: str,
        agent: AgentType,
    ) -> AgentResult:
        """
        Parse LLM JSON response into AgentResult.
        """

        try:

            data = json.loads(response)
            

            findings = []

            for finding in data.get(
                "findings",
                [],
            ):

                findings.append(
                    ReviewFinding(
                        title=finding["title"],
                        description=finding["description"],
                        severity=Severity(
                            finding["severity"].lower()
                        ),
                        recommendation=finding[
                            "recommendation"
                        ],
                        line_start=finding.get(
                            "line_start"
                        ),
                        line_end=finding.get(
                            "line_end"
                        ),
                    )
                )

            return AgentResult(
                agent=agent,
                success=True,
                findings=findings,
            )

        except Exception as e:

            return AgentResult(
                agent=agent,
                success=False,
                error=f"Invalid JSON: {e}",
            )