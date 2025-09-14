from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.run.agent import RunOutput
import os
from tool.txt_tool import read_txt_file
from tool.search import google_search, get_stockArticleAll

def analyze_run(stock_id:str) -> RunOutput:
    model = os.getenv("model")
    apiKey = os.getenv("api_key")
    prompt = read_txt_file('prompt/prompt.txt')
    instuction = read_txt_file('prompt/instruction.txt')
    llm = OpenAIChat(
        id=model,
        temperature=0.8,
        system_prompt=prompt,
        instructions=instuction,
        api_key=apiKey,
        )
    agent = Agent(
        model=llm,        
        tools=[google_search, get_stockArticleAll],
        )
    response = agent.run(input=f"請幫我分析這支股票:{stock_id}")
    print(response)
    return response