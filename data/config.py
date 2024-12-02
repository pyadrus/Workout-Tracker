# Файл со всеми параметрами, токен бота и данные подключения к БД
import os

from dotenv import load_dotenv

_ = load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
