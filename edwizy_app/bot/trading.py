import asyncio
from edwizy_app.models import Trades, Profile, Symbol, Strategies
from .bot import *
from .alpaca import *
from .dhan import *

def get_active_symbols():
    active_symbols = Symbol.objects.filter(active=True)
    symbol_data = {}
    
    for symbol in active_symbols:
        symbol_data[symbol.name] = dhan_stream_data(get_dhan_intraday_chart(symbol.security_id, symbol.exchange_segment, symbol.instrument_type, symbol.owner.secret_key), symbol.owner.time_frame)
        

    return symbol_data

def check_strategies(df):
    strategy_names = []
    result = False

    if buyDareToTrade(df):
        strategy_names.append(("DareToTrade", "BUY"))
        result = True

    if buyPriceAction(df):
        strategy_names.append(("PriceAction", "BUY"))
        result = True

    if buyFibonacci(df):
        strategy_names.append(("Fibonacci", "BUY"))
        result = True

    if buyCamarilla(df):
        strategy_names.append(("Camarilla", "BUY"))
        result = True

    if sellDareToTrade(df):
        strategy_names.append(("DareToTrade", "SELL"))
        result = True

    if sellPriceAction(df):
        strategy_names.append(("PriceAction", "SELL"))
        result = True

    if sellFibonacci(df):
        strategy_names.append(("Fibonacci", "SELL"))
        result = True

    if sellCamarilla(df):
        strategy_names.append(("Camarilla", "SELL"))
        result = True

    return result, strategy_names

def CalcPriceActionDataframe(df):
    number = df["open"].iloc[-1]
    dp = count_decimal_places(number)
    df["RSI"] = calculate_rsi(df["close"], window=7)

    for i in range(1, len(df)):
        open1 = df["open"].iloc[i]
        close1 = df["close"].iloc[i]
        low1 = df["low"].iloc[i]
        high1 = df["high"].iloc[i]
        open2 = df["open"].iloc[i-1]
        close2 = df["close"].iloc[i-1]
        low2 = df["low"].iloc[i-1]
        high2 = df["high"].iloc[i-1]

        df.at[i, "op1"] = open1
        df.at[i, "op2"] = open2
        df.at[i, "cp1"] = close1
        df.at[i, "cp2"] = close2
        df.at[i, "hp1"] = high1
        df.at[i, "hp2"] = high2
        df.at[i, "lp1"] = low1
        df.at[i, "lp2"] = low2
        df.at[i, "oc1"] = round(abs(open1 - close1), dp)
        df.at[i, "oc2"] = round(abs(open2 - close2), dp)
        df.at[i, "hl1"] = round(abs(high1 - low1), dp)
        df.at[i, "hl2"] = round(abs(high2 - low2), dp)
        df.at[i, "bot3"] = low1 + (0.3 * df.at[i, "hl1"])
        df.at[i, "top3"] = high1 - (0.3 * df.at[i, "hl1"])
        df.at[i, "points"] = get_decimal(dp)
    return df


def check_strategies_for_active_symbols():
    active_symbols_data = get_active_symbols()
    results = []
    
    for symbol, dataframe in active_symbols_data.items():
        try:
            data = CalcPriceActionDataframe(dataframe)
            results.append(check_strategies(data)) 
        except:
            pass

    print(results)
    for (symbol, _), (result, strategy_names) in zip(active_symbols_data.items(), results):
        if result:
            dataframe = active_symbols_data[symbol]
            for strategy_name, order_type in strategy_names:
                print(f"Strategy '{strategy_name}' returned True to {order_type} for symbol: {symbol}")
                symb = Symbol.objects.filter(name=symbol)
                for sym in symb:
                    open_trades = get_dhan_open_positions(sym.owner.secret_key)
                    if not open_trades.empty:
                        if sym.name in open_trades['tradingSymbol'].tolist():
                            print("DOUBLE TRADE")
                            pass
                    else:
                        # result = open_dhan_trade(strategy_name, sym.owner.time_frame, sym.owner.name, sym.owner.api_key, sym.owner.secret_key, 0,sym.owner.order_size, 3, 3,sym.security_id, sym.exchange_segment, order_type, symbol)
                        # print(result)
                        pass
                        


