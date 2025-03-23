# Index Growth API

## 📌 Overview
The **Index Growth API** is a **FastAPI-based service** that fetches and calculates the **NIFTY index growth** over a given period using **Yahoo Finance**. It allows users to:
- Fetch **historical closing prices** of NIFTY 50 or other indices.
- Compute **percentage growth** over a specified period (**e.g., 7 days, 30 days, 90 days**).
- Return **growth rate in JSON format**.

---

## 🛠 Dependencies
To run this API, install the following packages:
```bash
pip install fastapi uvicorn yfinance pandas
```

---

## 🚀 Usage
### ✅ **Accepted Parameters**
- `index_symbol`: Symbol for the desired index (**e.g., ^NSEI for NIFTY 50, ^NSEBANK for NIFTY Bank**).
- `period`: Time period for growth calculation (**e.g., 7d, 30d, 90d, 180d**).

### ✅ **How It Works**
1. Fetches **historical closing prices** of the selected index.
2. Computes **percentage growth** over the given period.
3. Returns the **growth rate in JSON format**.

### ✅ **Example API Request**
```http
GET http://localhost:8000/nifty-growth?index_symbol=^NSEI&period=30d
```

**Example Response:**
```json
{
    "index": "NIFTY 50",
    "start_price": 17500.30,
    "end_price": 18250.75,
    "growth_percentage": 4.29,
    "period": "30d"
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
- 📈 **Graphical Trends for Index Growth**.
- 📊 **Support for Multiple Indices in a Single Request**.
- 🔔 **Growth Rate Notifications & Alerts**.

---

## 🤝 Contributing
Pull requests are welcome! If you'd like to contribute, feel free to submit issues or PRs.

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

### 🚀 **Would you like to add Docker & CI/CD integration?**
