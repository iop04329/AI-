import json
import httpx
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field
import os
import time

class SearchResult(BaseModel):
    title: str = Field(..., description="標題")
    link: str = Field(..., description="連結")
    snippet: str = Field(..., description="摘要")
    
class SearchResults(BaseModel):
    results: list[SearchResult] = Field(..., description="搜尋結果列表")

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
    try:
        response = httpx.get(url, timeout=10.0)
        time.sleep(1)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace('   ', '').strip()
    except Exception as e:
        errorMsg = f"get_stockArticleAll error => {e}"
        print(errorMsg)
        return errorMsg
    
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
    ) -> SearchResults:
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
        return lst
    except Exception as e:
        print(f"google_search error => {e}")
        return []