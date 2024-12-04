from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    WebAppInfo,
)


def generate_user_options_keyboard() -> InlineKeyboardMarkup:
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
            InlineKeyboardButton(
                text="В бота",
                web_app=WebAppInfo(url="https://c667-109-254-149-114.ngrok-free.app/"),
            )
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
            InlineKeyboardButton(
                text="⚙️ Личный кабинет",
                callback_data="personal_account",
            ),  # Кнопка для начала процесса регистрации.
            InlineKeyboardButton(
                text="ℹ️ Описание",
                callback_data="description",
            ),  # Кнопка для отображения описания проекта.
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def generate_keyboard_personal_account() -> ReplyKeyboardMarkup:
    """
    :return: Объект ReplyKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            KeyboardButton(text="📋 Просмотр данных"),  # Кнопка для начала процесса регистрации.
            KeyboardButton(text="✏️ Изменение данных"),  # Кнопка для отображения описания проекта.
        ],
        [KeyboardButton(text="🔙 Назад")],  # Кнопка для просмотра личного кабинета
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,  # Уменьшает размер кнопок для удобства.
        input_field_placeholder="👇 Выберите один из вариантов",  # Подсказка в поле ввода.
    )
    return keyboard


def generate_inline_keyboard_update_data() -> InlineKeyboardMarkup:
    """
    :return: Объект ReplyKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [InlineKeyboardButton(text="Мой хабр", url="https://habr.com/ru/users/yakvenalex/")],
        [InlineKeyboardButton(text="Мой Telegram", url="tg://resolve?domain=yakvenalexx")],
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
