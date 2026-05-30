from langchain_community.tools import DuckDuckGoSearchResults
from .calculator import calculator
from .file_reader import read_file
from config import MAX_SEARCH_RESULTS

web_search = DuckDuckGoSearchResults(num_results=MAX_SEARCH_RESULTS)

tools = [web_search, calculator, read_file]
