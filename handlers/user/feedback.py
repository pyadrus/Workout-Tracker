from aiogram import types, F

from data.config import router
from utils.read_text import load_text_form_file


@router.callback_query(F.data == "feedback")
async def get_feedback(callback_query: types.CallbackQuery) -> None:
    """Обратная связь с разработчиком"""
    await callback_query.message.answer(f"{load_text_form_file('text_feedback.json')}")


def register_get_feedback():
    """Регистрация обработчиков для бота."""
    router.callback_query.register(get_feedback)  # Обратная связь с разработчиком
