from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def keyboard_start_handler() -> InlineKeyboardMarkup:
    """Назад в Начальное меню"""
    kb = [
        [
            InlineKeyboardButton(text="В начальное меню", callback_data="start_handler"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


if __name__ == '__main__':
    keyboard_start_handler()
