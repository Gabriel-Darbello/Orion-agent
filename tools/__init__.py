from langchain_community.tools import DuckDuckGoSearchRun
from .calculator import calculator
from .file_reader import read_file

web_search = DuckDuckGoSearchRun()

tools = [web_search, calculator, read_file]
