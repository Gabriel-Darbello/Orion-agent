from langchain_core.tools import tool

@tool
def read_file(file_path:str) -> str:
    """
    Use this tool to read the content of a text file.
    Input must be the full file path, like '/home/user/doc.txt' or 'data/notes.txt'.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Arquivo não encontrado: {file_path}"
    except Exception as e:
        return f"Erro ao ler arquivo: {e}"
