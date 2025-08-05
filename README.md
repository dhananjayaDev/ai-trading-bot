# AI Trading Bot

![Banner](https://github.com/dhananjayaDev/ai-trading-bot/blob/main/trading-bot-banner.png)

An intelligent trading assistant that predicts stock prices using **LSTM** and **Prophet**, fetches live market data, and makes auto-decisions (BUY / SELL / HOLD). Built with a clean Streamlit dashboard for real-time interaction and recruiter-friendly presentation.

---

## Features

-  Train **LSTM** and **Prophet** models on historical stock data
-  Fetch **live prices** using Yahoo Finance
-  Make **auto-decisions** based on predicted vs current price
-  Interactive **Streamlit dashboard** with tabs and sidebar
-  Log decisions to CSV for audit and backtesting

---

## Tech Stack

| Component     | Tool/Library        |
|---------------|---------------------|
| Forecasting   | `Prophet`, `LSTM (Keras)` |
| Data Fetching | `yfinance`          |
| Dashboard     | `Streamlit`         |
| Preprocessing | `scikit-learn`      |
| Visualization | `matplotlib`        |
| Logging       | `CSV`, `pickle`     |

---

## Project Structure

```
ai-trading-bot/
├── data/                  # Historical data (optional)
├── models/                # Saved models and plots
├── logs/                  # Decision logs
├── src/                   # Core logic
│   ├── train_lstm.py
│   ├── train_prophet.py
│   ├── fetch_live.py
│   ├── lstm_predict.py
│   ├── decision.py
├── app.py                 # Streamlit dashboard
├── config.py              # Global settings
├── requirements.txt       # Dependencies
├── README.md              # This file
└── .gitignore
```

---

## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/dhananjayaDev/ai-trading-bot.git
cd ai-trading-bot
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Train Models

### Train Prophet

```bash
python src/train_prophet.py --ticker AAPL
```

### Train LSTM

```bash
python src/train_lstm.py --ticker AAPL --epochs 20
```

---

## Run the App

```bash
streamlit run app.py
```

### Dashboard Includes:
-  Ticker selection
-  Live price + LSTM prediction
-  Auto-decision logic
-  Prophet forecast plot
-  LSTM training loss curve

---

##  Example Screenshots

![Prophet Forecast](models/AAPL_prophet_forecast.png)
![LSTM Loss](models/AAPL_lstm_loss.png)
![Dashboard](screenshots/dashboard.png)

---

##  Decision Logging

Decisions are logged to:

```
logs/decisions.csv
```

Each entry includes:
- Timestamp
- Ticker
- Current price
- Predicted price
- Decision

---

##  Future Enhancements

- ✅ Add crypto support via Binance or CoinGecko
- ✅ Toggle between LSTM and Prophet predictions
- ✅ Backtest mode with historical decisions
- ✅ Confidence score or ensemble logic
- ✅ Cyberpunk theme for dashboard

---

##  Author

**Dhananjaya** — Building explainable, recruiter-friendly AI tools with a creative twist.

---

##  License

MIT [LICENSE](https://github.com/dhananjayaDev/ai-trading-bot?tab=MIT-1-ov-file)

