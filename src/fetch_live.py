import yfinance as yf

def fetch_price(ticker: str) -> float:
    """
    Fetches the latest closing price for a given stock ticker.
    
    Args:
        ticker (str): Stock symbol (e.g., 'AAPL', 'GOOG')
    
    Returns:
        float: Latest closing price
    """
    try:
        data = yf.Ticker(ticker)
        hist = data.history(period="1d", interval="1m")
        if hist.empty:
            raise ValueError("No data returned. Market might be closed.")
        latest_price = hist['Close'].iloc[-1]
        return float(latest_price)
    except Exception as e:
        print(f"[ERROR] Failed to fetch price for {ticker}: {e}")
        return -1.0  # Sentinel value for failure