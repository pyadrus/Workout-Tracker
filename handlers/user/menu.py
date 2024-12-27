from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery
from aiogram.types import Message
from loguru import logger
from datetime import datetime
from data.config import ADMIN_USER_ID
from data.config import router, bot
from database.database import get_user_data, add_user_starting_the_bot, check_for_bot_launch
from keyboards.keyboard_user.keyboards import (generate_authorized_user_discription, generate_main_menu_keyboard,
                                               generate_admin_button)
from utils.read_text import load_text_form_file
import yaml

with open("messages/text/messages.yaml", "r", encoding="utf-8") as file:
    messages = yaml.safe_load(file)

menu_text = messages["menu"]["text"]


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    """Обработчик команды /start

    Отправляет приветственное сообщение пользователю при старте бота.
    Так же добавляет не авторизованного пользователя в таблицу.
    Обработчик команды /start, отправляющий приветственное сообщение и клавиатуру с вариантами.
    Аргументы:
    :param message: Сообщение пользователя с командой /start.
    """
    try:
        user_id = message.from_user.id
        if check_for_bot_launch(user_id):
            # await message.answer(
            #     f"{load_text_form_file('text_authorized_user_greeting.json')}",
            #     reply_markup=generate_admin_button() if user_id == ADMIN_USER_ID else generate_user_options_keyboard(),
            # )
            # Запись пользователя в базу данных, который ввел команду /start
            add_user_starting_the_bot(
                id_user=message.from_user.id,
                is_bot=message.from_user.is_bot or "",
                first_name=message.from_user.first_name or "",
                last_name=message.from_user.last_name or "",
                username=message.from_user.username or "",
                language_code=message.from_user.language_code or "",
                is_premium=message.from_user.is_premium or "",
                added_to_attachment_menu=message.from_user.added_to_attachment_menu or "",
                can_join_groups=message.from_user.can_join_groups or "",
                can_read_all_group_messages=message.from_user.can_read_all_group_messages or "",
                supports_inline_queries=message.from_user.supports_inline_queries or "",
                can_connect_to_business=message.from_user.can_connect_to_business or "",
                has_main_web_app=message.from_user.has_main_web_app or "",
                user_date=message.date.strftime("%Y-%m-%d %H:%M:%S")
            )

            await message.answer(menu_text, reply_markup=generate_main_menu_keyboard(), parse_mode="HTML")

        else:

            if get_user_data(ADMIN_USER_ID):

                await message.answer(f"{load_text_form_file('messages/text/text_authorized_user_greeting.json')}",
                                     reply_markup=generate_admin_button(),
                                     )
            else:
                # Запись пользователя в базу данных, который ввел команду /start
                add_user_starting_the_bot(
                    id_user=message.from_user.id,
                    is_bot=message.from_user.is_bot or "",
                    first_name=message.from_user.first_name or "",
                    last_name=message.from_user.last_name or "",
                    username=message.from_user.username or "",
                    language_code=message.from_user.language_code or "",
                    is_premium=message.from_user.is_premium or "",
                    added_to_attachment_menu=message.from_user.added_to_attachment_menu or "",
                    can_join_groups=message.from_user.can_join_groups or "",
                    can_read_all_group_messages=message.from_user.can_read_all_group_messages or "",
                    supports_inline_queries=message.from_user.supports_inline_queries or "",
                    can_connect_to_business=message.from_user.can_connect_to_business or "",
                    has_main_web_app=message.from_user.has_main_web_app or "",
                    user_date=message.date.strftime("%Y-%m-%d %H:%M:%S")
                )

                await message.answer(menu_text, reply_markup=generate_main_menu_keyboard())
    except Exception as e:
        logger.error(f"Ошибка в обработчике /start: {e}")


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
