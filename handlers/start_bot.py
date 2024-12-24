# Основной файл Telegram-бота, использующего aiogram для взаимодействия с пользователями.
# В этом файле создается логика обработки сообщений и FSM (Finite State Machine) для регистрации пользователей.

import json
from pathlib import Path

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message
from dotenv import load_dotenv
import os

from database.database import (
    get_user_data,  # Импорт функции получения пользователя из базы
    add_user_starting_the_bot,  # Импорт функции добавления не авторизованного пользователя
)
from keyboards.keyboards import (
    generate_authorized_user_discription,
    generate_authorized_user_options_keyboard,
    generate_user_options_keyboard,  # Импорт функции для создания клавиатуры.
    generate_admin_button,
)

router = Router()  # Создание маршрутизатора для обработки команд и сообщений.

load_dotenv()

ADMIN_USER_ID = os.getenv("ADMIN_ID")


# Чтение файла json для выборки текстов
def load_text_form_file(file_name):
    file_path = Path(f"messages/{file_name}")
    if (
        file_path.exists()
    ):  # возвращает true , если объект файловой системы существует, и false – если нет
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)  # Загружаем строку текста
    return "Файл не найден!"


# Обработчик команды /start, отправляющий приветственное сообщение и клавиатуру с вариантами.
@router.message(CommandStart())
async def start_bot(message: Message) -> None:
    """
    Отправляет приветственное сообщение пользователю при старте бота.
    Так же добавляет не авторизованного пользователя в таблицу.

    Аргументы:
    :param message: Сообщение пользователя с командой /start.
    """
    user_data = dict()  # В словаре хранятся данные пользователя из телеграмм.
    for key, value in message.from_user:
        user_data[key] = value

    add_user_starting_the_bot(
        id_user=user_data["id"],
        is_bot=user_data["is_bot"],
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        username=user_data["username"],
        language_code=user_data["language_code"],
        is_premium=user_data["is_premium"],
        added_to_attachment_menu=user_data["added_to_attachment_menu"],
        can_join_groups=user_data["can_join_groups"],
        can_read_all_group_messages=user_data["can_read_all_group_messages"],
        supports_inline_queries=user_data["supports_inline_queries"],
        can_connect_to_business=user_data["can_connect_to_business"],
        has_main_web_app=user_data["has_main_web_app"],
    )

    data_user = get_user_data(user_data["id"])
    if not data_user:
        await message.answer(
            f"{load_text_form_file('text_hello_welcome.json')}",
            reply_markup=generate_user_options_keyboard(),
        )
    else:
        if get_user_data(ADMIN_USER_ID):
            await message.answer(
                f"{load_text_form_file('text_authorized_user_greeting.json')}",
                reply_markup=generate_admin_button(),
            )
        else:
            await message.answer(
                f"{load_text_form_file('text_authorized_user_greeting.json')}",
                reply_markup=generate_authorized_user_options_keyboard(),
            )


@router.callback_query(F.data == "description")
async def description(callback_query: CallbackQuery) -> None:
    """
    Отправляет описание бота пользователю.

    Аргументы:
    :param message: Сообщение пользователя с текстом "описание".
    """
    await callback_query.message.edit_text(
        f"{load_text_form_file('text_description.json')}",
        reply_markup=generate_authorized_user_discription(),
    )
