import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App
st.title("Stock Metrics Dashboard")

# Sidebar for user input (Stock symbol)
stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, GOOG)")

# Function to fetch stock data
def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    stock_data = stock.history(period="1d")  # Get the most recent data
    stock_info = stock.info  # Fetch stock info
    return stock_data, stock_info

# Display metrics and data
if stock_symbol:
    try:
        # Fetch stock data and information
        stock_data, stock_info = fetch_stock_data(stock_symbol)

        # Display stock info and metrics
        st.subheader(f"{stock_symbol} Stock Information")
        st.write(f"**Company Name:** {stock_info.get('longName', 'N/A')}")
        st.write(f"**Sector:** {stock_info.get('sector', 'N/A')}")
        st.write(f"**Market Cap:** {stock_info.get('marketCap', 'N/A')}")
        st.write(f"**Current Price:** ${stock_info.get('currentPrice', 'N/A')}")
        st.write(f"**PE Ratio:** {stock_info.get('trailingPE', 'N/A')}")
        st.write(f"**Dividend Yield:** {stock_info.get('dividendYield', 'N/A')}")
        st.write(f"**Volume:** {stock_info.get('volume', 'N/A')}")

        # Display historical data (daily high/low, close, volume)
        st.subheader("Stock Historical Data (Last 7 Days)")
        stock_data = yf.Ticker(stock_symbol).history(period="7d")
        st.write(stock_data)

        # Plot the stock's closing price
        st.subheader("Stock Price History")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(stock_data.index, stock_data['Close'], label="Closing Price", color='blue')
        ax.set_xlabel("Date")
        ax.set_ylabel("Closing Price ($)")
        ax.set_title(f"{stock_symbol} - Closing Price History (Last 7 Days)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)

        # Plot volume
        st.subheader("Stock Volume History")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(stock_data.index, stock_data['Volume'], label="Volume", color='orange')
        ax.set_xlabel("Date")
        ax.set_ylabel("Volume")
        ax.set_title(f"{stock_symbol} - Volume History (Last 7 Days)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error fetching data for {stock_symbol}: {str(e)}")
else:
    st.write("Please enter a stock symbol to view the data.")
