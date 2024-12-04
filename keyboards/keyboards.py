from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.types.web_app_info import WebAppInfo


def generate_user_options_keyboard() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру с кнопками для взаимодействия пользователя с ботом.

    :return: Объект ReplyKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            InlineKeyboardButton(
                text="📝 Регистрация",
                callback_data="registration",
            ),  # Кнопка для начала процесса регистрации.
            InlineKeyboardButton(
                text="ℹ️ Описание",
                callback_data="description",
            ),  # Кнопка для отображения описания проекта.
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def generate_authorized_user_options_keyboard() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру с кнопками для взаимодействия пользователя с ботом.

    :return: Объект ReplyKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            InlineKeyboardButton(
                text="⚙️ Личный кабинет",
                callback_data="personal_account",
            ),  # Кнопка для начала процесса регистрации.
            InlineKeyboardButton(
                text="ℹ️ Описание",
                callback_data="description",
            ),  # Кнопка для отображения описания проекта.
        ],
        [
            InlineKeyboardButton(
                text="📞 Обратная связь",
                callback_data="feedback",
            ),  # Кнопка для начала процесса регистрации.
            InlineKeyboardButton(
                text="🏠 В бота",
                web_app=WebAppInfo(url="https://c667-109-254-149-114.ngrok-free.app/"),
            ),  # Кнопка для отображения описания проекта.
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def generate_keyboard_personal_account() -> InlineKeyboardMarkup:
    """
    :return: Объект ReplyKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            InlineKeyboardButton(
                text="📋 Просмотр данных",
                callback_data="view_data",
            ),  # Кнопка для начала процесса регистрации.
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data="back",
            ),
        ],  # Кнопка для просмотра личного кабинета
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def create_data_change_buttons() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру с инлайн кнопками для взаимодействия пользователя с ботом.

    :return: Объект InlineKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            InlineKeyboardButton(text="👤 Изменить имя", callback_data="update_name"),
            InlineKeyboardButton(
                text="📏 Изменить рост", callback_data="update_height"
            ),
        ],
        [
            InlineKeyboardButton(text="⚖️ Изменить вес", callback_data="update_weight"),
            InlineKeyboardButton(
                text="🏋️ Изменить опыт тренировок",
                callback_data="update_training_experience",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data="back_personal_account",
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
