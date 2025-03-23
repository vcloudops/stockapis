# Relative Strength Index (RSI) API

## 📌 Overview
The **Relative Strength Index (RSI) API** is a **FastAPI-based service** that calculates the **momentum indicator** of a stock’s price movement. It allows users to:
- Fetch **historical stock data** from Yahoo Finance.
- Compute **RSI using the standard formula**:

  \[ RSI = 100 - \frac{100}{1 + RS} \]
  
  Where:
  \[ RS = \frac{\text{Average Gain over n periods}}{\text{Average Loss over n periods}} \]

- Return the **RSI value (0-100)** in JSON format.

### 📊 **RSI Interpretation**
- **Above 70**: Overbought (**Possible Price Drop**)
- **Below 30**: Oversold (**Possible Price Rise**)
- **Default Period (n): 14 Days** (Most commonly used)

---

## 🛠 Dependencies
To run this API, install the following packages:
```bash
pip install fastapi uvicorn yfinance pandas
```

---

## 🚀 Usage
### ✅ **Accepted Parameters**
- `stock_symbol`: Stock ticker symbol (**e.g., RELIANCE.NS, ZOMATO.NS**).
- `period`: Time period for RSI calculation (**e.g., 14, 50**).

### ✅ **How It Works**
1. Fetches **historical stock prices**.
2. Calculates **daily price changes (delta)**.
3. Separates **gains & losses**, then computes average values.
4. Computes **Relative Strength (RS) and RSI**.
5. Returns the **RSI value (0-100)** in JSON format.

### ✅ **Example API Request**
```http
GET http://localhost:8000/stock-rsi?stock_symbol=RELIANCE.NS&period=14
```

**Example Response:**
```json
{
    "stock": "RELIANCE.NS",
    "period": 14,
    "rsi": 65.42
}
```

---

## 📊 Get RSI for Nifty 50 Index
```http
GET http://localhost:8000/stock-rsi?stock_symbol=^NSEI&period=14
```

---

## 🏗 Built With
- **FastAPI** - Web framework for building APIs.
- **Yahoo Finance (`yfinance`)** - Fetches real-time stock & index prices.
- **Uvicorn** - ASGI server to run FastAPI.

---

## 📌 Future Enhancements
- 📈 **Graphical Representation of RSI Trends**.
- 📊 **Real-time RSI Alerts**.
- 🔔 **Multi-Stock RSI Comparison**.

---

## 🤝 Contributing
Pull requests are welcome! If you'd like to contribute, feel free to submit issues or PRs.

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---