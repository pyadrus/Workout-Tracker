# Основной файл Telegram-бота, использующего aiogram для взаимодействия с пользователями.
# В этом файле создается логика обработки сообщений и FSM (Finite State Machine) для регистрации пользователей.

import json
from pathlib import Path

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from bot.database.database import (
    get_user_data,  # Импорт функции получения авторизованного пользователя из базы
    add_user_starting_the_bot,  # Импорт функции добавления не авторизованного пользователя
)
from bot.keyboards.keyboards import (
    generate_authorized_user_discription,
    generate_authorized_user_options_keyboard,
    generate_user_options_keyboard,  # Импорт функции для создания клавиатуры.
    generate_admin_button,
)
from bot.data.config import ADMIN_USER_ID

main_router = Router()  # Создание маршрутизатора для обработки команд и сообщений.


# Чтение файла json для выборки текстов
def load_text_form_file(file_name):
    file_path = Path(f"bot/messages/{file_name}")
    if (
        file_path.exists()
    ):  # возвращает true , если объект файловой системы существует, и false – если нет
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)  # Загружаем строку текста
    return "Файл не найден!"


# Обработчик команды /start, отправляющий приветственное сообщение и клавиатуру с вариантами.
@main_router.message(CommandStart())
async def start_bot_command(message: Message) -> None:
    """
    Отправляет приветственное сообщение пользователю при старте бота.
    Так же добавляет не авторизованного пользователя в таблицу.

    Аргументы:
    :param message: Сообщение пользователя с командой /start.
    """
    telegram_user_data: dict[str, str] = (
        dict()
    )  # В словаре хранятся данные пользователя из телеграмм.
    for key, value in message.from_user:
        telegram_user_data[key] = value

    user_data_from_database = get_user_data(telegram_user_data["id"])
    if not user_data_from_database:
        await message.answer(
            f"{load_text_form_file('text_hello_welcome.json')}",
            reply_markup=generate_user_options_keyboard(),
        )

        add_user_starting_the_bot(
            id_user=telegram_user_data["id"],
            is_bot=telegram_user_data["is_bot"],
            first_name=telegram_user_data["first_name"],
            last_name=telegram_user_data["last_name"],
            username=telegram_user_data["username"],
            language_code=telegram_user_data["language_code"],
            is_premium=telegram_user_data["is_premium"],
            added_to_attachment_menu=telegram_user_data["added_to_attachment_menu"],
            can_join_groups=telegram_user_data["can_join_groups"],
            can_read_all_group_messages=telegram_user_data[
                "can_read_all_group_messages"
            ],
            supports_inline_queries=telegram_user_data["supports_inline_queries"],
            can_connect_to_business=telegram_user_data["can_connect_to_business"],
            has_main_web_app=telegram_user_data["has_main_web_app"],
        )  # Добавление пользователя при запуске бота.

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


@main_router.callback_query(F.data == "description")
async def bot_description(callback_query: CallbackQuery) -> None:
    """
    Отправляет описание бота пользователю.

    Аргументы:
    :param message: Сообщение пользователя с текстом "описание".
    """
    await callback_query.message.edit_text(
        f"{load_text_form_file('text_description.json')}",
        reply_markup=generate_authorized_user_discription(),
    )
