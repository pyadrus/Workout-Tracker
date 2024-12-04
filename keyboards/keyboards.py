from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from aiogram.types import WebAppInfo


def generate_user_options_keyboard():
    """
    Создает клавиатуру с кнопками для взаимодействия пользователя с ботом.

    :return: Объект InlineKeyboardMarkup с кнопками для выбора.
    """
    kb = [
        [
            InlineKeyboardButton(text="📝 Регистрация", callback_data="register"),
            InlineKeyboardButton(text="ℹ️ Описание", callback_data="description"),
        ],
        [
            InlineKeyboardButton(text="В бота", web_app=WebAppInfo(url="https://c667-109-254-149-114.ngrok-free.app/"))
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


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
            KeyboardButton(
                text="✏️ Изменение данных"
            ),  # Кнопка для отображения описания проекта.
        ],
        [KeyboardButton(text="🔙 Назад")],  # Кнопка для просмотра личного кабинета
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,  # Уменьшает размер кнопок для удобства.
        input_field_placeholder="👇 Выберите один из вариантов",  # Подсказка в поле ввода.
    )
    return keyboard


def generate_inline_keyboard_update_data():
    """
    :return: Объект ReplyKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            InlineKeyboardButton(
                text="Мой хабр", url="https://habr.com/ru/users/yakvenalex/"
            )
        ],
        [
            InlineKeyboardButton(
                text="Мой Telegram", url="tg://resolve?domain=yakvenalexx"
            )
        ],
    ]
    # keyboard = ReplyKeyboardMarkup(
    #     keyboard=kb,
    #     resize_keyboard=True,  # Уменьшает размер кнопок для удобства.
    #     input_field_placeholder="👇 Выберите один из вариантов",  # Подсказка в поле ввода.
    # )
    return InlineKeyboardMarkup(inline_keyboard=kb)


if __name__ == "__main__":
    generate_user_options_keyboard()
    generate_authorized_user_options_keyboard()
    generate_keyboard_personal_account()
    generate_inline_keyboard_update_data()
