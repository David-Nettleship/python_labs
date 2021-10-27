import subprocess
import sys
import json

#subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
#sys.path.append('/tmp')
import yfinance as yf

#get open, close


def lambda_handler(event, context):
    companies = ["FB", "MSFT", "REL.L", "BTC-GBP"]
    for company in companies:
        company_ticker = yf.Ticker(company)
        hist = company_ticker.history(period="1d")

        for index, row in hist.iterrows():
            dat = {"open":row["Open"], "close":row["Close"], "ticker":company}
            print(dat)

        #for index, row in hist.iterrows():
            #dic = {"open":row["Open"], "close":row["Close"], "ts":index.strftime('%Y-%m-%d %X'), "name":company}
            #as_jsonstr = json.dumps(dic)
            #print(as_jsonstr)

    return {
    'statusCode': 200,
    'body': json.dumps('Done!')
    }

event = 0
context = 0
lambda_handler(event,context)