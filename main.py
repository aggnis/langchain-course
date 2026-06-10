from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


load_dotenv()

def main():
    print("Hello from langchain-course!")
    information = "My name is John Doe and I am a software engineer."
    summary_template = """Summarize the following information in one sentence:
{information}"""

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOllama(model="qwen3.5:0.8b", temperature=0)
    
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)
if __name__ == "__main__":
    main()
