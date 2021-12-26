import yfinance as yf
import numpy as np

#VARS
funds = 1000
fee = 0.5
orders = []


ticker = yf.Ticker('BTC-GBP')
hist = ticker.history(period="1wk", interval = "15m")

def rsi_calc(data):
    data["change"] = data["Close"] - data["Close"].shift(1)
    data["gain"] = np.where(data["change"]>=0,data["change"],0)
    data["loss"] = np.where(data["change"]<0,-1*data["change"],0)
    data["avg_gain"] = data["gain"].ewm(alpha=1/12, min_periods=12).mean()
    data["avg_loss"] = data["loss"].ewm(alpha=1/12, min_periods=12).mean()
    data["rs"] = data["avg_gain"]/data["avg_loss"]
    data["rsi"] = 100 - (100 / (1+data["rs"]))
    print(data)
    return round(data["rsi"].iloc[-1],2)


def buy(funds):
    funds = funds-100


def main():
    ticker = yf.Ticker('BTC-GBP')
    hist = ticker.history(period="1d", interval = "15m")
    rsi = rsi_calc(hist)

    if rsi > 70 and len(orders) > 0:
        print("SELL SELL SELL!")
    else:
        print("RSI = " + str(rsi) + " Sitting tight...")

    if rsi < 30 and funds > 100:
        print("BUY BUY BUY!")
        buy(funds)
    elif funds < 100:
        print("Insufficient Funds!")
    else:
        print("RSI = " + str(rsi) + " Sitting tight...")


main()
