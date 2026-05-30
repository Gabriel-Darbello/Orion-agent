from agent.agent import agent
from langchain_core.runnables import RunnableConfig

config: RunnableConfig = {"configurable": {"thread_id": "1"}}

print("Hi, I am Orion what you need today?")
print('Type "exit" to leave')

while True:
    message = input("Your message: ")

    if message.lower() == "exit":
        break

    if not message.strip():
        continue

    result = agent.invoke(
        {"messages": [{"role":"user", "content":message}]},
        config
    )

    print(f"Orion: {result['messages'][-1].content}")
