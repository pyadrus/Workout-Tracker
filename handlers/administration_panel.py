from aiogram import F, Router
from aiogram.types import CallbackQuery

from handlers.start import ADMIN_USER_ID, load_text_form_file
from database.database import (
    get_user_data,  # Импорт функции получения пользователя из базы
)
from keyboards.keyboards import (
    generate_admin_panel_keyboard,
    generate_admin_button,
)

routerrrrrrrrr = Router()  # Создание маршрутизатора для обработки команд и сообщений.


# Обработчик состояния админской-панели
@routerrrrrrrrr.callback_query(F.data == "admin_panel")
async def login_to_the_admin_panel(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer(
        "Админ-панель", reply_markup=generate_admin_panel_keyboard()
    )


# Обработчик состояния рассылка сообщений пользователям
@routerrrrrrrrr.callback_query(F.data == "sending_messages")
async def sending_messages_by_user(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer("Разослать сообщения")


# Обработчик состояния статистики
@routerrrrrrrrr.callback_query(F.data == "statistics")
async def user_activity_analysis(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer("Статистика")
