from dotenv import load_dotenv
from typing import cast
import os

load_dotenv()

# LLM
GROQ_API_KEY = cast(str, os.getenv("GROQ_API_KEY"))
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY não encontrada no .env")
MODEL_NAME = "openai/gpt-oss-120b"

# Memory
MAX_TOKEN_LIMIT = ("tokens", 2000)
MAX_MESSAGES = ("messages", 20)
# Tools
MAX_SEARCH_RESULTS = 3
