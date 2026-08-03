# llm.py
from langchain_groq import ChatGroq
from app.core.config import settings


def get_llm(
    temperature: float = 0,
    model: str | None = None,
):
    return ChatGroq(
        model=model or settings.GROQ_MODEL,
        api_key=settings.GROQ_API_KEY,
        temperature=temperature,
        max_retries=2,
    )


# Default instance
llm = get_llm()