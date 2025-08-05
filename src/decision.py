# src/decision.py
import yfinance as yf

def fetch_price(ticker="AAPL"):
    data = yf.download(ticker, period="1d", interval="1m")
    return data["Close"][-1]

def make_decision(current: float, predicted: float, threshold: float = 0.01) -> str:
    """
    Makes a trading decision based on current and predicted prices.
    Args:
        current (float): Current price
        predicted (float): Predicted price
        threshold (float): Minimum % change to trigger action
    Returns:
        str: 'BUY', 'SELL', or 'HOLD'
    """
    if current <= 0 or predicted <= 0:
        return "HOLD"

    change = (predicted - current) / current
    if change > threshold:
        return "BUY"
    elif change < -threshold:
        return "SELL"
    else:
        return "HOLD"