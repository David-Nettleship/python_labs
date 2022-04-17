import yfinance as yf
import matplotlib.pyplot as plt


t = yf.Ticker('AMZN')
fin = t.financials
balancesheet = t.balance_sheet
earnings = t.earnings
info = t.info
cashflow = t.cashflow

prices = t.history(period="5y", interval="1d")['Close']
#prices.plot()


def revenue():
    rev = earnings['Revenue']
    years = list(rev.keys())

    # Visual
    plt.bar(years,rev,color='green')
    plt.xlabel("Year")
    plt.ylabel("Revenue")
    plt.title("Revenue last "+ str(len(years)) +" years")
    
    
    # CAGR https://www.investopedia.com/terms/c/cagr.asp
    cagr = round(((rev.iloc[-1]/rev.iloc[0])*pow(1, len(years))-1)*100,2)
    
    i=0
    data = []
    
    while i <len(years):
        data.append({"Year":years[i], "Revenue":rev.iloc[i]})
        i = i+1
    data.append({str(len(years)) + " Year Revenue CAGR": cagr})
    
    return data


def fcf():
    
    tc = cashflow.loc['Total Cash From Operating Activities'].to_dict()
    te = cashflow.loc['Capital Expenditures'].to_dict()
    
    years = []
    cash = []
    
    for key, value in tc.items():
        cash.append(value)
        years.append(key)

    expenditures = [value for key, value in te.items()]
        
    zipped = zip(years,cash,expenditures)
        
    return list(zipped)



print(revenue())
print(fcf())

#liab = balancesheet.loc['Total Current Liabilities']
