from fastapi import FastAPI, HTTPException
import yfinance as yf

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Stock Relative Strength (RS) API"}

@app.get("/stock-rs/")
def get_stock_relative_strength(stock_symbol: str, benchmark_symbol: str = "^NSEI"):
    """
    Fetches the Relative Strength (RS) of a stock compared to a benchmark index.
    
    Parameters:
    - stock_symbol (str): Stock ticker symbol (e.g., "RELIANCE.NS")
    - benchmark_symbol (str): Benchmark index symbol (default: NIFTY 50 "^NSEI")
    
    Returns:
    - RS value
    """
    try:
        # Fetch stock and benchmark data
        stock = yf.Ticker(stock_symbol).history(period="1d")
        benchmark = yf.Ticker(benchmark_symbol).history(period="1d")

        if stock.empty or benchmark.empty:
            raise HTTPException(status_code=404, detail="Stock or benchmark data not found")

        # Get latest closing prices
        stock_price = stock["Close"].iloc[-1]
        benchmark_price = benchmark["Close"].iloc[-1]

        # Calculate Relative Strength (RS)
        relative_strength = stock_price / benchmark_price

        return {
            "stock": stock_symbol,
            "benchmark": benchmark_symbol,
            "stock_price": round(stock_price, 2),
            "benchmark_price": round(benchmark_price, 2),
            "relative_strength": round(relative_strength, 4)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))