from aiogram import F
from aiogram.types import CallbackQuery

from data.config import router
from keyboards.keyboard_user.keyboards import (generate_authorized_user_discription)
from utils.messages_loader import text_description


@router.callback_query(F.data == "description")
async def bot_description(callback_query: CallbackQuery) -> None:
    """
    Отправляет описание бота пользователю.

    Аргументы:
    :param callback_query: Кнопка с текстом "описание".
    """
    await callback_query.message.edit_text(text_description, reply_markup=generate_authorized_user_discription(),
                                           parse_mode="HTML")


def register_description():
    """Регистрация обработчиков для бота"""
    router.callback_query.add_callback(bot_description)
