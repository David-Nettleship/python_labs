import yfinance as yf

tickers = ["AMZN","FB","INTC","MSFT"]
data = {}

for stock in tickers:
    df = yf.download(stock,period='1mo',interval='15m')
    df.dropna(how="any",inplace=True)
    data[stock] = df

#MACD
def macd(df,a=12,b=26,c=9):
    df = df.copy()
    df["ma_fast"] = df["Adj Close"].ewm(span=a).mean()





intc = data['INTC']