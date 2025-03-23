API Name: Index growth

Purpose:

        FastAPI-based API to fetch and calculate the NIFTY index growth over a given period using Yahoo Finance
        Fetch historical closing prices of NIFTY 50 or other indices.
        Compute percentage growth over a custom period (e.g., 7 days, 30 days, 90 days).
        Return growth rate in JSON format.

Dependecies:

        fastapi 
        uvicorn 
        yfinance 
        pandas
        
Usage:
        Accepts:
            
        NIFTY index symbol (e.g., ^NSEI for NIFTY 50, ^NSEBANK for NIFTY Bank).
        Custom period (e.g., 7d, 30d, 90d, 180d).
        
        Fetches historical closing prices.
        Computes percentage growth.
        Returns growth rate in JSON.
        
        Test the API:

            http://localhost:8000/nifty-growth?index_symbol=^NSEI&period=30d
        
        Alternate Indices:

            NIFTY 50        -   ^NSEI
            NIFTY Bank      - 	^NSEBANK
            NIFTY IT        -   ^CNXIT
            NIFTY Pharma    -   ^CNXPHARMA