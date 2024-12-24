import os

from dotenv import load_dotenv
from loguru import logger

load_dotenv()  # Загружаем переменные из .env файла

BOT_TOKEN = os.getenv("TOKEN")  # Получаем токен бота из переменной окружения

ADMIN_USER_ID = os.getenv("ADMIN_ID")

logger.info(BOT_TOKEN)  # Проверка, что токен загружен
