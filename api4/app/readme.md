api name: Relative Strength (RS) of a stock

purpose: 

        Relative Strength (RS) of a stock, compare a stock’s performance against a benchmark index (e.g., NIFTY 50).

Dependecies:
        
        fastapi 
        uvicorn 
        yfinance 
        pandas
        
usage:
        Accepts:
                NIFTY index symbol (e.g., ^NSEI for NIFTY 50, ^NSEBANK for NIFTY Bank).
                stock_symbol (RELIANCE.NS, ZOMATO.NS)
        Fetches latest closing prices for the stock and benchmark index.
        Calculates Relative Strength (RS):
                                        Stock Closing Price Today 
                                RS =   ------------------------
                                        Benchmark Closing Price Today
        Returns the Relative Strength value.

        Test the API:

            http://localhost:8000/stock-rs?stock_symbol=RELIANCE.NS&benchmark_symbol=^NSEI

        Alternate Indices:
        
            NIFTY 50        -   ^NSEI
            NIFTY Bank      - 	^NSEBANK
            NIFTY IT        -   ^CNXIT
            NIFTY Pharma    -   ^CNXPHARMA