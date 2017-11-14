# Simple arbitrage detector based on the API below
Just run run.sh


BTC Markets python client
=================

A client implementation of [BTC Markets trading and account management API] (https://github.com/BTCMarkets/API) in python.


Example Usage

-----

```
client = BTCMarkets ('api key', 'private key') 
print client.account_balance()
```

TODO list:
* error handeling for http request, input parameter and json encoding of response
* support for http get query string
 

