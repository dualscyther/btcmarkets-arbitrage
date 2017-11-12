from btcmarkets import BTCMarkets 

import config

api_key = config.api_key
private_key = config.private_key

client = BTCMarkets (api_key, private_key) 

#print client.trade_history('AUD', 'BTC', 10, 1)

#print client.order_detail([1234, 213456])
 
#print client.order_create('AUD', 'LTC', 100000000, 100000000, 'Bid', 'Limit', '1')

fiat_fee = 0.007
crypto_fee = 0.0022

pairs = (('ETH','AUD'), ('ETH', 'BTC'), ('BTC', 'AUD'))

# So prices['ETH']['AUD'] is the conversion rate from ETH to AUD
# So 1 ETH * prices['ETH']['AUD'] ~= 300
# prices = {'AUD': {}, 'ETH': {}, 'BTC': {}}
rates = {}
for pair in pairs:
  for ticker in pair:
    if ticker not in rates:
      rates[ticker] = {}

for pair in pairs:
  result = client.get_market_tick(pair[0], pair[1])
  print(result['bestBid'])
  print(result['bestAsk'])

  rates[pair[0]][pair[1]] = result['bestAsk']
  rates[pair[1]][pair[0]] = 1/result['bestBid']

print(rates)

# print client.get_market_tick('ETH','BTC')
# print client.get_market_tick('BTC','AUD')
