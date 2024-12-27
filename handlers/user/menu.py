from datetime import datetime

import yaml
from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery
from aiogram.types import Message
from loguru import logger

from data.config import ADMIN_USER_ID
from data.config import router, bot
from database.database import add_user_starting_the_bot, check_for_bot_launch, is_user_authorized
from keyboards.keyboard_user.keyboards import (generate_authorized_user_discription, generate_main_menu_keyboard,
                                               generate_admin_button, registration_keyboard)

with open("messages/text/messages.yaml", "r", encoding="utf-8") as file:
    messages = yaml.safe_load(file)

menu_text = messages["menu"]["text"]
text_admin_panel = messages["text_admin_panel"]["text"]
text_description = messages["text_description"]["text"]
messages = "Привет админ"


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    """Обработчик команды /start

    Отправляет приветственное сообщение пользователю при старте бота.
    Так же добавляет не авторизованного пользователя в таблицу.
    """
    try:
        user_id = message.from_user.id

        # Проверяем, зарегистрирован ли пользователь
        if not is_user_authorized(user_id):
            logger.info(f"Пользователь {user_id} не зарегистрирован")
            await message.answer(
                "Вы не зарегистрированы. Пожалуйста, пройдите регистрацию, чтобы продолжить.",
                reply_markup=registration_keyboard(),  # Кнопка для начала регистрации
                parse_mode="HTML",
            )

        # # Проверяем ID администратора
        # if user_id == ADMIN_USER_ID:
        #     logger.info(f"Пользователь {user_id} авторизован")
        #
        #     await message.answer(messages, reply_markup=generate_admin_button(), parse_mode="HTML")
        #     return
        #
        # if check_for_bot_launch(user_id):
        #     # Запись пользователя в базу данных, который ввел команду /start
        #     add_user_starting_the_bot(
        #         id_user=message.from_user.id,
        #         is_bot=message.from_user.is_bot or "",
        #         first_name=message.from_user.first_name or "",
        #         last_name=message.from_user.last_name or "",
        #         username=message.from_user.username or "",
        #         language_code=message.from_user.language_code or "",
        #         is_premium=message.from_user.is_premium or "",
        #         added_to_attachment_menu=message.from_user.added_to_attachment_menu or "",
        #         can_join_groups=message.from_user.can_join_groups or "",
        #         can_read_all_group_messages=message.from_user.can_read_all_group_messages or "",
        #         supports_inline_queries=message.from_user.supports_inline_queries or "",
        #         can_connect_to_business=message.from_user.can_connect_to_business or "",
        #         has_main_web_app=message.from_user.has_main_web_app or "",
        #         user_date=message.date.strftime("%Y-%m-%d %H:%M:%S")
        #     )
        #
        #     await message.answer(menu_text, reply_markup=generate_main_menu_keyboard(), parse_mode="HTML")
        # else:
        #     # Запись пользователя в базу данных, который ввел команду /start
        #     add_user_starting_the_bot(
        #         id_user=message.from_user.id,
        #         is_bot=message.from_user.is_bot or "",
        #         first_name=message.from_user.first_name or "",
        #         last_name=message.from_user.last_name or "",
        #         username=message.from_user.username or "",
        #         language_code=message.from_user.language_code or "",
        #         is_premium=message.from_user.is_premium or "",
        #         added_to_attachment_menu=message.from_user.added_to_attachment_menu or "",
        #         can_join_groups=message.from_user.can_join_groups or "",
        #         can_read_all_group_messages=message.from_user.can_read_all_group_messages or "",
        #         supports_inline_queries=message.from_user.supports_inline_queries or "",
        #         can_connect_to_business=message.from_user.can_connect_to_business or "",
        #         has_main_web_app=message.from_user.has_main_web_app or "",
        #         user_date=message.date.strftime("%Y-%m-%d %H:%M:%S")
        #     )
        #
        #     await message.answer(menu_text, reply_markup=generate_main_menu_keyboard())
    except Exception as e:
        logger.error(f"Ошибка в обработчике /start: {e}")


@router.callback_query(F.data == "description")
async def bot_description(callback_query: CallbackQuery) -> None:
    """
    Отправляет описание бота пользователю.

    Аргументы:
    :param callback_query: Кнопка с текстом "описание".
    """
    await callback_query.message.edit_text(text_description, reply_markup=generate_authorized_user_discription(),
                                           parse_mode="HTML")


@router.callback_query(F.data == "start_handler")
async def start_handler_callback(callback_query: types.CallbackQuery) -> None:
    """Главное меню."""
    try:
        add_user_starting_the_bot(id_user=callback_query.from_user.id,
                                  is_bot=callback_query.from_user.is_bot or "",
                                  first_name=callback_query.from_user.first_name or "",
                                  last_name=callback_query.from_user.last_name or "",
                                  username=callback_query.from_user.username or "",
                                  language_code=callback_query.from_user.language_code or "",
                                  is_premium=callback_query.from_user.is_premium or "",
                                  added_to_attachment_menu=callback_query.from_user.added_to_attachment_menu or "",
                                  can_join_groups=callback_query.from_user.can_join_groups or "",
                                  can_read_all_group_messages=callback_query.from_user.can_read_all_group_messages or "",
                                  supports_inline_queries=callback_query.from_user.supports_inline_queries or "",
                                  can_connect_to_business=callback_query.from_user.can_connect_to_business or "",
                                  has_main_web_app=callback_query.from_user.has_main_web_app or "",
                                  user_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Если нужно отправить новое сообщение:
        await bot.send_message(chat_id=callback_query.message.chat.id,
                               text=menu_text,
                               reply_markup=generate_main_menu_keyboard())

    except Exception as e:
        logger.error(f"Ошибка: {e}")


def register_menu():
    """Регистрация обработчиков для бота"""
    router.message.register(start_handler)  # Главное меню бота
    router.callback_query.register(start_handler_callback)  # Главное меню бота
    router.callback_query.add_callback(bot_description)
