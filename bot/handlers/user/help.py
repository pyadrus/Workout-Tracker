from aiogram import types, F
from loguru import logger

from bot.data.config import router, bot
from bot.keyboards.keyboard_user.keyboard_help import keyboard_help


@router.callback_query(F.data == "help_with_work")
async def help_command(callback_query: types.CallbackQuery):
    try:
        help_text = (
            "🤖 Добро пожаловать в Бот-Тренер! Вот что я умею:\n\n"
            "🏋️‍♂️ **Планирование тренировок**\n"
            "Создавайте свои программы тренировок и следите за прогрессом.\n\n"
            "📊 **Анализ результатов**\n"
            "Показываю результаты ваших тренировок за текущий день.\n\n"
            "💪 **Подбор упражнений**\n"
            "Вывод списка упражнений для различных групп мышц с подробным описанием.\n\n"
            "🎯 **Советы и помощь**\n"
            "Помогаю составить эффективный план для достижения ваших целей.\n\n"
            "🌟 Используйте кнопки ниже, чтобы узнать больше о возможностях или начать прямо сейчас!"
        )
        # Если нужно отправить новое сообщение:
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text=help_text,
            reply_markup=keyboard_help(), parse_mode="Markdown",
        )

    except Exception as e:
        logger.error(f"Ошибка: {e}")


def register_help():
    """Регистрация обработчиков для бота"""
    router.callback_query.register(help_command)  # Помощь
