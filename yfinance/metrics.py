import yfinance as yf


t = yf.Ticker('AMZN')
fin = t.financials
balancesheet = t.balance_sheet
earnings = t.earnings
info = t.info

prices = t.history(period="5y", interval="1d")['Close']

prices.plot()

rev = earnings['Revenue']

liab = balancesheet.loc['Total Current Liabilities']