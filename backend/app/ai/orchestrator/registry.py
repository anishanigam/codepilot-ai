from app.ai.planner.models import AgentType

from app.ai.agents.bug_agent import bug_agent
from app.ai.agents.security_agent import security_agent
from app.ai.agents.performance_agent import performance_agent
from app.ai.agents.best_practices_agent import best_practices_agent
from app.ai.agents.style_agent import style_agent

class AgentRegistry:

    _registry = {
        AgentType.BUG: bug_agent,
        AgentType.SECURITY: security_agent,
        AgentType.PERFORMANCE: performance_agent,
        AgentType.BEST_PRACTICES: best_practices_agent,
        AgentType.STYLE: style_agent,
    }

    @classmethod
    def register(
        cls,
        agent_type: AgentType,
        agent,
    ) -> None:
        """
        Register a new review agent.
        """
        cls._registry[agent_type] = agent

    @classmethod
    def get_agent(
        cls,
        agent_type: AgentType,
    ):

        if agent_type not in cls._registry:
            raise ValueError(
                f"No agent registered for '{agent_type.value}'"
            )


        return cls._registry[agent_type]