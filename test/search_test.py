import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tool.search import *

def test():
    url = 'https://tw.stock.yahoo.com/news/00919%E4%B8%8B%E9%80%B1%E9%99%A4%E6%81%AF-%E5%85%AB%E5%A4%A7%E5%85%AC%E8%82%A1%E7%A0%B82-93%E5%84%84%E6%90%B6%E4%B8%8A%E8%BB%8A-%E9%80%99%E6%AA%94%E9%80%A38%E7%B4%85-%E9%80%B1%E6%BC%B24-115000140.html'
    res = get_stockArticleAll(url=url)
    print(res)
    

if __name__ == "__main__":
    test()