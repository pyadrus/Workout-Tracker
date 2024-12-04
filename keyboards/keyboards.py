from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


def generate_user_options_keyboard():
    """
    Создает клавиатуру с кнопками для взаимодействия пользователя с ботом.

    :return: Объект ReplyKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            KeyboardButton(
                text="📝 Регистрация"
            ),  # Кнопка для начала процесса регистрации.
            KeyboardButton(
                text="ℹ️ Описание"
            ),  # Кнопка для отображения описания проекта.
        ]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,  # Уменьшает размер кнопок для удобства.
        input_field_placeholder="👇 Выберите один из вариантов",  # Подсказка в поле ввода.
    )
    return keyboard


def generate_authorized_user_options_keyboard():
    """
    Создает клавиатуру с кнопками для взаимодействия пользователя с ботом.

    :return: Объект ReplyKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            KeyboardButton(
                text="⚙️ Личный кабинет"
            ),  # Кнопка для начала процесса регистрации.
            KeyboardButton(
                text="ℹ️ Описание"
            ),  # Кнопка для отображения описания проекта.
        ]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,  # Уменьшает размер кнопок для удобства.
        input_field_placeholder="👇 Выберите один из вариантов",  # Подсказка в поле ввода.
    )
    return keyboard


def generate_keyboard_personal_account():
    """
    :return: Объект ReplyKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            KeyboardButton(
                text="📋 Просмотр данных"
            ),  # Кнопка для начала процесса регистрации.
            KeyboardButton(text="🔙 Назад"),
        ],  # Кнопка для просмотра личного кабинета
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,  # Уменьшает размер кнопок для удобства.
        input_field_placeholder="👇 Выберите один из вариантов",  # Подсказка в поле ввода.
    )
    return keyboard


def create_data_change_buttons() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру с инлайн кнопками для взаимодействия пользователя с ботом.

    :return: Объект InlineKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            InlineKeyboardButton(text="👤 Изменить имя", callback_data="update_name"),
            InlineKeyboardButton(text="📏 Изменить рост", callback_data="height"),
        ],
        [
            InlineKeyboardButton(text="⚖️ Изменить вес", callback_data="weight"),
            InlineKeyboardButton(
                text="🏋️ Изменить опыт тренировок", callback_data="training_experience"
            ),
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


if __name__ == "__main__":
    generate_user_options_keyboard()
    generate_authorized_user_options_keyboard()
    generate_keyboard_personal_account()
    create_data_change_buttons()
