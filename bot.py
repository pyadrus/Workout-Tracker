import asyncio
import logging
import sys

from loguru import logger

from data.config import dp, bot  # Импорт токена бота из файла конфигурации.
from handlers.exercises.exercises_menu import register_exercises
from handlers.exercises.muscles.biceps import register_biceps
from handlers.exercises.muscles.pectoral import register_pectoral
from handlers.exercises.muscles.triceps import register_triceps
from handlers.user.description import register_description
from handlers.user.help import register_help
from handlers.user.menu import register_menu
from handlers.user.registration import register_registration_user
from handlers.user.today import register_today
from handlers.user.training import register_training
from handlers.user.workout import register_workout


async def start_bot() -> None:
    """
    Основная асинхронная функция для запуска бота.

    Создает экземпляр бота, регистрирует маршрутизаторы и запускает процесс опроса обновлений (polling).
    """
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        await dp.start_polling(bot)

        register_menu()  # Главное меню

        register_registration_user()  # Регистрация пользователя, если пользователь не зарегистрирован в боте

        register_description()  # Описание
        register_triceps()  # Упражнения на трицепс
        register_biceps()  # Упражнения на бицепс
        register_help()  # Помощь
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
