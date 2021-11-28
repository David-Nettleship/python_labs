import yfinance as yf

company = 'MSFT'

ticker = yf.Ticker(company)
info = ticker.info
print(info)
print(type(info))

#print(ticker.cashflow)
#print(ticker.earnings)

for i in info:
    print(str(i) + " " + " " + str(info[i]))
    #forwardPE  31.308641
    #trailingPE  36.88108