# Relative Strength (RS) API

## 📌 Overview
The **Relative Strength (RS) API** is a **FastAPI-based service** that compares a stock’s performance against a benchmark index (e.g., **NIFTY 50**). It allows users to:
- Fetch the **latest closing prices** of a stock and a benchmark index.
- Compute the **Relative Strength (RS)** using the formula:

  \[ RS = \frac{\text{Stock Closing Price Today}}{\text{Benchmark Closing Price Today}} \]
  
- Return the **Relative Strength value** in JSON format.

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
- `benchmark_symbol`: Index symbol (**e.g., ^NSEI for NIFTY 50, ^NSEBANK for NIFTY Bank**).

### ✅ **How It Works**
1. Fetches **latest closing prices** for the stock and the benchmark index.
2. Computes the **Relative Strength (RS)** using the given formula.
3. Returns the **Relative Strength value** in JSON format.

### ✅ **Example API Request**
```http
GET http://localhost:8000/stock-rs?stock_symbol=RELIANCE.NS&benchmark_symbol=^NSEI
```

**Example Response:**
```json
{
    "stock": "RELIANCE.NS",
    "benchmark": "NIFTY 50",
    "stock_price": 2700.50,
    "benchmark_price": 18500.75,
    "relative_strength": 0.1459
}
```

---

## 📊 Alternate Indices
| **Index Name**  | **Symbol**  |
|----------------|------------|
| NIFTY 50      | `^NSEI`     |
| NIFTY Bank    | `^NSEBANK`  |
| NIFTY IT      | `^CNXIT`    |
| NIFTY Pharma  | `^CNXPHARMA` |

---

## 🏗 Built With
- **FastAPI** - Web framework for building APIs.
- **Yahoo Finance (`yfinance`)** - Fetches real-time stock & index prices.
- **Uvicorn** - ASGI server to run FastAPI.

---

## 📌 Future Enhancements
- 📈 **Historical Relative Strength Calculation**.
- 📊 **Graphical Representation of RS Trends**.
- 🔔 **RS Alerts & Notifications**.

---

## 🤝 Contributing
Pull requests are welcome! If you'd like to contribute, feel free to submit issues or PRs.

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---
