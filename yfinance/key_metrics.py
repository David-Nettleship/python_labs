import yfinance as yf
import json

#print(info)
#print(type(info))


def stock_issuance(ticker):
    try:
        print(ticker.cashflow.loc['Issuance Of Stock'])
    except:
        print("No issuance in surveyed period.")

def earnings(ticker):
    try:
        print(ticker.earnings)
    except:
        print("No earnings data!")

def historic_pe(ticker):
    #print(ticker.history(period="4y", interval="1mo"))
    print(ticker.financials)

#print(ticker.earnings)
#print(ticker.balancesheet)
#print(ticker.history(period="1mo", interval="1d"))

# for i in info:
#     print(str(i) + " " + " " + str(info[i]))
#     #forwardPE  31.308641
#     #trailingPE  36.88108

# Metrics
#   4yr PE
#   4yr Return on Capital
# ticker.earnings
##   4yr Revenue
##   4yr Profit
#   4yr shares outstanding
#   long term liabilities/4yr Free cashflow
#   free cashflow/price

# FAAMG (MAAMG?)
tickers = ['FB','AAPL','AMZN','MSFT','GOOGL']
tickers = ['FB','MSFT']

#main
for t in tickers:
    print("Ticker: " + t)
    ticker = yf.Ticker(t)
    stats = (ticker.stats(proxy=None))
    # for s in stats:
    #     print("   " + s)
    #print(stats.get('financialData'))
    #print(ticker.balancesheet)

    stock_issuance(ticker)
    # earnings(ticker)
    #historic_pe(ticker)