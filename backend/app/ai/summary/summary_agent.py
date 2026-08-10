import json

from app.ai.llm import llm

from app.ai.models import GitHubFile

from app.ai.summary.prompt import SYSTEM_PROMPT
from app.ai.summary.parser import summary_parser


class SummaryAgent:

    async def generate(
        self,
        files: list[GitHubFile],
        findings,
        recommendation,
    ):

        payload = {

            "files": [

                {
                    "filename": file.filename,
                    "status": file.status,
                    "extension": file.filename.split(".")[-1],
                }

                for file in files
            ],

            "findings": [

                {
                    "title": finding.finding.title,
                    "severity": finding.finding.severity.value,
                    "reported_by": [
                        agent.value
                        for agent in finding.reported_by
                    ],
                }
                for finding in findings
            ],
            "recommendation": recommendation,
        }

        payload_json = json.dumps(payload, indent=2)

        print("=" * 80)
        print("SUMMARY PAYLOAD SIZE")
        print(len(payload_json))
        print("=" * 80)

        response = await llm.ainvoke(

            [

                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },

                {
                    "role": "user",
                    "content": json.dumps(
                        payload,
                        indent=2,
                    ),
                },

            ]

        )

        print("=" * 80)
        print("RAW SUMMARY RESPONSE")
        print(repr(response.content))
        print("=" * 80)

        return summary_parser.parse(
            response.content
        )


summary_agent = SummaryAgent()