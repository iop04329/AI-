import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ai.analyze_model import StockAnalysis
from tool.search import *

def test():
    try:
        content = '```json\n{\n    "AI分析總結": "群益台灣精選高息ETF (00919.TW) 近期進行除息，並吸引大量投資者關注。該ETF的高股息特性使其在市場波動中成為資金避風港。",\n    "媒體情緒觀察": "媒體對群益台灣精選高息ETF的情緒整體偏正面，強調其高股息率和穩定的收益特性，吸引了大量投資者的關注。",\n    "短期分析": "短期內，由於該ETF的除息活動，吸引了投資者的目光，預計成交量會有所增加，並可能在除息後出現股價調整。",\n    "中長期分析": "中長期來看，群益台灣精選高息ETF因其穩定的股息收益，預計將持續吸引尋求穩定收益的投資者，並在市場波動中保持相對穩定的表現。",\n    "詳細新聞列表": [\n        {\n            "文章名稱": "群益台灣精選高息(00919.TW) 相關新聞- Yahoo 奇摩股市",\n            "文章連結": "https://tw.stock.yahoo.com/quote/00919.TW/news"\n        },\n        {\n            "文章名稱": "群益台灣精選高息(00919) - 相關新聞- 台股| 玩股網",\n            "文章連結": "https://www.wantgoo.com/stock/etf/00919/news"\n        }\n    ]\n}\n```'
        analyze_result:StockAnalysis = StockAnalysis.model_validate_json(json.loads(content))
        print(analyze_result.AI分析總結)
    except Exception as e:
        print(f'test error {e}')
    
    

if __name__ == "__main__":
    test()