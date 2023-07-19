from channels.generic.websocket import AsyncWebsocketConsumer
from edwizy_app.bot.bot import *
from edwizy_app.bot.trading import *
from edwizy_app.models import Trades, Profile, Symbol, Strategies
import json

class StrategyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Process incoming WebSocket messages from the frontend
        data = json.loads(text_data)
        if data['action'] == 'get_active_symbols':
            await self.get_active_symbols()
        # Handle other actions as needed

    async def get_active_symbols(self):
        active_symbols_data = await get_active_symbols()

        for symbol, dataframe in active_symbols_data.items():
            result, strategy_names = await check_strategies(dataframe)
            if result:
                for strategy_name, order_type in strategy_names:
                    message = f"Strategy '{strategy_name}' returned True to {order_type} for symbol: {symbol}"
                    await self.send(text_data=json.dumps({'message': message}))
