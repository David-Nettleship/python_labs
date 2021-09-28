import requests as rq

api_key = ""

#get date 4 weeks ago, get change in addresses from then

req = rq.get("https://api.glassnode.com/v1/metrics/addresses/active_count?a=BTC&timestamp_format=humanized&i=1w&api_key=" + api_key)
for r in req:
    print(r)
