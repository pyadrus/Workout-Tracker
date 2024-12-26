from aiogram import types, F
from loguru import logger

from bot.data.config import router, bot
from bot.keyboards.exercises.exercise_keyboard import exercise_keyboard


@router.callback_query(F.data == "types_of_exercises_for_muscle_groups")
async def types_of_exercises_for_muscle_groups_handlers(callback_query: types.CallbackQuery):
    """Перечень групп мышц"""
    try:
        types_of_exercises_for_muscle_groups_text = (
            "💪 Выбирай и тренируйся!\n\n"

            "Добро пожаловать в меню упражнений! 👇 Нажимай на кнопку с интересующей тебя группой мышц, и я покажу "
            "лучшие упражнения для:\n\n"

            "1️⃣ Бицепсов – накачай сильные руки 💪\n"
            "2️⃣ Трицепсов – добавь мощь задней части рук 🏋️‍♂️\n"
            "3️⃣ Груди – прокачай объем и силу 🔥\n"
            "4️⃣ Спины – создай V-образную форму 🦅\n"
            "5️⃣ Плеч – добавь ширину и рельеф 🎯\n"
            "6️⃣ Ног – укрепи нижнюю часть тела 🦵\n"
            "7️⃣ Пресса – сделай кубики реальностью 🏖\n"
            "8️⃣ Ягодиц – придай им упругость и форму 🍑\n\n"

            "Просто нажми на нужную группу мышц, и начнем! 🚀"
        )

        # Если нужно отправить новое сообщение:
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text=types_of_exercises_for_muscle_groups_text,
            reply_markup=exercise_keyboard(), parse_mode="Markdown",
        )

    except Exception as e:
        logger.error(f"Ошибка: {e}")


def register_exercises():
    """Регистрация обработчиков для бота"""
    router.callback_query.register(types_of_exercises_for_muscle_groups_handlers)  # Перечень групп мышц
