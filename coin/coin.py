import cbpro


def get_gbp_pairs(client):
    result = client.get_products()
    for r in result:
        if 'GBP' in r['id']: 
            print(r['id'])


client = cbpro.PublicClient()

get_gbp_pairs(client)

fifteen = client.get_product_historic_rates('BTC-USD', granularity=900)

for s in fifteen:
    print(s)
