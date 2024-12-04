from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

routerrrrrrr = Router()  # Создание маршрутизатора для обработки команд и сообщений.


@routerrrrrrr.callback_query(F.data == "feedback")
async def get_feedback(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer("Обратная связь на связи")
