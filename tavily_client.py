from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
load_dotenv()

llm = ChatOllama(model="qwen3.5:0.8b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)
def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="What is the weather in Tokyo?")})
    print(result)
    
if __name__ == "__main__":
    main()
