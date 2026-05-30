from langchain_core.tools import tool
from simpleeval import simple_eval

@tool
def calculator(expression: str) -> str:
    """
    Use for numeric expressions and calculus.
    Input must be a math expression like '2 + 2' or 'sqrt(16)'.
    """
    try:
        return str(simple_eval(expression))
    except Exception as e:
        return f"Erro: {e}"
