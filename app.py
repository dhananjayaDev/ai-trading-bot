import streamlit as st
from src.fetch_live import fetch_price
from src.decision import make_decision

st.title("AI Trading Bot")
# ticker = st.text_input("Enter stock ticker", "AAPL")
# Replace this:
# ticker = st.text_input("Enter stock ticker", "AAPL")

# With this:
ticker = st.selectbox(
    "Choose a stock ticker",
    ["AAPL", "GOOG", "TSLA", "MSFT", "AMZN", "NVDA", "META", "NFLX", "INTC", "IBM"],
    index=0
)

if st.button("Fetch & Decide"):
    current = fetch_price(ticker)
    predicted = current * 1.03  # Simulated prediction
    decision = make_decision(current, predicted)

    st.metric("Current Price", f"${current:.2f}")
    st.metric("Predicted Price", f"${predicted:.2f}")
    st.success(f"Decision: {decision}")