from .commanfun import historical_data, atr, volatility_measure
import talib

def psar_profitloss_strategy(df, fund):
    signal = None
    eTime = ""
    ePrice = 0
    result = []
    for index, row in df.iterrows():
        if row.close > row.SAR and signal != "BUY":
            if signal != None:
                pl = ePrice - row.close
                quantity = round(fund/row.close)
                dateDf = df.loc[str(eTime): str(index)]
                print(dateDf['low'].min())
                result.append({"entryTime": eTime, "exitTime": index, "entryPrice": ePrice, "exitPrice": row.close, "highLow": dateDf['low'].min(),"indVolatility": row.ATR, "volatility": row.Volatility, "signal": "SELL",  "profit": round((pl * quantity),2), "profitPercentage": str(round(((pl/row.close)*100),2)) + " %"})
            else:    
                pass
            signal = "BUY"
            eTime = index
            ePrice = row.close
        if row.close < row.SAR and signal != "SELL":
            if signal != None:
                quantity = round(fund/row.close)
                pl = row.close - ePrice 
                dateDf = df.loc[str(eTime): str(index)]
                result.append({"entryTime": eTime, "exitTime": index, "entryPrice": ePrice, "exitPrice": row.close, "highLow": dateDf['high'].max(), "indVolatility": row.ATR, "volatility": row.Volatility, "signal": "BUY", "profit": round((pl * quantity),2), "profitPercentage": str(round(((pl/row.close)*100),2)) + " %"})
            else:    
                pass
            signal = "SELL"
            eTime = index
            ePrice = row.close
    return result 
    

def plreport_main(stockName, psarStart, psarIncrement, psarMaxvalue, timeFrame, fromDate, toDate, fund, pIncrement, pMaxvalue):
    df = historical_data(timeFrame, fromDate, toDate)
    df['SAR'] = talib.SAR(df.high, df.low, acceleration=pIncrement, maximum=pMaxvalue)
    df = atr(df, 14)
    df = volatility_measure(df)
    df = psar_profitloss_strategy(df, fund)
    return df
