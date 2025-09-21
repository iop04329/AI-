import json
import random
import httpx
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field, HttpUrl
import os
import time

class SearchResult(BaseModel):
    title: str = Field(..., description="標題")
    link: str = Field(..., description="連結")
    snippet: str = Field(..., description="摘要")
    
class SearchResults(BaseModel):
    results: list[SearchResult] = Field(..., description="搜尋結果列表")

class SearchArticle(BaseModel):
    title: str
    content: str
    link: str

def get_stockArticle(url: str) -> str:
    print(f"Fetching article from URL: {url}")
    try:
        response = httpx.get(url, timeout=10.0)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        article_text = '\n'.join(p.get_text() for p in paragraphs)
        return article_text if article_text else "無法提取文章內容"
    except Exception as e:
        errorMsg = f"get_stockArticle error => {e}"
        print(errorMsg)
        return errorMsg

def get_stockArticleAll(url: str) -> str:
    print(f"Fetching article from URL: {url}")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive"
    }
    try:
        
        response = httpx.get(url, headers=headers, timeout=10.0)
        time.sleep(random.uniform(2, 5))
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace('   ', '').strip()
    except Exception as e:
        errorMsg = f"get_stockArticleAll error => {e}"
        print(errorMsg)
        return errorMsg

# sample code
def google_search(
    query: str, 
    # api_key: str, 
    # engine_id: str,
    data_restrict: str = None,
    exact_terms: str = None,
    exclude_terms: str = None,
    link_site: str = None,
    site_search: str = None, 
    num: int = 10,
    start: int = 1,
    ) -> list[SearchResult]:
    url = 'https://www.googleapis.com/customsearch/v1'
    api_key = os.getenv("search_api_key")
    engine_id = os.getenv("engine_id")
    params = {
        'key': api_key,
        'cx': engine_id,
        'q': query,
        'num': num,
        'start': start,
        'data-restrict': data_restrict,
        'exactTerms': exact_terms,
        'excludeTerms': exclude_terms,
        'linkSite': link_site,
        'siteSearch': site_search,
        'gl': 'tw',           # 加入地理位置
        'hl': 'zh-TW',        # 加入語言偏好
    }
    lst:list[SearchResult] = []
    print(f"Google Search Params: {params}")
    try:
        response = httpx.get(url, params=params)
        if response.status_code == 200:
            json_results:dict = response.json()
            for item in json_results.get('items', []):
                item:dict
                lst.append(SearchResult(
                    title=item.get('title', ''),
                    link=item.get('link', ''),
                    snippet=item.get('snippet', '')
                ))
        for i, result in enumerate(lst, start=1):
            print(f"{i}. Title: {result.title}")
            print(f"   Link: {result.link}")
            print(f"   Snippet: {result.snippet}\n")
        return lst
    except Exception as e:
        print(f"google_search error => {e}")
        return []
    
def google_searchAll(
    query: str,
    data_restrict: str = None,
    exact_terms: str = None,
    exclude_terms: str = None,
    link_site: str = None,
    site_search: str = None,
    max_results: int = 50,  # 想抓取的總筆數
) -> list[SearchResult]:

    url = 'https://www.googleapis.com/customsearch/v1'
    api_key = os.getenv("search_api_key")
    engine_id = os.getenv("engine_id")

    results:list[SearchResult] = []
    
    # Google 每次最多返回 10 筆
    for start in range(1, max_results + 1, 10):
        params = {
            'key': api_key,
            'cx': engine_id,
            'q': query,
            'num': min(10, max_results - len(results)),
            'start': start,
            'data-restrict': data_restrict,
            'exactTerms': exact_terms,
            'excludeTerms': exclude_terms,
            'linkSite': link_site,
            'siteSearch': site_search,
            'gl': 'tw',           # 加入地理位置
            'hl': 'zh-TW',        # 加入語言偏好
        }

        try:
            print(f"Google Search Params: {params}")
            response = httpx.get(url, params=params, timeout=10.0)
            response.raise_for_status()
            json_results = response.json()

            items = json_results.get('items', [])
            if not items:  # 如果沒資料就停止抓取
                break

            for item in items:
                results.append(SearchResult(
                    title=item.get('title', ''),
                    link=item.get('link', ''),
                    snippet=item.get('snippet', '')
                ))

        except Exception as e:
            print(f"google_searcAll error => {e}")
            break  # 遇到錯誤停止分頁抓取

    # 列印結果
    for i, result in enumerate(results, start=1):
        print(f"{i}. Title: {result.title}")
        print(f"   Link: {result.link}")
        print(f"   Snippet: {result.snippet}\n")

    return results

def fetch_articles(query: str, num: int = 30, feedMax: int = 3) -> list[SearchArticle]:
    print(f'fetch_articles params => query:{query} num:{num} feedMax:{feedMax}')
    search_results = google_searchAll(query=query, max_results=num)
    articles: list[SearchArticle] = []

    for result in search_results:
        if len(articles) == feedMax:
            break
        try:
            content = get_stockArticleAll(result.link)
            if content.startswith("get_stockArticleAll error =>"):
                continue  # 忽略抓不到的文章

            article = SearchArticle(
                title=result.title,
                content=content,
                link=result.link
            )
            articles.append(article)

        except Exception as e:
            print(f"[Error] 無法處理 {result.link}")
            continue

    return articles

def extract_article_contents(articles: list[SearchArticle]) -> list[dict[str, str]]:
    """
    將 SearchArticle list 轉成兩個 list:
    - article_text: 只包含 content
    - article_data: 包含 content 與 link，方便給 AI 分析
    """
    article_text = [article.content for article in articles]
    article_data = [{"content": article.content, "link": str(article.link)} for article in articles]
    return article_data