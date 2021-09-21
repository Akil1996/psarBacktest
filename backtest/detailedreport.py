from .commanfun import historical_data
from .commanfun import atr, volatility_measure
import talib


def psar_strategy(df):
    signalStatus = ""
    result_dic = []
    for index, row in df.iterrows():
        if row.close > row.SAR:
            result_dic.append({"dtime": index, "open": row.open, "high": row.high, "low": row.low, "close": row.close, "psarValue": round(row.SAR, 2), "indVolatility": row.ATR, "volatility": row.Volatility, "signal": "BUY"})
        if row.close < row.SAR:
            result_dic.append({"dtime": index, "open": row.open, "high": row.high, "low": row.low, "close": row.close, "psarValue": round(row.SAR, 2), "indVolatility": row.ATR, "volatility": row.Volatility, "signal": "SELL"})
    return result_dic


def dreport_main(stockName, psarStart, psarIncrement, psarMaxvalue, timeFrame, fromDate, toDate, pIncrement, pMaxvalue):
    df = historical_data(timeFrame, fromDate, toDate)
    df['SAR'] = talib.SAR(df.high, df.low, acceleration=pIncrement, maximum=pMaxvalue)
    df = atr(df, 14)
    df = volatility_measure(df)
    result_df = psar_strategy(df)
    return result_df
