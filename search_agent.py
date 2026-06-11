from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
load_dotenv()
tavily = TavilyClient()
@tool
def search(query: str) -> str:
    """
    Tool that searches over internet.
    Args:
        query (str): The search query.
    Returns:
        str: The search results.
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)

llm = ChatOllama(model="qwen3.5:0.8b")
tools = [search]
agent = create_agent(model=llm, tools=tools)
def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {"messages": [HumanMessage(content="What is the weather in Tokyo?")]}
                          )
    print(result)
    
if __name__ == "__main__":
    main()
