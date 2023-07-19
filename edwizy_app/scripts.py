import asyncio
from django_q.tasks import async_task
from edwizy_app.bot.trading import check_strategies_for_active_symbols


async def run_task():
    await async_task(check_strategies_for_active_symbols)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_task())


if __name__ == "__main__":
    main()
