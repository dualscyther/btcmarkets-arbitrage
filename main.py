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

tickers = ['ETH', 'BCH', 'LTC', 'ETC', 'XRP']
pairs = []
for ticker in tickers:
  pairs.append((ticker, 'AUD'))
  pairs.append((ticker, 'BTC'))
# Add special pair
pairs.append(('BTC', 'AUD'))

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
  # print(result['bestBid'])
  # print(result['bestAsk'])

  rates[pair[0]][pair[1]] = result['bestBid']
  rates[pair[1]][pair[0]] = 1/result['bestAsk']

# print(rates)


cycles_percentages = []

# For AUD to ticker to BTC to AUD (and vice versa)
for ticker in tickers:
  start = 1
  cur = start
  cur = (cur * (1-fiat_fee)) * rates['AUD'][ticker]
  cur = (cur * (1-crypto_fee)) * rates[ticker]['BTC']
  cur = (cur * (1-fiat_fee)) * rates['BTC']['AUD']
  print "%.4f AUD to %s to BTC to AUD" % (cur, ticker)
  if cur > 1:
    print rates

  cur = start
  cur = (cur * (1-fiat_fee)) * rates['AUD']['BTC']
  cur = (cur * (1-crypto_fee)) * rates['BTC'][ticker]
  cur = (cur * (1-fiat_fee)) * rates[ticker]['AUD']
  print "%.4f AUD to BTC to %s to AUD" % (cur, ticker)
  if cur > 1:
    print rates

# For AUD to ticker to BTC to ticker2 to AUD
for t1 in tickers:
  for t2 in tickers:
    start = 1

    cur = start
    cur = (cur * (1-fiat_fee)) * rates['AUD'][t1]
    cur = (cur * (1-crypto_fee)) * rates[t1]['BTC']
    cur = (cur * (1-crypto_fee)) * rates['BTC'][t2]
    cur = (cur * (1-fiat_fee)) * rates[t2]['AUD']
    print "%.4f AUD to %s to BTC to %s to AUD" % (cur, t1, t2)
    if cur > 1:
      print rates
