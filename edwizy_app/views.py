from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import csv, os, json
from django.http import JsonResponse
from datetime import datetime
from .models import Trades, Profile, Symbol, Strategies
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from edwizy_app.bot.dhan import *
from edwizy_app.bot.alpaca import *
from edwizy_app.bot.trading import *
from edwizy_app.bot.angel import *

# from edwizy_app.bot.binance import *
from django.db.models import F, Case, When, IntegerField
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import threading
import time

ALPACA_API_KEY_ID = "PKZORLL65QU26JUJ7N0B"
ALPACA_API_SECRET_KEY = "QupmtRUUIh4hI0sd13tHQTgTes7t0UUXm0TFGXmU"
BASE_URL = "https://paper-api.alpaca.markets"

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('email')
            password = request.POST.get('password')
            user_exists = User.objects.filter(username=username).exists()
            if user_exists:
                authenticated_user = authenticate(request, username=username, password=password) 
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    return redirect('/')
            else:
                return HttpResponse("Else: Wrong Username or Password, please try again.", content_type='text/csv')
        except Exception as e:
            return HttpResponse(str(e))
            
@csrf_exempt
def user_logout(request):
    logout(request)
    request.user = None
    return redirect('/')

@csrf_exempt
def load_data(request):
    try:
        if request.method == 'POST':
            symbol = request.POST.get('symbol')
            time_frame = request.POST.get('timeframe')
            profile = Profile.objects.get(user=request.user)
            access_token = profile.secret_key
            current_symbol = Symbol.objects.get(name=symbol)
            security_id = current_symbol.security_id
            exchange_segment = current_symbol.exchange_segment
            instrument_type = current_symbol.instrument_type
            active_symbol = symbol + '_' + time_frame
            profile.active_chart = active_symbol
            profile.save()

            dat = get_dhan_intraday_chart(security_id, exchange_segment, instrument_type, access_token)
            data = dhan_process_data(dat, "5M")
            return HttpResponse(data, content_type='text/csv')
        
    except:
        profile = Profile.objects.get(user=request.user)
        symbol_old, time_frame_old = profile.active_chart.split("_")
        access_token = profile.secret_key
        current_symbol = Symbol.objects.get(name=symbol_old)
        symbol_conditions = {}
        symbol_conditions['owner'] = profile
        symbol_conditions['name'] = symbol_old
        current_symbol = Symbol.objects.get(**symbol_conditions) 
        security_id = current_symbol.security_id
        exchange_segment = current_symbol.exchange_segment
        instrument_type = current_symbol.instrument_type
        dat = get_dhan_intraday_chart(security_id, exchange_segment, instrument_type, access_token)
        data = dhan_process_data(dat, time_frame_old)
        return HttpResponse(data, content_type='text/csv')
    
    else:
        data = []
       
        return HttpResponse(data, content_type='text/csv')

def base(request):
    profile = Profile.objects.get(user=request.user)
    open_conditions = {}
    open_cond = ['OPEN', 'PENDING']
    open_conditions['owner'] = profile
    open_conditions['status__in'] = open_cond
    open_trades = Trades.objects.filter(**open_conditions).order_by('-pk')
    open_trades_count = open_trades.count()
    
    context = {
        "open_trades_count": open_trades_count
    }
    return render(request, 'dashboard.html', context)

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    if request.user.is_authenticated:
        calcAccount(request)
        profile = Profile.objects.get(user=request.user)
        open_conditions = {}
        open_cond = ['OPEN', 'PENDING']
        open_conditions['owner'] = profile
        open_conditions['status__in'] = open_cond
        open_trades = Trades.objects.filter(**open_conditions).order_by('-pk')
        open_trades_count = open_trades.count()
        active_chart = profile.active_chart

        if active_chart != "":
            symbol, time_frame = active_chart.split('_')
        else:
            time_frame = "5M"
            symbol = Symbol.objects.first()
        
        profile = Profile.objects.get(user=request.user)
        symbols_objects = Symbol.objects.filter(owner=profile).order_by(
        Case(
            When(active=True, then=F('pk')),
            default=F('pk') + 99999999,  # A high value to push inactive symbols to the bottom
        ))
        symbols = [str(symbol) for symbol in symbols_objects]

        timeframe = ["1M", "5M", "15M", "1H", "4H", "1D", "1W"]
            
        context = {
    
            "open_trades_count": open_trades_count,
            'symbols': symbols,
            'timeframe': timeframe,
            'active_chart': active_chart,
            'active_symbol': symbol,
            'active_time_frame': time_frame
        }
        return render(request, 'dashboard.html', context)
    else:
        print('happening')
        return render(request, 'dashboard.html')
    
def data_view(request):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'data.csv')

    data = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            timestamp_str = row[0]
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
            timestamp_ms = int(timestamp.timestamp() * 1000)  # Convert the timestamp to milliseconds
            data.append([timestamp_ms] + [float(value) for value in row[1:]])

    return JsonResponse(data, safe=False)

def trades(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        open_conditions = {}
        open_cond = ['OPEN', 'PENDING']
        open_conditions['owner'] = profile
        open_conditions['status__in'] = open_cond
        open_trades = Trades.objects.filter(**open_conditions).order_by('-pk')
        open_trades_count = open_trades.count()
        closed_conditions = {}
        closed_cond = ['CLOSED']
        closed_conditions['owner'] = profile
        closed_conditions['status__in'] = closed_cond
        closed_trades = Trades.objects.filter(**closed_conditions).order_by('-pk')
        closed_trades_count = closed_trades.count()

        context = {
            'open_trades': open_trades,
            'closed_trades': closed_trades,
            'closed_trades_count': closed_trades_count,
            'open_trades_count': open_trades_count
        }
        return render(request, 'trades.html', context)
    else:
        return redirect('/')

def addbot(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        
        active_bots = Symbol.objects.filter(owner=profile).order_by(
            Case(
                When(active=True, then=-F('pk')),  # Negative pk for active symbols to keep them at the top
                default=F('pk'),  # Use positive pk for inactive symbols to push them to the bottom
                output_field=IntegerField(),  # Set the output_field to IntegerField for consistent types
            )
        )
        charts = ["XAUUSD", "GBPUSD", "EURUSD", "BTCUSD", "ETHUSD"]
        bots = ["Camarilla", "Dare To Trade", "Price Action", "Fibonacci"]
        timeframe = ["1M", "5M", "15M", "1H", "4H", "1D", "1W"]
        order_size = ['0.01', '0.02', '0.03', '0.04', '0.05', '0.1']
        order_type = ['Market Order', 'Stop Order']
        risk_reward = ['1:1', '1:2', '1:3', '1:4', '1:5']
        profile = Profile.objects.get(user=request.user)
        open_conditions = {}
        open_cond = ['OPEN', 'PENDING']
        open_conditions['owner'] = profile
        open_conditions['status__in'] = open_cond
        open_trades = Trades.objects.filter(**open_conditions).order_by('-pk')
        open_trades_count = open_trades.count()
    
        context = {
            'active_bots': active_bots,
            'charts': charts,
            'bots': bots,
            'timeframe': timeframe,
            'order_size': order_size,
            'order_type': order_type,
            'risk_reward': risk_reward,
            "open_trades_count": open_trades_count

        }
        return render(request, 'addbot.html', context)
    else:
        return redirect('/')

def analytics(request):
    if request.user.is_authenticated:
        calcAccount(request)
        profile = Profile.objects.get(user=request.user)
        profile = Profile.objects.get(user=request.user)
        open_conditions = {}
        open_cond = ['OPEN', 'PENDING']
        open_conditions['owner'] = profile
        open_conditions['status__in'] = open_cond
        open_trades = Trades.objects.filter(**open_conditions).order_by('-pk')
        open_trades_count = open_trades.count()
        context = {
            'profile': profile,
            "open_trades_count": open_trades_count
        }
        return render(request, 'analytics.html', context)
    else:
        return redirect('/')

def settings(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        api_key = profile.api_key
        secret_key = profile.secret_key
        user_broker = profile.broker
        user_max_trade = profile.max_trade
        user_timeframe = profile.time_frame
        user_risk_reward = profile.risk_reward
        user_order_size = profile.order_size
        user_order_type = profile.order_type

        calcprofit(request)
        profile = Profile.objects.get(user=request.user)
        open_conditions = {}
        open_cond = ['OPEN', 'PENDING']
        open_conditions['owner'] = profile
        open_conditions['status__in'] = open_cond
        open_trades = Trades.objects.filter(**open_conditions).order_by('-pk')
        open_trades_count = open_trades.count()
        strategies = Strategies.objects.all()
        timeframe = ["1M", "5M", "15M", "1H", "4H", "1D", "1W"]
        order_size = ['1', '5', '10', '15', '20', '25']
        order_type = ['Market Order', 'Stop Order', 'Limit Order']
        risk_reward = ['1:1', '1:2', '1:3', '1:4', '1:5']
        brokers = ['OANDA', 'DHAN', 'ALPACA', 'BINANCE']
        max_trades = [1, 2, 3, 4, 5, 7, 10]
        selected_strategies = []
        if profile.dare_to_trade == True:
            selected_strategies.append('Dare To Trade')
        
        if profile.price_action == True:
            selected_strategies.append('Price Action')

        if profile.camarilla == True:
            selected_strategies.append('Camarilla')
        
        if profile.fibonacci == True:
            selected_strategies.append('Fibonacci')

        context = {
            'profile': profile,
            'api_key': api_key,
            'secret_key': secret_key,
            "open_trades_count": open_trades_count,
            'strategies': strategies,
            'timeframe': timeframe,
            'order_size': order_size,
            'order_type': order_type,
            'risk_reward': risk_reward, 
            'brokers': brokers,
            'max_trades': max_trades,
            'user_broker': user_broker,
            'user_max_trade': user_max_trade,
            'user_time_frame': user_timeframe,
            'user_risk_reward': user_risk_reward,
            'user_order_size': user_order_size,
            'user_order_type': user_order_type,
            'selected_strategies': selected_strategies
        }
        return render(request, 'settings.html', context)
    else:
        return redirect('/')

@csrf_exempt
def update_bot(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        data = json.loads(request.body)
        bot_id = data.get('botId')
        print(bot_id)
        symbol = data.get('symbol')
        security_id = data.get('security_id')
        exchange_segment = data.get('exchange_segment')
        instrument_type = data.get('instrument_type')

        try:
            active_bot = Symbol.objects.create(owner =profile, name=symbol, security_id = security_id, exchange_segment=exchange_segment, instrument_type=instrument_type)
            print('created')

        except:
            pass
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
def pause_bot(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        data = json.loads(request.body)
        bot_id = data.get('botId')
        symbol = Symbol.objects.get(id=bot_id)
        try:
            symbol.active = False
            symbol.save()
        except:
            pass
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
def activate_bot(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        data = json.loads(request.body)
        bot_id = data.get('botId')
        symbol = Symbol.objects.get(id=bot_id)
        try:
            symbol.active = True
            symbol.save()
        except:
            pass
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
def delete_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bot_id = data.get('botId')
        print(bot_id)
        symbol = Symbol.objects.get(id=bot_id)
        symbol.delete()

        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@csrf_exempt
def save_settings(request):
    if request.method == 'POST':
        # Access the values sent via AJAX
        profile = Profile.objects.get(user=request.user)
        profile.api_key = request.POST.get('api_key')
        profile.secret_key = request.POST.get('secret_key')
        profile.broker = request.POST.get('broker')
        profile.max_trade = request.POST.get('max_trades')
        profile.time_frame = request.POST.get('timeframe')
        profile.order_size = request.POST.get('order_size')
        profile.risk_reward = request.POST.get('risk_reward')
        profile.order_type = request.POST.get('order_type')

        strategy_status = json.loads(request.POST.get('strategyStatus'))
        print(strategy_status)
        for strategy_id, checked in strategy_status.items():
            if strategy_id == '1':
                profile.dare_to_trade = checked
                print('1')
            if strategy_id == '2':
                profile.price_action = checked
                print('2')
            if strategy_id == '3':
                profile.camarilla = checked
            if strategy_id == '4':
                profile.fibonacci = checked
        profile.save()

        print(request.POST.get('strategyStatus')[1])
        return JsonResponse({'message': 'Settings saved successfully.'})

def calcAccount(request):
    profile = Profile.objects.get(user=request.user)
    closed_conditions = {'owner': profile, 'status__in': ['CLOSED']}
    closed_trades = Trades.objects.filter(**closed_conditions).order_by('-id')

    if closed_trades.exists():
        last_closed_trade_id = closed_trades.first().id
        new_closed_trades = closed_trades.filter(id__gt=profile.last_closed_trade_id)
        profile.last_closed_trade_id = last_closed_trade_id
        profile.no_of_total_trades += new_closed_trades.count()

        for trade in new_closed_trades:
            profile.net_profit += trade.profit
            if trade.profit > 0:
                profile.no_of_profit_trades += 1
            else:
                profile.no_of_loss_trades += 1

            if "Buy" in trade.order_type:
                profile.no_of_long_positions += 1
                if trade.profit > 0:
                    profile.long_positions_won += 1

            if "Sell" in trade.order_type:
                profile.no_of_short_positions += 1
                if trade.profit > 0:
                    profile.short_positions_won += 1

        profile.account_balance = (profile.initial_deposit + profile.net_profit) - profile.withdrawal
        profile.total_win_rate = (profile.no_of_profit_trades / profile.no_of_total_trades) * 100 if profile.no_of_total_trades else 0.0
        profile.short_positions_won_perc = (profile.short_positions_won / profile.no_of_short_positions) * 100 if profile.no_of_short_positions else 0.0
        profile.long_positions_won_perc = (profile.long_positions_won / profile.no_of_long_positions) * 100 if profile.no_of_long_positions else 0.0
        profile.save()

    return JsonResponse({'success': True})

def calcprofit(request):
    profile = Profile.objects.get(user=request.user)
    closed_conditions = {'owner': profile, 'status__in': ['CLOSED']}
    closed_trades = Trades.objects.filter(**closed_conditions)

    result = [['0', profile.initial_deposit]]
    previous_value = profile.initial_deposit
    for trade in closed_trades:
        month = trade.id
        profit = trade.profit + previous_value
        result.append([month, profit])
        previous_value = profit

    return JsonResponse(result, safe=False)

