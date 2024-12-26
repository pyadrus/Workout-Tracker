from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Словарь упражнений на трицепс: ключ (key) - callback_data, значение (value) - текст кнопки
help_dict = {
    "start_handler": "В начальное меню"
}


def keyboard_help():
    """Клавиатура помощь"""
    triceps_exercises = [
        [InlineKeyboardButton(text=value, callback_data=key)]
        for key, value in help_dict.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=triceps_exercises)


if __name__ == '__main__':
    keyboard_help()
