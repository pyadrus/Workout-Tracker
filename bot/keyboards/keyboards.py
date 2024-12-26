from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
)
from bot.data.config import BASE_SITE_URL


def generate_user_options_keyboard() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру с кнопками для взаимодействия пользователя с ботом.

    :return: Объект InlineKeyboardMarkup с кнопками для выбора.
    """
    kb = [
        [
            InlineKeyboardButton(text="📝 Регистрация", callback_data="registration"),
            InlineKeyboardButton(text="ℹ️ Описание", callback_data="description"),
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def generate_authorized_user_options_keyboard() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру с кнопками для взаимодействия пользователя с ботом.

    :return: Объект InlineKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            InlineKeyboardButton(text="⚙️ Личный кабинет", callback_data="personal_account"),
            # Кнопка для начала процесса регистрации.
            InlineKeyboardButton(text="ℹ️ Описание", callback_data="description"),
            # Кнопка для отображения описания проекта.
        ],
        [
            InlineKeyboardButton(text="🗣️ Обратная связь", callback_data="feedback"),
            InlineKeyboardButton(text="🤖 В бота", web_app=WebAppInfo(url=BASE_SITE_URL)),
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def generate_admin_button() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру с кнопками для взаимодействия пользователя с ботом.

    :return: Объект InlineKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            InlineKeyboardButton(text="⚙️ Личный кабинет", callback_data="personal_account", ),
            # Кнопка для входа в личный кабинет.
            InlineKeyboardButton(text="ℹ️ Описание", callback_data="description",
                                 ),  # Кнопка для отображения описания проекта.
        ],
        [
            InlineKeyboardButton(text="🗣️ Обратная связь", callback_data="feedback"),
            InlineKeyboardButton(text="🤖 В бота", web_app=WebAppInfo(url=BASE_SITE_URL)),
        ],
        [
            InlineKeyboardButton(text="🔧 Админ-панель", callback_data="admin_panel"),
            # Кнопка для входа в админское меню
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def generate_admin_panel_keyboard() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру с кнопками для ажминистратора.

    :return: Объект InlineKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            InlineKeyboardButton(text="Рассылка сообщений пользователям", callback_data="sending_messages"),
            # Кнопка для рассылки сообщений пользователям.
            InlineKeyboardButton(text="Статистика", callback_data="statistics"),  # Кнопка для отображения статистики.
        ],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def generate_authorized_user_discription() -> None:
    kb = [
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def generate_keyboard_personal_account() -> InlineKeyboardMarkup:
    """
    :return: Объект InlineKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            InlineKeyboardButton(text="📋 Просмотр данных", callback_data="view_data"),
            # Кнопка для начала процесса регистрации.
            InlineKeyboardButton(text="🔙 Назад", callback_data="back"),
        ],  # Кнопка для просмотра личного кабинета
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def create_data_change_buttons() -> InlineKeyboardMarkup:
    """
    :return: Объект InlineKeyboardMarkup с кнопками для выбора.
    """

    kb = [
        [
            InlineKeyboardButton(text="✍️ Изменить имя", callback_data="update_name"),
            InlineKeyboardButton(text="📏 Изменить рост", callback_data="update_height"),
        ],
        [
            InlineKeyboardButton(text="⚖️ Изменить вес", callback_data="update_weight"),
            InlineKeyboardButton(text="🏋️ Изменить опыт тренировок", callback_data="update_training_experience"),
        ],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_personal_account")],
        [InlineKeyboardButton(text="🔙 В главное меню", callback_data="back", )],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


if __name__ == "__main__":
    generate_user_options_keyboard()
    generate_authorized_user_options_keyboard()
    generate_keyboard_personal_account()
    create_data_change_buttons()
