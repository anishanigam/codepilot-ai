from app.ai.agents.base_agent import BaseAgent

from app.ai.agents.prompts.best_practices_prompt import (
    BEST_PRACTICES_AGENT_SYSTEM_PROMPT,
)


class BestPracticesAgent(BaseAgent):

    agent_name = "Best Practices Agent"

    system_prompt = BEST_PRACTICES_AGENT_SYSTEM_PROMPT


best_practices_agent = BestPracticesAgent()