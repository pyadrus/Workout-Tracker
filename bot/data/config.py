import os

from aiogram import Router
from dotenv import load_dotenv
from loguru import logger

load_dotenv()  # Загружаем переменные из .env файла

BOT_TOKEN = os.getenv("TOKEN")  # Получаем токен бота из переменной окружения

ADMIN_USER_ID = os.getenv("ADMIN_ID")

BASE_SITE_URL = os.getenv("BASE_SITE")

logger.info(BOT_TOKEN)  # Проверка, что токен загружен


# Создание маршрутизатора для обработки команд и сообщений.
router_administration_panel = (Router())


router_feedback = Router()  # Создание маршрутизатора для обработки команд и сообщений.


router_main = Router()  # Создание маршрутизатора для обработки команд и сообщений.
