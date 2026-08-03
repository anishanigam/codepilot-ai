from app.ai.agents.base_agent import BaseAgent

from app.ai.agents.prompts.style_prompt import (
    STYLE_AGENT_SYSTEM_PROMPT,
)


class StyleAgent(BaseAgent):

    agent_name = "Style Agent"

    system_prompt = STYLE_AGENT_SYSTEM_PROMPT


style_agent = StyleAgent()