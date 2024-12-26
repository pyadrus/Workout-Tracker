from aiogram import F
from aiogram import types
from loguru import logger
from datetime import datetime

from bot.data.config import router, bot
from bot.keyboards.keyboard_user.keyboard_help import keyboard_help


@router.callback_query(F.data == "training_program")
async def training_program(callback_query: types.CallbackQuery):
    """Программа тренировок"""
    try:
        user_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = (
            f"<b>🔥 Силовая и функциональная тренировка на сегодня ({user_date}) 🔥</b>\n\n"
            f"👋 Привет! Вот твой план на сегодня:\n\n"

            "<b>1. Поочередный подъем гантелей перед собой</b>\n"
            "- <b>Вес:</b> 10 кг\n"
            "- <b>Повторения:</b> 8\n"
            "- <b>Подходы:</b> 4\n\n"

            "<b>2. Трицепс с гантелью</b>\n"
            "- <b>Вес:</b> 7,5 кг\n"
            "- <b>Повторения:</b> 8\n"
            "- <b>Подходы:</b> 4\n\n"

            "<b>3. Трицепс на блоке (канат)</b>\n"
            "- <b>Вес:</b> 36 кг\n"
            "- <b>Повторения:</b> 8\n"
            "- <b>Подходы:</b> 4\n\n"

            "<b>4. Подъем ног</b>\n"
            "- <b>Повторения:</b> 8\n"
            "- <b>Подходы:</b> 5\n\n"

            "<b>5. Ноги на тренажёре</b>\n"
            "- <b>Вес:</b> 34 кг\n"
            "- <b>Повторения:</b> 8\n"
            "- <b>Подходы:</b> 4\n\n"

            "<b>6. Опускание блока на тренажёре</b>\n"
            "- <b>Вес:</b> 36 кг\n"
            "- <b>Повторения:</b> 8\n"
            "- <b>Подходы:</b> 4\n\n"

            "<b>7. Гиперэкстензия</b>\n"
            "- <b>Повторения:</b> 8\n"
            "- <b>Подходы:</b> 4"
        )

        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text=result,
            reply_markup=keyboard_help(),  # Убедитесь, что функция keyboard_menu() возвращает правильную клавиатуру
            parse_mode="HTML"
        )


    except Exception as e:

        logger.error(f"Ошибка: {e}")


def register_training():
    """Регистрация обработчиков для бота"""
    router.callback_query.register(training_program)  # Программа тренировок
