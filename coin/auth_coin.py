import cbpro

public = ''
passphrase = ''
secret = ''

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)

#print(auth_client.get_accounts())

print(auth_client.buy(price="10.0", size="0.1", order_type="limit", product_id="ETH-GBP"))
print(auth_client.buy(size="0.1", order_type="market", product_id="ETH-GBP"))
print(auth_client.sell(size="0.1", order_type="market", product_id="ETH-GBP"))
