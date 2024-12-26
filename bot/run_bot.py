# Код для запуска Telegram-бота с использованием aiogram.
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from loguru import logger

from bot.data.config import BOT_TOKEN  # Импорт токена бота из файла конфигурации.
from bot.handlers.admin import router
from bot.handlers.exercises.main import register_exercises
from bot.handlers.exercises.muscles.biceps import register_biceps_exercises_handlers
from bot.handlers.exercises.muscles.pectoral import register_exercises_for_the_pectoral_muscles
from bot.handlers.exercises.muscles.triceps import register_diamond_push_ups_handlers
from bot.handlers.user.today import register_get_today_data_handler
from bot.handlers.user.help import register_help_command_handlers
from bot.handlers.user.menu import register_start_handler_handlers
from bot.handlers.user.training import register_training_program
from bot.handlers.user.workout import register_workout_recording_handlers

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

        register_diamond_push_ups_handlers()  # Упражнения на трицепс
        register_biceps_exercises_handlers()  # Упражнения на бицепс
        register_help_command_handlers()  # Помощь
        register_start_handler_handlers()
        register_workout_recording_handlers()  # Запись тренировки в базу данных
        register_training_program()  # Программа тренировки
        register_get_today_data_handler()  # Получение данных тренировок за сегодня

        register_exercises()  # Перечень упражнений для группы мышц
        register_exercises_for_the_pectoral_muscles()  # Перечень упражнений на Грудные мышцы

        await dp.start_polling(bot)  # Запуск опроса обновлений.
    except Exception as error:
        logger.exception(error)


if __name__ == "__main__":
    asyncio.run(start_bot())  # Запуск основного цикла бота.
