from app.ai.agents.base_agent import BaseAgent

from app.ai.agents.prompts.security_prompt import (
    SECURITY_AGENT_SYSTEM_PROMPT,
)


class SecurityAgent(BaseAgent):

    agent_name = "Security Agent"

    system_prompt = SECURITY_AGENT_SYSTEM_PROMPT


security_agent = SecurityAgent()