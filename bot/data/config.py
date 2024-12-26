import os
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from loguru import logger

# Загрузка переменных окружения
load_dotenv(dotenv_path="system/.env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    logger.error("BOT_TOKEN не найден в .env файле!")
    sys.exit("Укажите BOT_TOKEN в .env файле.")

# Инициализация бота, диспетчера и хранилища
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Создание маршрутизатора
router = Router()
dp.include_router(router)

load_dotenv()  # Загружаем переменные из .env файла

BOT_TOKEN = os.getenv("TOKEN")  # Получаем токен бота из переменной окружения

ADMIN_USER_ID = os.getenv("ADMIN_ID")

BASE_SITE_URL = os.getenv("BASE_SITE")

logger.info(BOT_TOKEN)  # Проверка, что токен загружен

router = Router()  # Создание маршрутизатора для обработки команд и сообщений.
