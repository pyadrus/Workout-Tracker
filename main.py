# from WebApp.main import start_web
import asyncio
import logging
import sys

from loguru import logger

from bot.run_bot import start_bot
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

# Настройка логов
logger.add("log/log.log", retention="1 days", enqueue=True)

# Основная функция запуска бота
async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        register_diamond_push_ups_handlers()  # Упражнения на трицепс
        register_biceps_exercises_handlers()  # Упражнения на бицепс
        register_help_command_handlers()  # Помощь
        register_start_handler_handlers()
        register_workout_recording_handlers()  # Запись тренировки в базу данных
        register_training_program()  # Программа тренировки
        register_get_today_data_handler()  # Получение данных тренировок за сегодня

        register_types_of_exercises_for_muscle_groups_handlers()  # Перечень упражнений для группы мышц
        register_exercises_for_the_pectoral_muscles()  # Перечень упражнений на Грудные мышцы

        telegram_task = asyncio.create_task(start_bot())
        await asyncio.gather(telegram_task)
    except Exception as e:
        logger.error(f"Ошибка в main(): {e}")

if __name__ == "__main__":
    asyncio.run(main())
