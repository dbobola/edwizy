from django_q.tasks import async_task
from edwizy_app.bot.trading import check_strategies_for_active_symbols

def run_check_strategies_for_active_symbols():
    async_task(check_strategies_for_active_symbols)
