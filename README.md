# Orion — ReAct AI Agent

A simple AI agent built with LangChain and Groq that can search the web, perform calculations, and read files.

## Features

- **ReAct loop** — Thought → Action → Observation powered by LangChain
- **Web search** — DuckDuckGo integration for real-time information
- **Calculator** — Safe math expression evaluation via `simpleeval`
- **File reader** — Read local text files
- **Memory** — Automatic summarization when conversation history exceeds token limit

## Stack

- [LangChain](https://python.langchain.com/) — agent framework
- [Groq](https://groq.com/) — LLM inference (openai/gpt-oss-120b)
- [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) — web search tool
- [simpleeval](https://pypi.org/project/simpleeval/) — safe math evaluation

## Project Structure

```
react-agent/
├── agent/
│   └── agent.py        # AgentExecutor setup
├── tools/
│   ├── __init__.py     # Tools registry
│   ├── calculator.py
│   └── file_reader.py
├── interface/
│   └── cli.py          # CLI interface
├── main.py
├── config.py
└── requirements.txt
```

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/your-username/react-agent.git
cd react-agent
```

**2. Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**
```bash
cp .env.example .env
```
Add your Groq API key to `.env`:
```
GROQ_API_KEY=your_key_here
```
Get your free API key at [console.groq.com](https://console.groq.com).

**5. Run**
```bash
python main.py
```

## Usage

```
Hi, I am Orion, what do you need today?
Type "exit" to leave

You: what is the latest news about Python?
Orion: ...

You: what is 1234 * 5678?
Orion: ...

You: read the file /path/to/file.txt
Orion: ...
```

## License

MIT
