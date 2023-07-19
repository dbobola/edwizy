from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager


api_key = "iQvgalKKnf5mG4iQZJrwi0lE2h5FA1w9SQbqETANDlSHBtqeuN24uVcvCrdPkhBi"
api_secret = "xLSVhqqcXWENRZ5qeIXIVFAKrutTfX2a3KPeC0RnZCxP37JC2Fn2UQ4zVQka1BIb"
client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

# place a test market buy order, to place an actual order use the create_order function
order = client.create_test_order(
    symbol='BNBBTC',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=100)

def try_binance(): 
    # get all symbol prices
    prices = client.get_all_tickers()
    print(prices)