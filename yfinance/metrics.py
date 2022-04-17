import yfinance as yf


t = yf.Ticker('AMZN')
fin = t.financials
balancesheet = t.balance_sheet
earnings = t.earnings
info = t.info
cashflow = t.cashflow

prices = t.history(period="5y", interval="1d")['Close']
#prices.plot()

def revenue(earnings):
    
    rev = earnings['Revenue']
    years = list(rev.keys())
    
    revdelta = round(((rev.iloc[-1]-rev.iloc[0])/rev.iloc[0])*100,2)
    
    i=0
    data = []
    
    while i <len(years):
        data.append({"Year":years[i], "Revenue":rev.iloc[i]})
        i = i+1
    data.append({str(len(years)) + " Year Revenue Change %": revdelta})
    
    return data


def fcf(cashflow):

    tc = cashflow.loc['Total Cash From Operating Activities'].to_dict()
    te = cashflow.loc['Capital Expenditures'].to_dict()
    
    years = []
    cash = []
    
    for key, value in tc.items():
        cash.append(value)
        #TODO
        years.append(key) #append only year, remove Timestamp

    expenditures = [value for key, value in te.items()]
        
    data = zip(years,cash,expenditures)
        
    return list(data)


def dividend(info):
    
    div = info['dividendYield']
    avgdiv = info['fiveYearAvgDividendYield']
    
    if div is None:
        return {"Dividend Yield": 0, "5yr Average Dividend Yield": 0}
    else:
        return {"Dividend Yield":round(div*100,2),"5yr Average Dividend Yield":round(avgdiv,2)}


def cagr5yr(prices):
    # CAGR https://www.investopedia.com/terms/c/cagr.asp
    return round(((prices.iloc[-1]/prices.iloc[0])**(1/5)-1)*100,2)


def shares():
    pass


def debt():
    pass


print(dividend(info))
#print(revenue(earnings))
#print(fcf(cashflow))
#print(cagr5yr(prices))

#liab = balancesheet.loc['Total Current Liabilities']
