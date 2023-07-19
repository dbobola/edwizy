import requests
import oandapyV20
import oandapyV20.endpoints.transactions as transactions
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.orders import OrderCreate


# Set the base URL for the OANDA API
BASE_URL = "https://api-fxpractice.oanda.com"
ACCOUNT_ID  = "101-001-25836141-002"

OANDA_API_KEY = ""
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OANDA_API_KEY}",
    "Connection": "keep-alive"
}

# Function to get account details
def get_account_details(ACCOUNT_ID):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get account details. Error: {err}")


def create_order(ACCOUNT_ID, order_data):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/orders"
    response = requests.post(url, headers=headers, json=order_data)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to create order. Error: {err}")


def get_account_summary(ACCOUNT_ID):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/summary"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get account summary. Error: {err}")

def get_candlestick_data(instrument, granularity):
    url = f"{BASE_URL}/v3/instruments/{instrument}/candles"
    params = {
        "granularity": granularity
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get candlestick data. Error: {err}")

def get_order_book(instrument):
    url = f"{BASE_URL}/v3/instruments/{instrument}/orderBook"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get order book. Error: {err}")

def get_position_book(instrument):
    url = f"{BASE_URL}/v3/instruments/{instrument}/positionBook"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get position book. Error: {err}")

def get_accounts():
    url = f"{BASE_URL}/v3/accounts"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get accounts. Error: {err}")

def get_account_instruments(ACCOUNT_ID):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/instruments"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get account instruments. Error: {err}")

def set_account_configuration(ACCOUNT_ID, configuration_data):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/configuration"
    response = requests.patch(url, headers=headers, json=configuration_data)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to set account configuration. Error: {err}")

def get_account_changes(ACCOUNT_ID, since_transaction_id):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/changes"
    params = {
        "sinceTransactionID": since_transaction_id
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get account changes. Error: {err}")


def get_orders(ACCOUNT_ID):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/orders"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get orders. Error: {err}")

def get_pending_orders(ACCOUNT_ID):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/pendingOrders"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get pending orders. Error: {err}")

def get_order_details(ACCOUNT_ID, order_id):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/orders/{order_id}"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get order details. Error: {err}")

def replace_order(ACCOUNT_ID, order_id, order_data):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/orders/{order_id}/replace"
    response = requests.put(url, headers=headers, json=order_data)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to replace order. Error: {err}")

def cancel_order(ACCOUNT_ID, order_id):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/orders/{order_id}/cancel"
    response = requests.put(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to cancel order. Error: {err}")

def update_order_extensions(ACCOUNT_ID, order_id, extension_data):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/orders/{order_id}/clientExtensions"
    response = requests.put(url, headers=headers, json=extension_data)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to update order extensions. Error: {err}")

def get_trades(ACCOUNT_ID):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/trades"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get trades. Error: {err}")

def get_open_trades(ACCOUNT_ID):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/openTrades"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get open trades. Error: {err}")

def get_trade_details(ACCOUNT_ID, trade_id):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/trades/{trade_id}"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get trade details. Error: {err}")

def close_trade(ACCOUNT_ID, trade_id):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/trades/{trade_id}/close"
    response = requests.put(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to close trade. Error: {err}")

def update_trade_extensions(ACCOUNT_ID, trade_id, extension_data):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/trades/{trade_id}/clientExtensions"
    response = requests.put(url, headers=headers, json=extension_data)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to update trade extensions. Error: {err}")

def update_trade_orders(ACCOUNT_ID, trade_id, order_data):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/trades/{trade_id}/orders"
    response = requests.put(url, headers=headers, json=order_data)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to update trade orders. Error: {err}")

def get_positions(ACCOUNT_ID):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/positions"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get positions. Error: {err}")

def get_open_positions(ACCOUNT_ID):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/openPositions"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get open positions. Error: {err}")

def get_position_details(ACCOUNT_ID, instrument):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/positions/{instrument}"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get position details. Error: {err}")

def close_position(ACCOUNT_ID, instrument):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/positions/{instrument}/close"
    response = requests.put(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to close position. Error: {err}")

def get_transactions(ACCOUNT_ID):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/transactions"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get transactions. Error: {err}")

def get_transaction_details(ACCOUNT_ID, transaction_id):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/transactions/{transaction_id}"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get transaction details. Error: {err}")

def get_transactions_id_range(ACCOUNT_ID, from_id, to_id):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/transactions/idrange"
    params = {
        "from": from_id,
        "to": to_id
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get transactions in ID range. Error: {err}")

def get_transactions_since_id(ACCOUNT_ID, since_id):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/transactions/sinceid"
    params = {
        "id": since_id
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get transactions since ID. Error: {err}")

def get_transaction_stream(ACCOUNT_ID):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/transactions/stream"
    response = requests.get(url, headers=headers, stream=True)
    try:
        response.raise_for_status()
        return response.iter_lines()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get transaction stream. Error: {err}")

def get_latest_candles(instrument, granularity):
    url = f"{BASE_URL}/v3/instruments/{instrument}/candles/latest"
    params = {
        "granularity": granularity
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get latest candles. Error: {err}")

def get_pricing(instruments):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/pricing"
    params = {
        "instruments": instruments
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get pricing. Error: {err}")

def get_pricing_stream(instruments):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/pricing/stream"
    params = {
        "instruments": instruments
    }
    response = requests.get(url, headers=headers, stream=True, params=params)
    try:
        response.raise_for_status()
        return response.iter_lines()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get pricing stream. Error: {err}")

def get_instrument_candles(instrument, granularity, count=500, from_time=None, to_time=None):
    url = f"{BASE_URL}/v3/instruments/{instrument}/candles"
    params = {
        "granularity": granularity,
        "count": count,
        "from": from_time,
        "to": to_time
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get instrument candles. Error: {err}")
    
def get_tradeable_instruments(ACCOUNT_ID):
    url = f"{BASE_URL}/v3/accounts/{ACCOUNT_ID}/instruments"
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to get tradeable instruments. Error: {err}")
    
    



import time
import pandas as pd
import numpy as np
import os
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
from oandapyV20.endpoints.instruments import InstrumentsCandles

# Set the OANDA API key
OANDA_API_KEY = "33a9e22e79a6afe67da0e568b0cca830-cf5e494dfe461d8704057859e229b74e"
api = API(access_token=OANDA_API_KEY)

ACCOUNT_ID = "101-001-25836141-002"
INSTRUMENTS = ["GBP_USD"]  # Add more forex pairs as per your requirements
GRANULARITIES = ["D"]
directory = "streaming_data"
os.makedirs(directory, exist_ok=True)

INDICATORS_DIRECTORY = "indicators"
os.makedirs(INDICATORS_DIRECTORY, exist_ok=True)


def load_historical_data(instrument, granularity, count):
    params = {"granularity": granularity, "count": count}
    r = InstrumentsCandles(instrument=instrument, params=params)
    api.request(r)

    records = []
    for candle in r.response["candles"]:
        record = {
            "time": candle["time"],
            "volume": candle["volume"],
            "open": candle["mid"]["o"],
            "high": candle["mid"]["h"],
            "low": candle["mid"]["l"],
            "close": candle["mid"]["c"],
            "instrument": instrument,
            "granularity": granularity
        }
        records.append(record)
    
    df = pd.DataFrame(records)
    df["time"] = pd.to_datetime(df["time"])
    df = calculate_indicators(df) 
    save_to_csv(df, instrument, granularity)
    save_indicators_to_csv(df, instrument)


def stream_data(account_id, instruments):
    try:
        r = PricingStream(accountID=account_id, params={"instruments": ",".join(instruments)})
        for R in api.request(r):
            for instrument in instruments:
                if R['type'] == 'PRICE' and R['instrument'] == instrument:
                    process_data(R, instrument)
    except V20Error as e:
        print(f"Error: {e}")

def process_data(data, instrument):
    for granularity in GRANULARITIES:
        r = InstrumentsCandles(instrument=instrument, params={"granularity": granularity, "count": 1})
        api.request(r)
        time.sleep(3.5)
        for candle in r.response["candles"]:
            record = {
                "time": candle["time"],
                "volume": candle["volume"],
                "open": candle["mid"]["o"],
                "high": candle["mid"]["h"],
                "low": candle["mid"]["l"],
                "close": candle["mid"]["c"],
                "instrument": instrument,
                "granularity": granularity
            }
            df = pd.DataFrame([record])
            df["time"] = pd.to_datetime(df["time"])
            df = calculate_indicators(df)  
            save_to_csv(df, instrument, granularity)


def calculate_indicators(df):
    # Convert columns to numeric type
    numeric_cols = ["open", "high", "low", "close"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)

    # Calculate indicators
    df["RSI"] = calculate_rsi(df["close"], window=14)
    df["MACD"], df["Signal_Line"], df["Histogram"] = calculate_macd(df["close"], window_fast=12, window_slow=26, window_signal=9)
    df["BollingerBands_middle"], df["BollingerBands_std"] = calculate_bollinger_bands(df["close"], window=20)
    df["ATR"] = calculate_atr(df["high"], df["low"], df["close"], window=14)
    df["ADX"] = calculate_adx(df["high"], df["low"], df["close"], window=14)
    df["OBV"] = calculate_obv(df["close"], df["volume"])
    return df

def save_indicators_to_csv(df, instrument):
    indicators = ["RSI", "MACD", "Signal_Line", "Histogram", "BollingerBands_middle", "BollingerBands_std", "ATR", "ADX", "OBV"]
    for indicator in indicators:
        indicator_df = df[["time", indicator]]
        filename = f"{INDICATORS_DIRECTORY}/{instrument}_{indicator}.csv"
        indicator_df.to_csv(filename, index=False)

def calculate_rsi(series, window):
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(series, window_fast, window_slow, window_signal):
    ema_fast = series.ewm(span=window_fast, adjust=False).mean()
    ema_slow = series.ewm(span=window_slow, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=window_signal, adjust=False).mean()
    histogram = macd - signal_line
    return macd, signal_line, histogram

def calculate_bollinger_bands(series, window):
    middle_band = series.rolling(window=window).mean()
    std = series.rolling(window=window).std()
    return middle_band, std

def calculate_atr(high, low, close, window):
    tr = np.maximum(high - low, np.abs(high - close.shift()), np.abs(low - close.shift()))
    atr = tr.rolling(window=window).mean()
    return atr

def calculate_adx(high, low, close, window):
    tr = np.maximum(high - low, np.abs(high - close.shift()), np.abs(low - close.shift()))
    atr = calculate_atr(high, low, close, window)  # Calculate ATR using the separate function
    plus_dm = np.where((high - high.shift()) > (low.shift() - low), high - high.shift(), 0)
    minus_dm = np.where((low.shift() - low) > (high - high.shift()), low.shift() - low, 0)
    plus_di = 100 * (pd.Series(plus_dm).rolling(window=window).mean() / pd.Series(atr).rolling(window=window).mean())
    minus_di = 100 * (pd.Series(minus_dm).rolling(window=window).mean() / pd.Series(atr).rolling(window=window).mean())
    dx = 100 * np.abs(plus_di - minus_di) / (plus_di + minus_di)
    adx = dx.rolling(window=window).mean()
    return adx

def calculate_obv(close, volume):
    obv = np.where(close > close.shift(), volume, -volume).cumsum()
    return obv

def save_to_csv(df, instrument, granularity):
    if df is not None and not df.empty:
        filename = os.path.join(directory, f"{instrument}_{granularity}.csv")
        if not os.path.isfile(filename):
            df.to_csv(filename, index=False)
        else:
            df.to_csv(filename, mode='a', header=False, index=False)


if __name__ == "__main__":
    for instrument in INSTRUMENTS:
        for granularity in GRANULARITIES:
            load_historical_data(instrument, granularity, count=90*24)

    stream_data(ACCOUNT_ID, INSTRUMENTS)
