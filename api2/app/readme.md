# Rate of Change (ROC) API

## 📌 Overview
The **Rate of Change (ROC) API** is a **FastAPI-based service** that calculates the **momentum indicator** of a stock’s percentage change over a specified period. It allows users to:
- Fetch **historical stock data** from Yahoo Finance.
- Compute **ROC using the standard formula**:

  \[ ROC = \frac{P_{current} - P_{n\ days\ ago}}{P_{n\ days\ ago}} \times 100 \]
  
  Where:
  - **Pcurrent** = Latest stock price
  - **Pn days ago** = Stock price `n` days ago
  - **n** = Period (e.g., 10 days, 14 days, 50 days)

- Return the **ROC value in percentage** along with stock prices.

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
- `period`: Time period for ROC calculation (**e.g., 10, 14, 50**).

### ✅ **How It Works**
1. Fetches **historical stock prices**.
2. Extracts **closing prices over the last `n` days**.
3. Computes **Rate of Change (ROC) using the given formula**.
4. Returns the **ROC value in percentage**.

### ✅ **Example API Request**
```http
GET http://localhost:8000/stock-roc?stock_symbol=RELIANCE.NS&period=10
```

**Example Response:**
```json
{
    "stock": "RELIANCE.NS",
    "period": 10,
    "current_price": 2800.50,
    "price_10_days_ago": 2700.75,
    "rate_of_change": 3.69
}
```

---

## 📊 Get ROC for Nifty 50 Index
```http
GET http://localhost:8000/stock-roc?stock_symbol=^NSEI&period=10
```

---

## 🏗 Built With
- **FastAPI** - Web framework for building APIs.
- **Yahoo Finance (`yfinance`)** - Fetches real-time stock & index prices.
- **Uvicorn** - ASGI server to run FastAPI.

---

## 📌 Future Enhancements
- 📈 **Graphical Representation of ROC Trends**.
- 📊 **Real-time ROC Alerts**.
- 🔔 **Multi-Stock ROC Comparison**.

---

## 🤝 Contributing
Pull requests are welcome! If you'd like to contribute, feel free to submit issues or PRs.

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

