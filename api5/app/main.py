from fastapi import FastAPI, HTTPException
import yfinance as yf
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the NIFTY Index Growth API"}

@app.get("/nifty-growth/")
def get_nifty_growth(index_symbol: str = "^NSEI", period: str = "30d"):
    """
    Fetches the growth percentage of a given NIFTY index over a specified period.

    Parameters:
    - index_symbol (str): The symbol of the NIFTY index (default: "^NSEI" for NIFTY 50).
    - period (str): Time period (e.g., "7d", "30d", "90d", "180d").

    Returns:
    - Growth percentage of the index over the period.
    """
    try:
        # Fetch historical data
        index_data = yf.Ticker(index_symbol).history(period=period)

        if index_data.empty:
            raise HTTPException(status_code=404, detail="Index data not found")

        # Extract first and last closing prices
        start_price = index_data["Close"].iloc[0]
        end_price = index_data["Close"].iloc[-1]

        # Calculate percentage growth
        growth_percentage = ((end_price - start_price) / start_price) * 100

        return {
            "index_symbol": index_symbol,
            "start_price": round(start_price, 2),
            "end_price": round(end_price, 2),
            "growth_percentage": round(growth_percentage, 2),
            "period": period
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
