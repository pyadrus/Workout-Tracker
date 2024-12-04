# Код для запуска Telegram-бота с использованием aiogram.
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from loguru import logger

from data.config import BOT_TOKEN  # Импорт токена бота из файла конфигурации.
from handlers.start import router  # Импорт маршрутизатора с обработчиками.

logger.add("log/log.log")


async def main() -> None:
    """
    Основная асинхронная функция для запуска бота.

    Создает экземпляр бота, регистрирует маршрутизаторы и запускает процесс опроса обновлений (polling).
    """
    try:
        bot = Bot(
            token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
        dp = (
            Dispatcher()
        )  # Создание диспетчера для управления маршрутизацией и обработкой событий.
        dp.include_router(
            router
        )  # Подключение маршрутизаторов с обработчиками команд и сообщений.
        await dp.start_polling(bot)  # Запуск опроса обновлений.
    except Exception as error:
        logger.exception(error)


asyncio.run(main())  # Запуск основного цикла бота.
