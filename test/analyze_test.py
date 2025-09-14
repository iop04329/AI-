import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ai.analyze import analyze_run
from agno.run.agent import RunOutput
from tool.finance import get_stock_name
from ai.analyze_model import StockAnalysis

def test():
    ticker_id = '00919.TW'
    ticker_name = get_stock_name(ticker_symbol=ticker_id)
    print(f'股票代號:{ticker_id} 股票名稱:{ticker_name}')
    res:RunOutput = analyze_run(stock_id=ticker_id)
    print(res.content)
    analyze_result:StockAnalysis = StockAnalysis.model_validate_json(res.content)
    # print(res.messages)
    print(analyze_result.分析總結)
    # res.messages #全部聊天訊息
    


if __name__ == "__main__":
    test()