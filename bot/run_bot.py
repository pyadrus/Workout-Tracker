# Код для запуска Telegram-бота с использованием aiogram.
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from loguru import logger

from bot.data.config import BOT_TOKEN  # Импорт токена бота из файла конфигурации.
from bot.handlers.feedback import router
from bot.handlers.personal_acount import router_personal_acount
from bot.handlers.registration_user import router
from bot.handlers.launch_bot import router_main
from bot.handlers.administration_panel import router
from bot.handlers.types_of_exercises_for_muscle_groups_handlers.exercise_handlers import \
    register_types_of_exercises_for_muscle_groups_handlers
from bot.handlers.types_of_exercises_for_muscle_groups_handlers.exercises_handlers.biceps_exercises_handlers import \
    register_biceps_exercises_handlers
from bot.handlers.types_of_exercises_for_muscle_groups_handlers.exercises_handlers.pectoral_muscles_exercises_handlers import \
    register_exercises_for_the_pectoral_muscles
from bot.handlers.types_of_exercises_for_muscle_groups_handlers.exercises_handlers.triceps_exercises_handlers import \
    register_diamond_push_ups_handlers
from bot.handlers.user_handlers.get_today_data_handler import register_get_today_data_handler
from bot.handlers.user_handlers.help_handlers import register_help_command_handlers
from bot.handlers.user_handlers.menu_handlers import register_start_handler_handlers
from bot.handlers.user_handlers.training_program_handlers import register_training_program
from bot.handlers.user_handlers.workout_recording_handlers import register_workout_recording_handlers

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
        dp.include_router(router)
        dp.include_router(router)
        dp.include_router(router_personal_acount)
        dp.include_router(router)

        register_diamond_push_ups_handlers()  # Упражнения на трицепс
        register_biceps_exercises_handlers()  # Упражнения на бицепс
        register_help_command_handlers()  # Помощь
        register_start_handler_handlers()
        register_workout_recording_handlers()  # Запись тренировки в базу данных
        register_training_program()  # Программа тренировки
        register_get_today_data_handler()  # Получение данных тренировок за сегодня

        register_types_of_exercises_for_muscle_groups_handlers()  # Перечень упражнений для группы мышц
        register_exercises_for_the_pectoral_muscles()  # Перечень упражнений на Грудные мышцы

        await dp.start_polling(bot)  # Запуск опроса обновлений.
    except Exception as error:
        logger.exception(error)


if __name__ == "__main__":
    asyncio.run(start_bot())  # Запуск основного цикла бота.
