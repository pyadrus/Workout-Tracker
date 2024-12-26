from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from loguru import logger

from bot.keyboards.keyboard_user.keyboard_menu import keyboard_menu
from system.dispatcher import bot
from system.dispatcher import router


# Обработчик команды /start
@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    try:

        user_id = message.from_user.id
        user_name = message.from_user.username or ""
        user_first_name = message.from_user.first_name or ""
        user_last_name = message.from_user.last_name or ""
        user_date = message.date.strftime("%Y-%m-%d %H:%M:%S")

        logger.info(f"User Info: {user_id}, {user_name}, {user_first_name}, {user_last_name}, {user_date}")

        menu_text = ("Привет! 💪 Я — твой персональный тренер в мире спорта! 🚀\n\n"

                     "Готов помочь тебе достичь новых высот и максимально эффективно тренироваться.\n\n"

                     "Неважно, хочешь ли ты увеличить силу, улучшить выносливость или просто поддерживать форму — я "
                     "здесь, чтобы помочь! Начнём тренировку? 😎")

        await message.answer(menu_text, reply_markup=keyboard_menu())
    except Exception as e:
        logger.error(f"Ошибка в обработчике /start: {e}")


@router.callback_query(F.data == "start_handler")
async def start_handler_callback(callback_query: types.CallbackQuery) -> None:
    """Главное меню."""
    try:
        user_id = callback_query.from_user.id
        user_name = callback_query.from_user.username or ""
        user_first_name = callback_query.from_user.first_name or ""
        user_last_name = callback_query.from_user.last_name or ""
        # Исправление: используем дату из сообщения
        user_date = callback_query.message.date.strftime("%Y-%m-%d %H:%M:%S")

        logger.info(f"User Info: {user_id}, {user_name}, {user_first_name}, {user_last_name}, {user_date}")

        menu_text = ("Привет! 💪 Я — твой персональный тренер в мире спорта! 🚀\n\n"

                     "Готов помочь тебе достичь новых высот и максимально эффективно тренироваться.\n\n"

                     "Неважно, хочешь ли ты увеличить силу, улучшить выносливость или просто поддерживать форму — я "
                     "здесь, чтобы помочь! Начнём тренировку? 😎")

        # Если нужно отправить новое сообщение:
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text=menu_text,
            reply_markup=keyboard_menu()  # Убедитесь, что функция keyboard_menu() возвращает правильную клавиатуру
        )

    except Exception as e:
        logger.error(f"Ошибка: {e}")


def register_start_handler_handlers():
    """Регистрация обработчиков для бота"""
    router.message.register(start_handler)  # Главное меню бота
    router.callback_query.register(start_handler_callback)  # Главное меню бота
