

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import http.client
import json
import pandas as pd
from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect
import pyotp


api_key = '919fab386d944600bae6fb8ad1bca47c'
clientId = 'JS5aC43B'
pwd = 'Your Pin'
smartApi = SmartConnect(api_key)


current_date = datetime.now().date()
start_date = current_date - timedelta(days=7)
start_date_str = start_date.strftime('%Y-%m-%d')
current_date_str = current_date.strftime('%Y-%m-%d')

def get_angel_intraday_chart():
    #Historic api
    try:
        historicParam={
        "exchange": "NSE",
        "symboltoken": "19441",
        "interval": "ONE_MINUTE",
        "fromdate": "2021-02-08 09:00", 
        "todate": "2021-02-08 09:16"
        }
        data = smartApi.getCandleData(historicParam)
        print(data)
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))

