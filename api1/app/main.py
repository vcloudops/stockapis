from fastapi import FastAPI
import yfinance as yf
import unittest

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to NIFTY 50 Stock API"}

@app.get("/nifty50")
def get_nifty50():
    """Fetches stock prices for NIFTY 50 stocks"""
    nifty50_stocks = [
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
    stock_data = {}

    for stock in nifty50_stocks:
        ticker = yf.Ticker(stock)
        data = ticker.history(period="1d")
        if not data.empty:
            stock_data[stock] = {
                "price": round(data["Close"].iloc[-1], 2),
                "volume": int(data["Volume"].iloc[-1]),
                "open": round(data["Open"].iloc[-1], 2),
                "high": round(data["High"].iloc[-1], 2),
                "low": round(data["Low"].iloc[-1], 2)
            }

    return stock_data


# Unit Test Cases
class TestStockAPI(unittest.TestCase):

    def setUp(self):
        """Set up a test client"""
        from fastapi.testclient import TestClient
        self.client = TestClient(app)

    def test_read_root(self):
        """Test root endpoint"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to NIFTY 50 Stock API"})

    def test_get_nifty50(self):
        """Test stock data API"""
        response = self.client.get("/nifty50")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertGreater(len(response.json()), 0)

        for stock, data in response.json().items():
            self.assertIn("price", data)
            self.assertIn("volume", data)
            self.assertIsInstance(data["price"], (int, float))
            self.assertIsInstance(data["volume"], int)

# Run tests if the script is executed directly
if __name__ == "__main__":
    unittest.main()