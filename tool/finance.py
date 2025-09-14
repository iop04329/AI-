import yfinance as yf

def get_stock_name(ticker_symbol: str) -> str:
    """
    輸入股票代號，返回該股票的名稱（longName）。
    若無法找到，回傳提示文字。
    """
    try:
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info
        return info.get("longName", "")
    except Exception as e:
        print(f"get_stock_name error => {e}")
        return ""