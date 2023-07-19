from edwizy_app.bot.bot import *
from dhanhq import dhanhq
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import http.client
import json
import pandas as pd
from edwizy_app.models import Trades, Profile, Symbol, Strategies

current_date = datetime.now().date()
start_date = current_date - timedelta(days=7)
start_date_str = start_date.strftime('%Y-%m-%d')
current_date_str = current_date.strftime('%Y-%m-%d')


def get_dhan_trading_history(client_id, access_token):
    dhan = dhanhq(client_id,access_token)
    return dhan.get_positions()

def get_dhan_orders(access_token):
    conn = http.client.HTTPSConnection("api.dhan.co")
    headers = {
        'access-token': access_token,
        'Accept': "application/json"
    }
    conn.request("GET", "/orders", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")

    df = pd.read_json(data)
    return df

def get_dhan_open_positions(access_token):
    conn = http.client.HTTPSConnection("api.dhan.co")
    headers = {
        'access-token': access_token,
        'Accept': "application/json"
    }
    conn.request("GET", "/positions", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")

    df = pd.read_json(data)
    return df

def get_dhan_intraday_chart(security_id, exchange_segment, instrument, access_token):
    try:
        conn = http.client.HTTPSConnection("api.dhan.co")
        payload = {
            "securityId": security_id,
            "exchangeSegment": exchange_segment,
            "instrument": instrument
        }   
        payload_json = json.dumps(payload)

        headers = {
            'access-token': access_token,
            'Content-Type': "application/json",
            'Accept': "application/json"
        }

        conn.request("POST", "/charts/intraday", payload_json, headers)

        res = conn.getresponse()
        data = res.read().decode("utf-8")

        df = pd.read_json(data)
        return df
    except:
        return []

def dhan_process_data(data, timeframe):
    m15_candles = []
    processed_data = []
    current_candle = None
    # processed_data.append(["DateTime", "Price", "Open", "High", "Low"])

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
    try:
        for index, row in data.iterrows():
            open_price = row['open']
            high_price = row['high']
            low_price = row['low']
            close_price = row['close']
            timestamp = row['start_Time']
            
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
            time = candle[0] + relativedelta(years=10)
            formatted_timestamp = time.strftime("%b %d, %Y %H:%M:%S")
            processed_row = [formatted_timestamp, candle[4], candle[1], candle[2], candle[3]]
            processed_data.append(processed_row)

        csv_string = ""
        for row in processed_data:
            csv_string += ",".join('"{0}"'.format(item) for item in row) + "\n"

        return csv_string
    except:
        return ""


def dhan_stream_data(data, timeframe):
    m15_candles = []
    processed_data = []
    current_candle = None
    # processed_data.append(["DateTime", "Price", "Open", "High", "Low"])

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
    try:
        for index, row in data.iterrows():
            open_price = row['open']
            high_price = row['high']
            low_price = row['low']
            close_price = row['close']
            timestamp = row['start_Time']
            
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
            processed_row = [int(candle[4]), int(candle[1]), int(candle[2]), int(candle[3])]
            processed_data.append(processed_row)

        df = pd.DataFrame(processed_data, columns=['open', 'high', 'low', 'close'])
        return df
    except:
        return ""

def open_dhan_trade(strategy, time_frame, username, client_id, access_token, entry_price, order_qty, take_profit, stop_loss,security_id, exchange_segment, signal, symbol):
    dhan = dhanhq(client_id,access_token)
    if not currencyTrading():
        if not maxTrades():
            order_placed = dhan.place_order(
                            tag=symbol,
                            transaction_type=getattr(dhan, signal),
                            exchange_segment= getattr(dhan, exchange_segment),
                            product_type=dhan.BO,
                            order_type=dhan.MARKET,
                            validity='DAY',
                            security_id=security_id,
                            quantity=int(order_qty),
                            disclosed_quantity=0,
                            price=entry_price,
                            trigger_price=0,
                            after_market_order=False,
                            amo_time='OPEN',
                            bo_profit_value=take_profit,
                            bo_stop_loss_Value=stop_loss,
                            drv_expiry_date=None,
                            drv_options_type=None,
                            drv_strike_price=None    
                        )
            
            status = order_placed['status']
            
            if status == 'success': 
                result = order_placed['orderStatus']
                id = order_placed['orderId']
                if result == "PENDING" or result == "TRADED":
                    dhan_save_trade(id, username, symbol, signal, order_qty, entry_price, stop_loss, take_profit, time_frame, strategy)    
                return result
            else:
                return order_placed
        else:
            return 0
    else:
         return 0

def dhan_save_trade(id, username, symbol,order_type, order_size, price, stoploss, takeprofit, trigger_timeframe, bot):
    profile = Profile.objects.get(name=username)
    bot = Strategies.objects.get(name=bot)
    current_time = datetime.now().strftime("%Y.%m.%d.%H:%M")
    trade = Trades.objects.create(trade_id=id, owner=profile, symbol=symbol, time=current_time, order_type=order_type, order_size= order_size, price=price, stop_loss=stoploss, take_profit=takeprofit, trigger_timeframe=trigger_timeframe, bot=bot)
    

# def dhan_update_trades(username):
#     profile = Profile.objects.get(name=username)
#     open_conditions = {}
#     open_cond = ['OPEN', 'PENDING']
#     open_conditions['owner'] = profile
#     open_conditions['status__in'] = open_cond
#     open_trades = Trades.objects.filter(**open_conditions).order_by('-pk')
#     positions = get_dhan_open_positions(profile.secret_key)
#     if not open_trades.empty:
#         for trade in open_trades:
#             if sym.name in open_trades['tradingSymbol'].tolist():

        