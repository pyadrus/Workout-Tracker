# Код для запуска Telegram-бота с использованием aiogram.
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from loguru import logger

from data.config import BOT_TOKEN  # Импорт токена бота из файла конфигурации.
from handlers.admin import router
from handlers.exercises.main import register_exercises
from handlers.exercises.muscles.biceps import register_biceps
from handlers.exercises.muscles.pectoral import register_pectoral
from handlers.exercises.muscles.triceps import register_triceps
from handlers.user.today import register_today
from handlers.user.help import register_help
from handlers.user.menu import register_menu
from handlers.user.training import register_training
from handlers.user.workout import register_workout

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
