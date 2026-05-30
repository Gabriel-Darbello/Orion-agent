from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_groq import ChatGroq
from pydantic import SecretStr
from tools import tools
from config import *

llm = ChatGroq(model=MODEL_NAME, api_key=SecretStr(GROQ_API_KEY))

agent = create_agent(
    model=llm,
    tools=tools,
    middleware=[
        SummarizationMiddleware(
            model="llama-3.1-8b-instant",
            trigger=MAX_TOKEN_LIMIT,
            keep=("messages", 20)
        )
    ],
    checkpointer=InMemorySaver(),
)
