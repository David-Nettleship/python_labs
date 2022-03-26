import requests

gm_to_oz = 31.1034768

au_gm = 10
au_oz = 0.25

ag_gm = 0
ag_oz  = 1

metals = ['XAU',"XAG"]


def au_weight_to_value(au_gm, au_oz):
    pass


# Get current price of metal in GBP
def api_call(base):

    symbol = 'GBP' 
    endpoint = 'latest'
    access_key = ''

    resp = requests.get(
        'https://www.metals-api.com/api/'+endpoint+'?access_key='+access_key+'&base='+base+'&symbols='+symbol)

    resp = resp.json()
    price = round(resp['rates']['GBP'],2)

    return price


def main():

    resp = {u'success': True, u'timestamp': 1648233780, u'base': u'XAU', u'rates': {u'GBP': 1480.1329326254915}, u'date': u'2022-03-25', u'unit': u'per ounce'}
    print(resp)
    print(round(resp['rates']['GBP'],2))



    #for base in metals:
        #resp = api_call(base)

        #print(base)
        #print(resp.keys())
        #print(resp)

main()