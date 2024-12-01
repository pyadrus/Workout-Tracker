from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def generate_user_options_keyboard():
    """
    Создает клавиатуру с кнопками для взаимодействия пользователя с ботом.

    :return: Объект ReplyKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            KeyboardButton(text="📝 Регистрация"),  # Кнопка для начала процесса регистрации.
            KeyboardButton(text="ℹ️ Описание"),  # Кнопка для отображения описания проекта.
        ]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,  # Уменьшает размер кнопок для удобства.
        input_field_placeholder="👇 Выберите один из вариантов",  # Подсказка в поле ввода.
    )
    return keyboard


if __name__ == '__main__':
    generate_user_options_keyboard()
