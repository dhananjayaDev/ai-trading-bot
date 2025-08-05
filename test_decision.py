from src.fetch_live import fetch_price
from src.decision import make_decision

ticker = "AAPL"
current = fetch_price(ticker)
predicted = current * 1.03  # Simulated prediction

print(f"Current: ${current:.2f}, Predicted: ${predicted:.2f}")
print("Decision:", make_decision(current, predicted))