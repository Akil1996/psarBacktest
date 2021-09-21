from twelvedata import TDClient
import numpy as np
td = TDClient(apikey="f2ddcd6e25d34a479b06a0314934717b")

def historical_data(timeFrame, fromDate, toDate):
    if timeFrame == "minute":
        ts = td.time_series(
        symbol="ARKK",
        interval="1min",
        outputsize=5000,
        timezone="America/New_York",
        start_date= fromDate,
        end_date= toDate,
        )
        df = ts.as_pandas()
        df = df.iloc[::-1]
        return df
    if timeFrame == "5minute":
        ts = td.time_series(
        symbol="ARKK",
        interval="5min",
        outputsize=5000,
        timezone="America/New_York",
        start_date= fromDate,
        end_date= toDate,
        )
        df = ts.as_pandas()
        df = df.iloc[::-1]
        return df
    if timeFrame == "15minute":
        ts = td.time_series(
        symbol="ARKK",
        interval="15min",
        outputsize=5000,
        timezone="America/New_York",
        start_date= fromDate,
        end_date= toDate,
        )
        df = ts.as_pandas()
        df = df.iloc[::-1]
        return df
    if timeFrame == "1 hour":
        ts = td.time_series(
        symbol="ARKK",
        interval="1h",
        outputsize=5000,
        timezone="America/New_York",
        start_date= fromDate,
        end_date= toDate,
        )
        df = ts.as_pandas()
        df = df.iloc[::-1]
        return df
    if timeFrame == "2 hour":
        ts = td.time_series(
        symbol="ARKK",
        interval="2h",
        outputsize=5000,
        timezone="America/New_York",
        start_date= fromDate,
        end_date= toDate,
        )
        df = ts.as_pandas()
        df = df.iloc[::-1]
        return df
    if timeFrame == "4 hour":
        ts = td.time_series(
        symbol="ARKK",
        interval="4h",
        outputsize=5000,
        timezone="America/New_York",
        start_date= fromDate,
        end_date= toDate,
        )
        df = ts.as_pandas()
        df = df.iloc[::-1]
        return df
    if timeFrame == "day":
        ts = td.time_series(
        symbol="ARKK",
        interval="1day",
        outputsize=5000,
        timezone="America/New_York",
        start_date= fromDate,
        end_date= toDate,
        )
        df = ts.as_pandas()
        df = df.iloc[::-1]
        return df
    if timeFrame == "week":
        ts = td.time_series(
        symbol="ARKK",
        interval="1week",
        outputsize=5000,
        timezone="America/New_York",
        start_date= fromDate,
        end_date= toDate,
        )
        df = ts.as_pandas()
        df = df.iloc[::-1]
        return df   
    if timeFrame == "month":
        ts = td.time_series(
        symbol="ARKK",
        interval="1month",
        outputsize=5000,
        timezone="America/New_York",
        start_date= fromDate,
        end_date= toDate,
        )
        df = ts.as_pandas()
        df = df.iloc[::-1]
        return df   
    pass




def atr(DF, n):
    df = DF.copy()
    df['H-L'] = abs(df['high'] - df['low'])
    df['H-PC'] = abs(df['high'] - df['close'].shift(1))
    df['L-PC'] = abs(df['low'] - df['close'].shift(1))
    df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1, skipna=False)
    df['ATR'] = df['TR'].ewm(com=n, min_periods=n).mean()
    df['ATR'] = df['ATR'].fillna(0)
    return df




def volatility_measure(NIFTY):
    # Compute the logarithmic returns using the Closing price 
    NIFTY['Log_Ret'] = np.log(NIFTY['close'] / NIFTY['close'].shift(1))

    # Compute Volatility using the pandas rolling standard deviation function
    NIFTY['Volatility'] = NIFTY['Log_Ret'].rolling(window=252).std() * np.sqrt(252)
    NIFTY['Volatility'] = NIFTY['Volatility'].fillna(0)
    return NIFTY
