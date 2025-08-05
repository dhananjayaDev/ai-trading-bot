import yfinance as yf
from prophet import Prophet
import matplotlib.pyplot as plt

def train_prophet(ticker: str = "AAPL"):
    data = yf.download(ticker, period="1y", interval="1d")
    df = data.reset_index()[["Date", "Close"]].rename(columns={"Date": "ds", "Close": "y"})

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    model.plot(forecast)
    plt.title(f"{ticker} Forecast with Prophet")
    plt.savefig(f"models/{ticker}_prophet_forecast.png")
    plt.show()

if __name__ == "__main__":
    train_prophet()