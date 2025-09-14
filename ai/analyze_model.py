from typing import List
from pydantic import BaseModel, HttpUrl
import json

# -----------------------------
# 1️⃣ 定義模型
# -----------------------------
class NewsItem(BaseModel):
    文章名稱: str
    文章連結: HttpUrl

class StockAnalysis(BaseModel):
    AI分析結果: str
    分析總結: str
    媒體情緒觀察: str
    短期分析: str
    中長期分析: str
    詳細新聞列表: List[NewsItem]
