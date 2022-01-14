import requests
import re
import json
from bs4 import BeautifulSoup

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#https://stackoverflow.com/questions/68259148/getting-404-error-for-certain-stocks-and-pages-on-yahoo-finance-python

ticker = 'MSFT'
url = "https://finance.yahoo.com/quote/" + ticker + "/financials?p=" + ticker
page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

pattern = re.compile(r'\s--\sData\s--\s')
data = soup.find('script', text=pattern).contents[0]
start = data.find("context")-2
json_data = json.loads(data[start:-12])
income_stmt = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']#.keys()
print(income_stmt)
for i in income_stmt:
    print(i)
    #print("\n" + str(i))
exit()

print(data)
#tabl = soup.find_all("div", {"class" : "D(tbrg)"})
#print([tabl.attrs['data-test'] for t in tabl])

# print(type(page))
# print(page)
# print(type(tabl))
# print(tabl)