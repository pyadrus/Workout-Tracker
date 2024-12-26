from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loguru import logger


def exercise_keyboard():
    """Клавиатура упражнений на различные группы мышц, с распределением на 2 колонки и кнопкой в центре."""
    try:

        rows = [
            [InlineKeyboardButton(text='Трицепс', callback_data='triceps'),  # TODO готово
             InlineKeyboardButton(text='Бицепс', callback_data='biceps'), ],  # TODO готово

            [InlineKeyboardButton(text='Грудные мышцы', callback_data='pectoral'),  # TODO в разработке
             InlineKeyboardButton(text='Спина', callback_data='back_exercises')],

            [InlineKeyboardButton(text='Плечи', callback_data='shoulder_exercises'),
             InlineKeyboardButton(text='Ноги', callback_data='leg_exercises')],

            [InlineKeyboardButton(text='Пресс', callback_data='ab_exercises'),
             InlineKeyboardButton(text='Ягодичные мышцы', callback_data='exercises_for_the_gluteal_muscles')],

            [InlineKeyboardButton(text='В начальное меню', callback_data='start_handler')],
        ]

        return InlineKeyboardMarkup(inline_keyboard=rows)
    except Exception as e:
        logger.error(f"Ошибка: {e}")


if __name__ == '__main__':
    exercise_keyboard()  # Клавиатура с распределением на 2 колонки
