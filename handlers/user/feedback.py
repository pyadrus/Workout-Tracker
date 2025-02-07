from aiogram import types, F

from data.config import router
from keyboards.keyboard_user.keyboard_menu import keyboard_start_handler
from utils.messages_loader import text_feedback


@router.callback_query(F.data == "feedback")
async def get_feedback(callback_query: types.CallbackQuery) -> None:
    """Обратная связь с разработчиком"""
    await callback_query.message.answer(text_feedback,
                                        reply_markup=keyboard_start_handler())


def register_get_feedback():
    """Регистрация обработчиков для бота."""
    router.callback_query.register(get_feedback)  # Обратная связь с разработчиком
