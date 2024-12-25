# Код для запуска Telegram-бота с использованием aiogram.
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from loguru import logger

from bot.data.config import BOT_TOKEN  # Импорт токена бота из файла конфигурации.
from bot.handlers.feedback import router_feedback
from bot.handlers.personal_acount import routerr
from bot.handlers.registration_user import router_registration_user
from bot.handlers.launch_bot import (
    router_main,
)  # Импорт маршрутизатора с обработчиками.
from bot.handlers.administration_panel import routerrrrrrrrr

logger.add("logs/log.log")


async def start_bot() -> None:
    """
    Основная асинхронная функция для запуска бота.

    Создает экземпляр бота, регистрирует маршрутизаторы и запускает процесс опроса обновлений (polling).
    """
    try:
        global bot
        bot = Bot(
            token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
        # Создание диспетчера для управления маршрутизацией и обработкой событий.
        dp = Dispatcher()
        # Подключение маршрутизаторов с обработчиками команд и сообщений.
        dp.include_router(router_main)
        dp.include_router(router_feedback)
        dp.include_router(router_registration_user)
        dp.include_router(routerr)
        dp.include_router(routerrrrrrrrr)
        await dp.start_polling(bot)  # Запуск опроса обновлений.
    except Exception as error:
        logger.exception(error)


if __name__ == "__main__":
    asyncio.run(main())  # Запуск основного цикла бота.
