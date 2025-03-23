from fastapi import FastAPI, HTTPException
import yfinance as yf
import pandas as pd
import numpy as np

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Stock RSI API"}

@app.get("/stock-rsi/")
def get_stock_rsi(stock_symbol: str, period: int = 14):
    """
    Fetches the Relative Strength Index (RSI) for a given stock.
    
    Parameters:
    - stock_symbol (str): Stock ticker symbol (e.g., "RELIANCE.NS")
    - period (int): Number of days for RSI calculation (default = 14)
    
    Returns:
    - RSI value (0-100)
    """
    try:
        # Fetch historical data
        stock = yf.Ticker(stock_symbol)
        data = stock.history(period="2mo")  # Fetch 2 months of data for better accuracy

        if data.empty:
            raise HTTPException(status_code=404, detail="Stock data not found")

        # Get closing prices
        close_prices = data["Close"]

        # Calculate daily price changes
        delta = close_prices.diff()

        # Separate gains and losses
        gain = np.where(delta > 0, delta, 0)
        loss = np.where(delta < 0, -delta, 0)

        # Calculate average gain & average loss (Exponential Moving Average)
        avg_gain = pd.Series(gain).rolling(window=period, min_periods=1).mean()
        avg_loss = pd.Series(loss).rolling(window=period, min_periods=1).mean()

        # Calculate Relative Strength (RS) and RSI
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        # Get the latest RSI value
        latest_rsi = round(rsi.iloc[-1], 2)

        return {
            "stock": stock_symbol,
            "period": period,
            "rsi_value": latest_rsi
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
