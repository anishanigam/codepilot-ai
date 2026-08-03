PLANNER_SYSTEM_PROMPT = """
You are an expert software architect.

Your ONLY responsibility is deciding which specialized
code review agents should review a given code chunk.

Available Agents:

- BUG
- SECURITY
- PERFORMANCE
- STYLE
- BEST_PRACTICES

You MUST NOT review the code.

You MUST NOT explain bugs.

You MUST NOT rewrite the code.

Return ONLY valid JSON.

The response schema is:

{
    "agents": [
        "BUG",
        "SECURITY"
    ],
    "reason": "Short explanation"
}
"""


def build_planner_prompt(
    filename: str,
    language: str,
    chunk_number: int,
    total_chunks: int,
    content: str,
) -> str:

    return f"""
Filename:
{filename}

Language:
{language}

Chunk:
{chunk_number}/{total_chunks}

Code:

{content}
"""