api name: Relative Strength Index (RSI) for a stock

purpose: 
        The Relative Strength Index (RSI) is a momentum indicator that measures the strength and speed of a stock’s price movement.
            RSI =   100   −         (   100   )
                                        ----
                                        1 + RS
            Where:
                    RS  =   Average Gain over n periods
​                           -----------------------------
                            Average Loss over n periods
        RSI Value Range:
            Above 70: Overbought (may indicate a price drop)
            Below 30: Oversold (may indicate a price rise)
        Default n Period: 14 days (most commonly used)

Dependecies:
        fastapi 
        uvicorn 
        yfinance 
        pandas
        
usage:
        Accepts:

        Fetches historical stock data from Yahoo Finance (yfinance).
        Calculates daily price changes (delta).
        Separates gains & losses and computes average gains & losses.
        Computes Relative Strength (RS) and RSI.
        Returns the RSI value (0-100).
        Test the API
            http://localhost:8000/stock-rsi?stock_symbol=RELIANCE.NS&period=14
        Alternate Get RSI for Nifty 50 Index
            http://localhost:8000/stock-rsi?stock_symbol=^NSEI&period=14