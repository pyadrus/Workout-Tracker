# Основной файл Telegram-бота, использующего aiogram для взаимодействия с пользователями.
# В этом файле создается логика обработки сообщений и FSM (Finite State Machine) для регистрации пользователей.
from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery
from aiogram.types import Message
from loguru import logger

from data.config import ADMIN_USER_ID
from data.config import router, bot
from database.database import (get_user_data,  # Импорт функции получения авторизованного пользователя из базы
                               add_user_starting_the_bot,  # Импорт функции добавления не авторизованного пользователя
                               )
from keyboards.keyboard_user.keyboard_menu import keyboard_menu
from keyboards.keyboards import (generate_authorized_user_discription, generate_authorized_user_options_keyboard,
                                 generate_user_options_keyboard, generate_admin_button)
from utils.read_text import load_text_form_file


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    """Обработчик команды /start"""
    try:
        logger.info(f"{message}")
        user_id = message.from_user.id
        user_name = message.from_user.username or ""
        user_first_name = message.from_user.first_name or ""
        user_last_name = message.from_user.last_name or ""
        user_date = message.date.strftime("%Y-%m-%d %H:%M:%S")

        is_bot = message.from_user.is_bot
        language_code = message.from_user.language_code
        is_premium = message.from_user.is_premium
        added_to_attachment_menu = message.from_user.added_to_attachment_menu
        can_join_groups = message.from_user.can_join_groups
        can_read_all_group_messages = message.from_user.can_read_all_group_messages
        supports_inline_queries = message.from_user.supports_inline_queries
        can_connect_to_business = message.from_user.can_connect_to_business
        has_main_web_app = message.from_user.has_main_web_app

        logger.info(f"User Info: {user_id}, {user_name}, {user_first_name}, {user_last_name}, {user_date}")

        add_user_starting_the_bot(id_user=user_id,
                                  is_bot=is_bot,
                                  first_name=user_first_name,
                                  last_name=user_last_name,
                                  username=user_name,
                                  language_code=language_code,
                                  is_premium=is_premium,
                                  added_to_attachment_menu=added_to_attachment_menu,
                                  can_join_groups=can_join_groups,
                                  can_read_all_group_messages=can_read_all_group_messages,
                                  supports_inline_queries=supports_inline_queries,
                                  can_connect_to_business=can_connect_to_business,
                                  has_main_web_app=has_main_web_app,
                                  )  # Добавление пользователя при запуске бота.

        menu_text = ("Привет! 💪 Я — твой персональный тренер в мире спорта! 🚀\n\n"

                     "Готов помочь тебе достичь новых высот и максимально эффективно тренироваться.\n\n"

                     "Неважно, хочешь ли ты увеличить силу, улучшить выносливость или просто поддерживать форму — я "
                     "здесь, чтобы помочь! Начнём тренировку? 😎")

        await message.answer(menu_text, reply_markup=keyboard_menu())
    except Exception as e:
        logger.error(f"Ошибка в обработчике /start: {e}")


@router.message(CommandStart())
async def start_bot_command(message: Message) -> None:
    """
    Отправляет приветственное сообщение пользователю при старте бота.
    Так же добавляет не авторизованного пользователя в таблицу.
    Обработчик команды /start, отправляющий приветственное сообщение и клавиатуру с вариантами.
    Аргументы:
    :param message: Сообщение пользователя с командой /start.
    """
    telegram_user_data: dict[str, str] = (dict())  # В словаре хранятся данные пользователя из телеграмм.
    for key, value in message.from_user:
        telegram_user_data[key] = value

    if not get_user_data(telegram_user_data["id"]):
        await message.answer(f"{load_text_form_file('text_hello_welcome.json')}",
                             reply_markup=generate_user_options_keyboard())

        add_user_starting_the_bot(id_user=telegram_user_data["id"],
                                  is_bot=telegram_user_data["is_bot"],
                                  first_name=telegram_user_data["first_name"],
                                  last_name=telegram_user_data["last_name"],
                                  username=telegram_user_data["username"],
                                  language_code=telegram_user_data["language_code"],
                                  is_premium=telegram_user_data["is_premium"],
                                  added_to_attachment_menu=telegram_user_data["added_to_attachment_menu"],
                                  can_join_groups=telegram_user_data["can_join_groups"],
                                  can_read_all_group_messages=telegram_user_data["can_read_all_group_messages"],
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


@router.callback_query(F.data == "description")
async def bot_description(callback_query: CallbackQuery) -> None:
    """
    Отправляет описание бота пользователю.

    Аргументы:
    :param callback_query: Кнопка с текстом "описание".
    """
    await callback_query.message.edit_text(f"{load_text_form_file('text_description.json')}",
                                           reply_markup=generate_authorized_user_discription())


@router.callback_query(F.data == "start_handler")
async def start_handler_callback(callback_query: types.CallbackQuery) -> None:
    """Главное меню."""
    try:
        user_id = callback_query.from_user.id
        user_name = callback_query.from_user.username or ""
        user_first_name = callback_query.from_user.first_name or ""
        user_last_name = callback_query.from_user.last_name or ""
        # Исправление: используем дату из сообщения
        user_date = callback_query.message.date.strftime("%Y-%m-%d %H:%M:%S")

        logger.info(f"User Info: {user_id}, {user_name}, {user_first_name}, {user_last_name}, {user_date}")

        menu_text = ("Привет! 💪 Я — твой персональный тренер в мире спорта! 🚀\n\n"

                     "Готов помочь тебе достичь новых высот и максимально эффективно тренироваться.\n\n"

                     "Неважно, хочешь ли ты увеличить силу, улучшить выносливость или просто поддерживать форму — я "
                     "здесь, чтобы помочь! Начнём тренировку? 😎")

        # Если нужно отправить новое сообщение:
        await bot.send_message(chat_id=callback_query.message.chat.id,
                               text=menu_text,
                               reply_markup=keyboard_menu())

    except Exception as e:
        logger.error(f"Ошибка: {e}")


def register_menu():
    """Регистрация обработчиков для бота"""
    router.message.register(start_handler)  # Главное меню бота
    router.callback_query.register(start_handler_callback)  # Главное меню бота
