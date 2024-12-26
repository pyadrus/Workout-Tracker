# Код для запуска Telegram-бота с использованием aiogram.
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from loguru import logger

from bot.data.config import BOT_TOKEN  # Импорт токена бота из файла конфигурации.
from bot.handlers.admin import router
from bot.handlers.exercises.main import register_exercises
from bot.handlers.exercises.muscles.biceps import register_biceps
from bot.handlers.exercises.muscles.pectoral import register_pectoral
from bot.handlers.exercises.muscles.triceps import register_triceps
from bot.handlers.user.today import register_today
from bot.handlers.user.help import register_help
from bot.handlers.user.menu import register_menu
from bot.handlers.user.training import register_training
from bot.handlers.user.workout import register_workout

logger.add("logs/log.log")


async def start_bot() -> None:
    """
    Основная асинхронная функция для запуска бота.

    Создает экземпляр бота, регистрирует маршрутизаторы и запускает процесс опроса обновлений (polling).
    """
    try:
        global bot
        bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        # Создание диспетчера для управления маршрутизацией и обработкой событий.
        dp = Dispatcher()
        # Подключение маршрутизаторов с обработчиками команд и сообщений.
        dp.include_router(router)

        register_triceps()  # Упражнения на трицепс
        register_biceps()  # Упражнения на бицепс
        register_help()  # Помощь
        register_menu()
        register_workout()  # Запись тренировки в базу данных
        register_training()  # Программа тренировки
        register_today()  # Получение данных тренировок за сегодня

        register_exercises()  # Перечень упражнений для группы мышц
        register_pectoral()  # Перечень упражнений на Грудные мышцы

        await dp.start_polling(bot)  # Запуск опроса обновлений.
    except Exception as error:
        logger.exception(error)


if __name__ == "__main__":
    asyncio.run(start_bot())  # Запуск основного цикла бота.
