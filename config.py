from dotenv import load_dotenv
import os

load_dotenv()

# LLM
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0

# Memory
MAX_TOKEN_LIMIT = 2000
SUMMARY_THRESHOLD = 1500

# Tools
MAX_SEARCH_RESULTS = 3
