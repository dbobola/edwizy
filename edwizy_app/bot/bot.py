
from decimal import Decimal
from datetime import datetime
import time

def process_df(df, timeframe):
    m15_candles = []
    processed_df = []
    current_candle = None
    processed_df.append(["DateTime", "Price", "Open", "High", "Low"])

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
    
    for row in df:
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
        processed_df.append(processed_row)

    csv_string = ""
    for row in processed_df:
        csv_string += ",".join('"{0}"'.format(item) for item in row) + "\n"

    return csv_string
def maxTrades():
    return False

def currencyTrading():
        return False

def calculate_rsi(series, window):
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def IsRSI7OverBought(df):
    
    current_rsi = df["RSI"].iloc[-1]
    if current_rsi >= 55.0:
        return True
    
    return False

def IsRSI7OverSold(df):
    current_rsi = df['RSI'].iloc[-1]
    if current_rsi <= 35.0:
        return True
    return False

def IsRSI15OverBought(df):
    current_rsi = df['RSI'].iloc[-1]
    if current_rsi >= 55.0:
        return True
    return False

def IsRSI15OverSold(df):
    current_rsi = df['RSI'].iloc[-1]
    if current_rsi <= 35.0:
        return True
    return False

def IsSwingLow(df):
    last_100_candles = df.tail(100)
    lowest_value = last_100_candles["low"].min()
    low = df["low"].iloc[-1]

    if lowest_value == low:
        return True
    return False
        

def IsSwingHigh(df):
    last_100_candles = df.tail(100)
    highest_value = last_100_candles["high"].max()
    high = df["high"].iloc[-1]

    if highest_value == high:
        return True
    
    return False

def count_decimal_places(number):
    if isinstance(number, float):
        number_str = str(number)
        if '.' in number_str:
            decimal_places = len(number_str) - number_str.index('.') - 1
            return decimal_places
    return 0

def get_decimal(dp):
    return Decimal('0.1') ** dp
    
def CalcDareToTradedfframe(df):
    return calculate_rsi(df, )


def CalcCamarilldfframe(daily_df):
    number = daily_df["open"].iloc[-1]
    dp = count_decimal_places(number)
    c = daily_df["close"]
    h = daily_df["high"]
    l = daily_df["low"]

    daily_df["H1"] = round(c + (h -l)*1.1/12)
    daily_df["H2"] = round(c + (h -l)*1.1/6)
    daily_df["H3"] = round(c + (h -l)*1.1/4)
    daily_df["H4"] = round(c + (h -l)*1.1/2)
    daily_df["H5"] = round(c + (h -l)*1.1)
    daily_df["H6"] = round(daily_df["H5"] + 1.168*(daily_df["H5"] - daily_df["H4"]))
    daily_df["L1"] = round(c - (h -l)*1.1/12)
    daily_df["L2"] = round(c - (h -l)*1.1/6)
    daily_df["L3"] = round(c - (h -l)*1.1/4)
    daily_df["L4"] = round(c - (h -l)*1.1/2)
    daily_df["L5"] = round(c - daily_df["H5"] - c)
    daily_df["L6"] = round(c - daily_df["H6"] - c)

    return daily_df
    
def IsBuyKangaroo(df):
    
    return (
        (df["oc1"].iloc[-1] > 100 * df["points"].iloc[-1]) and
        (df["oc1"].iloc[-1] < 300 * df["points"].iloc[-1]) and
        (df["cp1"].iloc[-1] > df["top3"].iloc[-1]) and
        (df["hl1"].iloc[-1] > 3 * df["oc1"].iloc[-1]) and
        (df["op1"].iloc[-1] > df["lp2"].iloc[-2]) and
        (df["cp1"].iloc[-1] > df["lp2"].iloc[-2])
    )


def IsSellKangaroo(df):

    return (
        (df["oc1"].iloc[-1] > 100 * df["points"].iloc[-1]) and 
        (df["oc1"].iloc[-1] < 300 * df["points"].iloc[-1]) and 
        (df["cp1"].iloc[-1] < df["bot3"].iloc[-1]) and 
        (df["hl1"].iloc[-1] > 3 * df["oc1"].iloc[-1]) and 
        (df["op1"].iloc[-1] < df["hp2"].iloc[-2]) and 
        (df["cp1"].iloc[-1] < df["hp2"].iloc[-2]))
       

def IsBuyBigShadow(df):


    if((df["oc1"].iloc[-1] > df["oc2"].iloc[-1]) and (df["oc1"].iloc[-1] > 500 * df["points"].iloc[-1]) and (df["cp1"].iloc[-1] > df["cp2"].iloc[-1]) and (df["bot3"].iloc[-1] > df["op1"].iloc[-1]) and (df["cp1"].iloc[-1] > df["top3"].iloc[-1]) and (df["hp1"].iloc[-1] > df["hp2"].iloc[-1]) and (df["op2"].iloc[-2] > df["cp2"].iloc[-2]) and (df["cp1"].iloc[-1] > df["op2"].iloc[-2])):
        return True
    return False

def IsSellBigShadow(df):
    
    if((df["oc1"].iloc[-1] > df["oc2"].iloc[-1]) and (df["oc1"].iloc[-1] > 500 * df["points"].iloc[-1]) and (df["cp1"].iloc[-1] < df["cp2"].iloc[-1]) and (df["bot3"].iloc[-1] > df["cp1"].iloc[-1]) and (df["op1"].iloc[-1] > df["top3"].iloc[-1]) and (df["lp1"].iloc[-1] > df["lp2"].iloc[-1]) and (df["op2"].iloc[-2] < df["cp2"].iloc[-2]) and (df["cp1"].iloc[-1] < df["op2"].iloc[-2])):
        return True
    return False

def buyDareToTrade(df):
    return (IsRSI7OverBought(df) and IsRSI15OverBought(df) and ((IsBuyKangaroo(df) or IsBuyBigShadow(df))))
    
    
def sellDareToTrade(df):
    return (IsRSI7OverSold(df) and IsRSI15OverSold(df) and ((IsSellKangaroo(df) or IsSellBigShadow(df))))


def buyCamarilla(df):
    daily_df = df
    daily_df = CalcCamarilldfframe(daily_df)
    df = df.iloc[-1]
    return ((daily_df["H3"].iloc[-1] > df["open"]) and (df["open"] > daily_df["L3"].iloc[-1]) and (df["low"] < daily_df["L3"].iloc[-1]) and (df["close"] > daily_df["L3"].iloc[-1]))
    
def sellCamarilla(df):
    daily_df = df
    daily_df = CalcCamarilldfframe(daily_df)
    df = df.iloc[-1]
    return ((daily_df["H3"].iloc[-1] > df["open"]) and (df["open"] > daily_df["L3"].iloc[-1]) and (df["high"] > daily_df["H3"].iloc[-1]) and (df["close"] < daily_df["H3"].iloc[-1]))
   

def buyPriceAction(df):
    return ((IsBuyKangaroo(df) or IsBuyBigShadow(df)))
    
    
def sellPriceAction(df):
    return ((IsSellKangaroo(df) or IsSellBigShadow(df)))
       

def buyFibonacci(df):
    number = df["open"].iloc[-1]
    dp = count_decimal_places(number)
    last_100_candles = df.tail(100)
    price_low_candle = int(last_100_candles['low'].idxmin())  # Convert index to integer
    price_high_candle = int(last_100_candles['high'].idxmax())  # Convert index to integer
    price_low = df.loc[price_low_candle, 'low']
    price_high = df.loc[price_high_candle, 'high']
    price_range = round(abs(price_high - price_low), dp)
    zero_eight_level = round(abs(price_high - price_range * 0.08), dp)
    three_eight_level = round(abs(price_high - price_range * 0.382), dp)
    five_one_level = round(abs(price_high - price_range * 0.51), dp)
    one_two_two_eight_level = round(abs(price_high - price_range * 1.22), dp)
    one_five_nine_level = round(abs(price_high - price_range * 1.59), dp)
    
    min_count = 30
    buy_true = True
    sell_true = True


    for i in range(1, min_count):
        if df.loc[i, 'close'] < three_eight_level:
            buy_true = False
            break

    for i in range(1, min_count):
        if df.loc[i, 'close'] > three_eight_level:
            sell_true = False
            break

    return buy_true and (df.loc[1, 'close'] < zero_eight_level) and (
            (df.loc[1, 'close'] > three_eight_level) or (df.loc[1, 'close'] > five_one_level))
    
def sellFibonacci(df):
    number = df["open"].iloc[-1]
    dp = count_decimal_places(number)
    last_100_candles = df.tail(100)
    price_low_candle = int(last_100_candles['low'].idxmin())  # Convert index to integer
    price_high_candle = int(last_100_candles['high'].idxmax())  # Convert index to integer
    price_low = df.loc[price_low_candle, 'low']
    price_high = df.loc[price_high_candle, 'high']
    price_range = round(abs(price_high - price_low), dp)
    zero_eight_level = round(abs(price_high - price_range * 0.08), dp)
    three_eight_level = round(abs(price_high - price_range * 0.382), dp)
    five_one_level = round(abs(price_high - price_range * 0.51), dp)
    one_two_two_eight_level = round(abs(price_high - price_range * 1.22), dp)
    one_five_nine_level = round(abs(price_high - price_range * 1.59), dp)
    
    min_count = 30
    buy_true = True
    sell_true = True
    
    for i in range(1, min_count):
        if df.loc[i, 'close'] < three_eight_level:
            buy_true = False
            break

    for i in range(1, min_count):
        if df.loc[i, 'close'] > three_eight_level:
            sell_true = False
            break

    return sell_true and (df.loc[1, 'close'] > one_two_two_eight_level) and (
            (df.loc[1, 'close'] < three_eight_level) or (df.loc[1, 'close'] < five_one_level))