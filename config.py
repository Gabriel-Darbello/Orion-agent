from dotenv import load_dotenv
from typing import cast
import os

load_dotenv()

# LLM
GROQ_API_KEY = cast(str, os.getenv("GROQ_API_KEY"))
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY não encontrada no .env")
MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0

# Memory
MAX_TOKEN_LIMIT = ("tokens", 2000)
SUMMARY_THRESHOLD = 1500

# Tools
MAX_SEARCH_RESULTS = 3
