from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_groq import ChatGroq
from pydantic import SecretStr
from tools import tools
from config import *

llm = ChatGroq(model=MODEL_NAME, api_key=SecretStr(GROQ_API_KEY))
llm_mini = ChatGroq(model="llama-3.1-8b-instant", api_key=SecretStr(GROQ_API_KEY))

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are Orion, a helpful assistant. When using tools, always follow the exact function call format required.",
    middleware=[
        SummarizationMiddleware(
            model=llm_mini,
            trigger=MAX_TOKEN_LIMIT,
            keep=MAX_MESSAGES
        )
    ],
    checkpointer=InMemorySaver(),
)
