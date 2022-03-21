import yfinance as yf
import numpy as np

tickers = ["AMZN","FB","INTC"]
data = {}

for stock in tickers:
    df = yf.download(stock,period='1mo',interval='15m')
    df.dropna(how="any",inplace=True)
    data[stock] = df
    
#RSI
def RSI(df, n=14):
    df = df.copy()
    df["change"] = df["Adj Close"] - df["Adj Close"].shift(1)
    df["gain"] = np.where(df["change"]>=0,df["change"],0)
    df["loss"] = np.where(df["change"]<0,-1*df["change"],0)
    df["avgGain"] = df["gain"].ewm(alpha=1/n, min_periods=n).mean()
    df["avgLoss"] = df["loss"].ewm(alpha=1/n, min_periods=n).mean()
    df["rs"] = df["avgGain"]/df["avgLoss"]
    df["rsi"] = 100 - (100/(1+df["rs"]))
    return df["rsi"]

for stock in data:
    data[stock]["RSI"] = RSI(data[stock])
    
amzn = data["AMZN"]
fb = data["FB"]

fb['RSI'].plot()