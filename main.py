import asyncio
from bot.run_bot import start_bot
from WebApp.main import start_web


async def main() -> None:
    # await asyncio.gather(
    #     start_bot(),
    #     start_web(),
    # )

    telegram_task = asyncio.create_task(start_bot())
    webapp_task = asyncio.create_task(start_web())
    await asyncio.gather(telegram_task, webapp_task)


if __name__ == "__main__":
    asyncio.run(main())
