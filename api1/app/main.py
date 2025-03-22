from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

# List of NIFTY 50 stock symbols (NSE India)
NIFTY_50_SYMBOLS = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "HINDUNILVR.NS", "HDFC.NS", "BHARTIARTL.NS", "KOTAKBANK.NS", "SBIN.NS",
    "LT.NS", "ITC.NS", "ASIANPAINT.NS", "AXISBANK.NS", "MARUTI.NS",
    "SUNPHARMA.NS", "TITAN.NS", "BAJFINANCE.NS", "WIPRO.NS", "HCLTECH.NS",
    "ULTRACEMCO.NS", "TECHM.NS", "ONGC.NS", "TATASTEEL.NS", "NESTLEIND.NS",
    "POWERGRID.NS", "JSWSTEEL.NS", "BAJAJFINSV.NS", "COALINDIA.NS", "ADANIENT.NS",
    "GRASIM.NS", "HEROMOTOCO.NS", "INDUSINDBK.NS", "BPCL.NS", "DIVISLAB.NS",
    "BRITANNIA.NS", "HDFCLIFE.NS", "CIPLA.NS", "EICHERMOT.NS", "BAJAJ-AUTO.NS",
    "DRREDDY.NS", "APOLLOHOSP.NS", "TATACONSUM.NS", "HINDALCO.NS", "M&M.NS",
    "SBILIFE.NS", "NTPC.NS", "UPL.NS", "IOC.NS", "SHREECEM.NS"
]

@app.get("/")
def home():
    return {"message": "Welcome to NIFTY 50 Stock API"}

@app.get("/nifty50")
def get_nifty50_data():
    stocks_data = []

    for symbol in NIFTY_50_SYMBOLS:
        try:
            stock = yf.Ticker(symbol)
            data = stock.history(period="1d")
            
            if not data.empty:
                stocks_data.append({
                    "symbol": symbol,
                    "price": round(data["Close"].iloc[-1], 2),
                    "volume": int(data["Volume"].iloc[-1]),
                    "open": round(data["Open"].iloc[-1], 2),
                    "high": round(data["High"].iloc[-1], 2),
                    "low": round(data["Low"].iloc[-1], 2)
                })
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")

    return {"nifty50": stocks_data}

# Run the API with:
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload