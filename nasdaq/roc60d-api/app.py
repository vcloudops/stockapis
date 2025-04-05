import os
import yfinance as yf
import pandas as pd
from flask import Flask, jsonify

# Flask App
app = Flask(__name__)

# List of NASDAQ-100 stock tickers (shortened for demo)
NASDAQ_TICKERS = [
    "AAPL", "MSFT", "NVDA", "AMZN", "TSLA", "META", "GOOGL", "GOOG", "AVGO", "COST",
    "PEP", "AMD", "NFLX", "ADP", "ADBE", "INTC", "CSCO", "HON", "AMGN", "QCOM",
    "INTU", "TXN", "SBUX", "GILD", "LRCX", "BKNG", "PYPL", "ABNB", "AMAT", "NOW",
    "MRVL", "ISRG", "PANW", "REGN", "ADI", "KDP", "ORLY", "CDNS", "KLAC", "MDT",
    "MCHP", "SNPS", "MAR", "CHTR", "MU", "DXCM", "PDD", "FTNT", "CRWD", "IDXX",
    "VRTX", "WDAY", "LULU", "EXC", "MNST", "FISV", "TCOM", "XEL", "PCAR", "ROST",
    "AZN", "EBAY", "ILMN", "MRNA", "NXPI", "CTAS", "AEP", "ODFL", "PAYX", "MELI",
    "GEHC", "CPRT", "KHC", "SIRI", "BIDU", "CSGP", "VRSK", "EA", "NTES", "CHKP",
    "FAST", "ANSS", "CDW", "SPLK", "DELL", "DXCM", "WST", "ALGN", "SWKS", "ZS",
    "CEG", "MPWR", "OKTA", "MTCH", "DDOG", "SEDG", "GFS", "ZM", "TEAM", "LPLA",
    "BIIB", "DOCU", "VRSN", "PTC", "PAYC", "MRNA", "TSCO"
  ]

def fetch_stock_prices(ticker, days=60):
    """Fetch historical stock prices from Yahoo Finance"""
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=f"{days+1}d")
        return data["Close"]
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def calculate_roc(ticker, days=60):
    """Calculate Rate of Change (ROC)"""
    prices = fetch_stock_prices(ticker, days)
    if prices is None or len(prices) < days + 1:
        return None

    recent_close = prices.iloc[-1]
    past_close = prices.iloc[0]
    roc = ((recent_close - past_close) / past_close) * 100
    return roc

@app.route('/roc60d', methods=['GET'])
def fetch_roc():
    """API Endpoint to fetch ROC for NASDAQ-100 stocks"""
    try:
        roc_data = {}
        for symbol in NASDAQ_TICKERS:
            roc = calculate_roc(symbol, days=60)
            if roc is not None:
                roc_data[symbol] = roc

        return jsonify({"ROC": roc_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
