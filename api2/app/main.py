from fastapi import FastAPI, HTTPException
import yfinance as yf
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Stock Rate of Change (ROC) API"}

@app.get("/stock-roc/")
def get_stock_roc(stock_symbol: str, period: int = 14):
    """
    Fetches the Rate of Change (ROC) for a given stock.
    
    Parameters:
    - stock_symbol (str): Stock ticker symbol (e.g., "RELIANCE.NS")
    - period (int): Number of days for ROC calculation (default = 14)
    
    Returns:
    - ROC percentage
    """
    try:
        # Fetch historical data
        stock = yf.Ticker(stock_symbol)
        data = stock.history(period=f"{period + 1}d")

        if data.empty:
            raise HTTPException(status_code=404, detail="Stock data not found")

        # Get closing prices
        close_prices = data["Close"]

        # Calculate Rate of Change (ROC)
        current_price = close_prices.iloc[-1]
        past_price = close_prices.iloc[0]

        roc = ((current_price - past_price) / past_price) * 100

        return {
            "stock": stock_symbol,
            "period": period,
            "current_price": round(current_price, 2),
            "past_price": round(past_price, 2),
            "roc_percentage": round(roc, 2)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
