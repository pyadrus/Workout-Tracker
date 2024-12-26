from aiogram import F
from aiogram.types import CallbackQuery

from bot.data.config import router_feedback
from bot.utils.read_text import load_text_form_file


@router_feedback.callback_query(F.data == "feedback")
async def get_feedback(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer(f"{load_text_form_file('text_feedback.json')}")
