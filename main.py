import asyncio
import logging
import sys

from loguru import logger

from bot import start_bot

# Настройка логов
logger.add("log/log.log", retention="1 days", enqueue=True)


# Основная функция запуска бота
async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:

        telegram_task = asyncio.create_task(start_bot())
        await asyncio.gather(telegram_task)
    except Exception as e:
        logger.error(f"Ошибка в main(): {e}")


if __name__ == "__main__":
    asyncio.run(main())
