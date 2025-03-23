api name: Rate of Change (ROC) of a stock

purpose: 
       The Rate of Change (ROC) is a momentum indicator that measures the percentage change in stock price over a given period. It is calculated as:

                    (Pcurrent − Pn days ago)
            ROC =   ------------------------ * 100
                        Pn days ago

            Where:
                    𝑃current    = Latest stock price
                    𝑃n days ago = Stock price n days ago
                    n           = Period (e.g., 10 days, 14 days)
Dependecies:
        fastapi 
        uvicorn 
        yfinance 
        pandas
        
usage:
        Accepts:

        Fetches historical stock data from Yahoo Finance.
        Extracts closing prices over the last n days.
        Calculates Rate of Change (ROC) using the formula.
        Returns the ROC in percentage along with the stock prices.
        Test the API
            http://localhost:8000/stock-roc?stock_symbol=RELIANCE.NS&period=10
        Alternate Get ROC for Nifty 50 Index
            http://localhost:8000/stock-roc?stock_symbol=^NSEI&period=10
