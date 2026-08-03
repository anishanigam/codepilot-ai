from app.ai.agents.base_agent import BaseAgent

from app.ai.agents.prompts.bug_prompt import (
    BUG_AGENT_SYSTEM_PROMPT,
)


class BugAgent(BaseAgent):

    agent_name = "Bug Agent"

    system_prompt = BUG_AGENT_SYSTEM_PROMPT


bug_agent = BugAgent()