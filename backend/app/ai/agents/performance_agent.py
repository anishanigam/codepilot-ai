from app.ai.agents.base_agent import BaseAgent

from app.ai.agents.prompts.performance_prompt import (
    PERFORMANCE_AGENT_SYSTEM_PROMPT,
)


class PerformanceAgent(BaseAgent):

    agent_name = "Performance Agent"

    system_prompt = PERFORMANCE_AGENT_SYSTEM_PROMPT


performance_agent = PerformanceAgent()