import requests
import certifi

from datetime import datetime
import requests
from alpaca.trading.client import TradingClient
from alpaca.data.live import CryptoDataStream, StockDataStream
from django.views.decorators.csrf import csrf_exempt
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
import csv
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
from datetime import datetime, timedelta


API_KEY = "PKZORLL65QU26JUJ7N0B"
SECRET_KEY = "QupmtRUUIh4hI0sd13tHQTgTes7t0UUXm0TFGXmU"
BASE_URL = "https://paper-api.alpaca.markets"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
crypto_stream = CryptoDataStream(API_KEY, SECRET_KEY)
stock_stream = StockDataStream(API_KEY, SECRET_KEY)
historical_client = CryptoHistoricalDataClient()

MAX_TOKENS= 3055
# Set the base URL for the Alpaca API
BASE_URL = "https://paper-api.alpaca.markets"


# Set the headers for the HTTP requests
headers = {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY,
    "Content-Type": "application/json",
    "Connection": "keep-alive"
}

def get_account(api_key, secret_key, base_url):
    url = f"{base_url}/v2/account"
    headers = {'APCA-API-KEY-ID': api_key, 'APCA-API-SECRET-KEY': secret_key}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get account details. Status code: {response.status_code}")
    
    
def get_orders(api_key, secret_key, base_url):
    url = f"{base_url}/v2/orders"
    headers = {'APCA-API-KEY-ID': api_key, 'APCA-API-SECRET-KEY': secret_key}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get orders. Status code: {response.status_code}")
def place_trade(api_key, secret_key, base_url, order_data):
    url = f"{base_url}/v2/orders"
    headers = {'APCA-API-KEY-ID': api_key, 'APCA-API-SECRET-KEY': secret_key}
    
    response = requests.post(url, headers=headers, json=order_data)
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Failed to place order. Status code: {response.status_code}")
def get_order(api_key, secret_key, base_url, order_id):
    url = f"{base_url}/v2/orders/{order_id}"
    headers = {'APCA-API-KEY-ID': api_key, 'APCA-API-SECRET-KEY': secret_key}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get order. Status code: {response.status_code}")
def get_positions(api_key, secret_key, base_url):
    url = f"{base_url}/v2/positions"
    headers = {'APCA-API-KEY-ID': api_key, 'APCA-API-SECRET-KEY': secret_key}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get positions. Status code: {response.status_code}")
def get_open_positions():
    response = requests.get("https://paper-api.alpaca.markets/v2/positions", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get open positions. Response: {response.text}")
def get_open_position_for_symbol(symbol):
    response = requests.get(f"https://paper-api.alpaca.markets/v2/positions/{symbol}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get open position for symbol {symbol}. Response: {response.text}")
def close_all_positions():
    response = requests.delete("https://paper-api.alpaca.markets/v2/positions", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to close all positions. Response: {response.text}")
def close_position_for_symbol(symbol):
    response = requests.delete(f"https://paper-api.alpaca.markets/v2/positions/{symbol}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to close position for symbol {symbol}. Response: {response.text}")

def get_asset(symbol_or_asset_id):
    response = requests.get(f"https://paper-api.alpaca.markets/v2/assets/{symbol_or_asset_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get asset {symbol_or_asset_id}. Response: {response.text}")
def get_watchlists():
    response = requests.get("https://paper-api.alpaca.markets/v2/watchlists", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get watchlists. Response: {response.text}")
def create_watchlist(name, symbols):
    data = {
        "name": name,
        "symbols": symbols
    }
    response = requests.post("https://paper-api.alpaca.markets/v2/watchlists", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to create watchlist. Response: {response.text}")
def get_watchlist(watchlist_id):
    response = requests.get(f"https://paper-api.alpaca.markets/v2/watchlists/{watchlist_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get watchlist {watchlist_id}. Response: {response.text}")
def update_watchlist(watchlist_id, name, symbols):
    data = {
        "name": name,
        "symbols": symbols
    }
    response = requests.put(f"https://paper-api.alpaca.markets/v2/watchlists/{watchlist_id}", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to update watchlist {watchlist_id}. Response: {response.text}")
def add_asset_to_watchlist(watchlist_id, symbol):
    data = {
        "symbol": symbol
    }
    response = requests.post(f"https://paper-api.alpaca.markets/v2/watchlists/{watchlist_id}", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to add asset to watchlist {watchlist_id}. Response: {response.text}")
def delete_watchlist(watchlist_id):
    response = requests.delete(f"https://paper-api.alpaca.markets/v2/watchlists/{watchlist_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to delete watchlist {watchlist_id}. Response: {response.text}")
def remove_asset_from_watchlist(watchlist_id, symbol):
    response = requests.delete(f"https://paper-api.alpaca.markets/v2/watchlists/{watchlist_id}/{symbol}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to remove asset from watchlist {watchlist_id}. Response: {response.text}")
def get_order(order_id):
    response = requests.get(f"https://paper-api.alpaca.markets/v2/orders/{order_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get order {order_id}. Response: {response.text}")


def get_alpaca_assets():
    response = requests.get("https://paper-api.alpaca.markets/v2/assets", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get assets. Response: {response.text}")
def alpaca_process_data(data, timeframe):
    m15_candles = []
    processed_data = []
    current_candle = None
    processed_data.append(["DateTime", "Price", "Open", "High", "Low"])

    if timeframe == '1M':
        interval = 1
    elif timeframe == '5M':
        interval = 5
    elif timeframe == '15M':
        interval = 15
    elif timeframe == '30M':
        interval = 30
    elif timeframe == '1H':
        interval = 1
    elif timeframe == '4H':
        interval = 4
    elif timeframe == '1D':
        interval = 1
    else:
        interval = 1
    
    
    for row in data:
        timestamp, open_price, high_price, low_price, close_price = row[0], row[1], row[2], row[3], row[4]
        timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        minute_timestamp_rounded = timestamp.replace(second=0, microsecond=0)
        hour_timestamp_rounded = timestamp.replace(minute=0, second=0, microsecond=0)
        day_timestamp_rounded = timestamp.replace(hour=0, minute=0, second=0, microsecond=0)
        
        if ('M' in timeframe) and (current_candle is None or minute_timestamp_rounded.minute % interval == 0):
            if current_candle is not None:
                m15_candles.append(current_candle)
            current_candle = [minute_timestamp_rounded, open_price, high_price, low_price, close_price]

        elif ('H' in timeframe) and (current_candle is None or hour_timestamp_rounded.hour % interval == 0):
            if current_candle is not None:
                m15_candles.append(current_candle)
            current_candle = [hour_timestamp_rounded, open_price, high_price, low_price, close_price]

        elif ('D' in timeframe) and (current_candle is None or day_timestamp_rounded.day % interval == 0):
            if current_candle is not None:
                m15_candles.append(current_candle)
                
            current_candle = [day_timestamp_rounded, open_price, high_price, low_price, close_price]

        else:
            current_candle[2] = max(current_candle[2], high_price)
            current_candle[3] = min(current_candle[3], low_price)
            current_candle[4] = close_price
    
    if current_candle is not None:
        m15_candles.append(current_candle)

    for candle in m15_candles:
        formatted_timestamp = candle[0].strftime("%b %d, %Y %H:%M:%S")
        processed_row = [formatted_timestamp, candle[4], candle[1], candle[2], candle[3]]
        processed_data.append(processed_row)

    csv_string = ""
    for row in processed_data:
        csv_string += ",".join('"{0}"'.format(item) for item in row) + "\n"

    return csv_string

def get_alpaca_historical_data(symbol):
    print("function called")
    current_date = datetime.now().date()
    start_date = current_date - timedelta(days=7)
    start_date_str = start_date.strftime('%Y-%m-%d %H:%M:%S')
    print(start_date_str)
    request_params = CryptoBarsRequest(
        symbol_or_symbols=[symbol],
        timeframe=TimeFrame.Minute,
        start=start_date_str
    )
    
    bars = historical_client.get_crypto_bars(request_params, feed="us")
    data = bars.df.reset_index()  # Reset the index to make timestamp a column
    
    formatted_data = []
    for _, row in data.iterrows():
        timestamp = row['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
        open_price = row['open']
        high_price = row['high']
        low_price = row['low']
        close_price = row['close']
        
        formatted_row = [timestamp, open_price, high_price, low_price, close_price]
        formatted_data.append(formatted_row)
    return formatted_data

def get_alpaca_dataframe(symbol):
    print("function called")
    current_date = datetime.now().date()
    start_date = current_date - timedelta(days=7)
    start_date_str = start_date.strftime('%Y-%m-%d %H:%M:%S')
    request_params = CryptoBarsRequest(
        symbol_or_symbols=[symbol],
        timeframe=TimeFrame.Minute,
        start=start_date_str
    )
    
    bars = historical_client.get_crypto_bars(request_params, feed="us")
    data = bars.df.reset_index()  # Reset the index to make timestamp a column
    
    return data

# async def bar_callback(bar):
#     for property_name, value in bar:
#         print(f"\"{property_name}\": {value}")

# # Subscribing to bar event 
# symbol = "BTC/USD"
# crypto_stream.subscribe_bars(bar_callback, symbol)

# crypto_stream.run()