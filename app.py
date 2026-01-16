import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import os

# Step 1: Fetch data
tickers = ["AAPL","TSLA","AMZN","GOOGL","MSFT"]
data = {}

for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    data[ticker] = hist

# Step 2: Clean and process
for ticker, df in data.items():
    df.ffill(inplace=True)  # Fill missing values first
    df['Daily_Return'] = df['Close'].pct_change() * 100
    df['Moving_Avg_20'] = df['Close'].rolling(20).mean()
    df['Volatility'] = df['Daily_Return'].rolling(20).std()

# Save CSV locally
os.makedirs("data", exist_ok=True)
for ticker, df in data.items():
    df.to_csv(f"data/{ticker}_1yr.csv")

# Step 3: Save charts
os.makedirs("outputs", exist_ok=True)

plt.figure(figsize=(12,6))
for ticker, df in data.items():
    plt.plot(df.index, df['Close'], label=ticker)
plt.title("Stock Closing Price Trends - Last 1 Year")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.savefig(os.path.join("outputs","closing_price_trends.png"))

plt.figure(figsize=(12,6))
for ticker, df in data.items():
    plt.plot(df.index, df['Daily_Return'], label=ticker)
plt.title("Daily Returns (%) Comparison")
plt.xlabel("Date")
plt.ylabel("Daily Return (%)")
plt.legend()
plt.savefig(os.path.join("outputs","daily_returns.png"))

# Step 4: Streamlit Dashboard
st.title("Global Stock Market Explorer")

ticker = st.selectbox("Select Stock", list(data.keys()))
df = data[ticker]  # reuse pre-fetched data

fig = px.line(df, x=df.index, y='Close', title=f"{ticker} Closing Prices")
st.plotly_chart(fig)

fig2 = px.line(df, x=df.index, y='Daily_Return', title=f"{ticker} Daily Returns (%)")
st.plotly_chart(fig2)
