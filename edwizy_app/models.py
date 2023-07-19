from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    broker = models.CharField(max_length=100)
    dare_to_trade = models.BooleanField(default=True)
    camarilla = models.BooleanField(default=True)
    price_action = models.BooleanField(default=True)
    fibonacci = models.BooleanField(default=True)
    api_key = models.TextField()
    secret_key = models.TextField()
    max_trade = models.IntegerField(default=5)
    time_frame = models.CharField(max_length=100, blank=True)
    order_type = models.CharField(max_length=100, blank=True)
    order_size = models.CharField(max_length=100, blank=True)
    risk_reward = models.CharField(max_length=100, blank=True)
    active_chart = models. CharField(max_length=100, blank=True)
    account_balance = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    initial_deposit = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    net_profit = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    withdrawal = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    no_of_profit_trades = models.IntegerField(default=0)
    no_of_loss_trades = models.IntegerField(default=0)
    no_of_total_trades = models.IntegerField(default=0)
    total_win_rate = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    no_of_short_positions = models.IntegerField(default=0)
    no_of_long_positions = models.IntegerField(default=0)
    short_positions_won =  models.DecimalField(default=0, decimal_places=2, max_digits=10)
    long_positions_won = models.IntegerField(default=0)
    short_positions_won_perc =  models.IntegerField(default=0)
    long_positions_won_perc =  models.DecimalField(default=0, decimal_places=2, max_digits=10)
    last_closed_trade_id = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user.username}"


class Strategies(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Symbol(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    security_id = models.CharField(max_length=100)
    exchange_segment = models.CharField(max_length=100)
    instrument_type = models.CharField(max_length=100)
    total_trades = models.CharField(max_length=100, default=0.00)
    win_rate = models.CharField(max_length=100, default=0.00)

    def __str__(self):
        return f"{self.name}"

class Trades(models.Model):
    OPEN = 'OPEN'
    PENDING = 'PENDING'
    CLOSED = 'CLOSED'

    STATUS_CHOICES = (
            (OPEN, 'OPEN'),
            (PENDING, 'PENDING'),
            (CLOSED, 'CLOSED')
    )
    trade_id = models.CharField(max_length=100, default=0)
    owner =  models.ManyToManyField(Profile)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING)
    symbol = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    order_type = models.CharField(max_length=100)
    order_size =  models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    stop_loss = models.CharField(max_length=100)
    take_profit = models.CharField(max_length=100)
    profit = models.IntegerField(default=0)
    trigger_timeframe = models.CharField(max_length=100)
    bot = models.ForeignKey(Strategies, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.symbol}"