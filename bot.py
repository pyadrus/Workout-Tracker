# Код для запуска Telegram-бота с использованием aiogram.
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from data.config import BOT_TOKEN  # Импорт токена бота из файла конфигурации.
from handlers.start import router  # Импорт маршрутизатора с обработчиками.
from handlers.personal_acount import routerr  # Импорт маршрутизатора с обработчиками.
from handlers.registration_user import (
    routerrrr,
)  # Импорт маршрутизатора с обработчиками.


async def main() -> None:
    """
    Основная асинхронная функция для запуска бота.

    Создает экземпляр бота, регистрирует маршрутизаторы и запускает процесс опроса обновлений (polling).
    """
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = (
        Dispatcher()
    )  # Создание диспетчера для управления маршрутизацией и обработкой событий.
    dp.include_router(
        router
    )  # Подключение маршрутизаторов с обработчиками команд и сообщений.
    dp.include_router(routerr)
    dp.include_router(routerrrr)
    await dp.start_polling(bot)  # Запуск опроса обновлений.


asyncio.run(main())  # Запуск основного цикла бота.
