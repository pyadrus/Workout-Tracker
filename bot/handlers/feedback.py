from aiogram import F, Router
from aiogram.types import CallbackQuery
from bot.utils.read_text import load_text_form_file

router_feedback = Router()  # Создание маршрутизатора для обработки команд и сообщений.


@router_feedback.callback_query(F.data == "feedback")
async def get_feedback(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer(f"{load_text_form_file('text_feedback.json')}")
