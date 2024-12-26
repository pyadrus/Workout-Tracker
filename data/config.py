import os
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from loguru import logger

# Загрузка переменных окружения
load_dotenv(dotenv_path="system/.env")  # Загружаем переменные из .env файла

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Получаем токен бота из переменной окружения
if not BOT_TOKEN:
    logger.error("BOT_TOKEN не найден в .env файле!")
    sys.exit("Укажите BOT_TOKEN в .env файле.")
logger.info(BOT_TOKEN)  # Проверка, что токен загружен

ADMIN_USER_ID = os.getenv("ADMIN_ID")

BASE_SITE_URL = os.getenv("BASE_SITE")

# Инициализация бота, диспетчера и хранилища
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()  # Создание маршрутизатора для обработки команд и сообщений.
dp.include_router(router)
