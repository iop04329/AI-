from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.run.agent import RunOutput
import os
from tool.finance import get_stock_name
from tool.txt_tool import read_txt_file
from tool.search import *

def analyze_run(stock_name:str) -> RunOutput:
    model = os.getenv("model")
    apiKey = os.getenv("api_key")
    prompt = read_txt_file('prompt/prompt.txt')
    instuction = read_txt_file('prompt/instruction.txt')
    llm = OpenAIChat(
        id=model,
        temperature=0.5,
        system_prompt=prompt,
        instructions=instuction,
        api_key=apiKey,
        )
    agent = Agent(
        model=llm,        
        )
    articles = fetch_articles(query=f'{stock_name}相關新聞',num=10,feedMax=2)
    json_data = [article.model_dump() for article in articles]  # List of dict
    json_str = json.dumps(json_data)  # JSON 字串
    messages = [ 
        {"role": "user", "content": "請分析以下新聞文章："}, 
        {"role": "user", "content": json_str}, 
    ]
    response = agent.run(input=messages)
    print(response)
    return response