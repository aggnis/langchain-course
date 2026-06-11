from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
load_dotenv()

class Source(BaseModel):
    """Represents a source of information."""
    url:str = Field(description="The URL of the source.")

class AgentResponse(BaseModel):
    """Represents the structured response from the agent."""
    answer: str = Field(description="The answer to the user's query.")
    sources: List[Source] = Field(default_factory=list, description="A list of sources used to generate the answer.")

llm = ChatOllama(model="qwen3.5:0.8b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)
def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="What is the weather in Tokyo?")})
    print(result)
    
if __name__ == "__main__":
    main()
