from aiogram import types, F
from loguru import logger

from data.config import bot, router
from database.database import get_user_data_for_today
from keyboards.keyboard_user.keyboard_help import keyboard_help


@router.callback_query(F.data == "get_today")
async def get_today_data_handler(callback_query: types.CallbackQuery):
    """Получение данных тренировки за день"""
    try:
        user_id = callback_query.from_user.id
        result = await get_user_data_for_today(user_id)
        # Если нужно отправить новое сообщение:
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text=result,
            reply_markup=keyboard_help()
        )

    except Exception as e:
        logger.error(f"Ошибка: {e}")


def register_today():
    """Регистрация обработчиков для бота. Упражнения на бицепс"""
    router.callback_query.register(get_today_data_handler)  # Перечень упражнений на бицепс
