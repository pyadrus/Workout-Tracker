from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from data.config import BASE_SITE_URL


def generate_main_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Создает компактную клавиатуру с кнопками для взаимодействия пользователя с ботом.

    :return: Объект InlineKeyboardMarkup с кнопками для выбора.
    """
    kb = [
        [
            InlineKeyboardButton(text="📝 Регистрация", callback_data="registration"),
            InlineKeyboardButton(text="ℹ️ Описание", callback_data="description"),
        ],
        [
            InlineKeyboardButton(text="💪 Упражнения", callback_data="types_of_exercises_for_muscle_groups"),
            InlineKeyboardButton(text="🆘 Помощь", callback_data="help_with_work"),
        ],
        [
            InlineKeyboardButton(text="🗂️ Тренировки", callback_data="training_program"),
            InlineKeyboardButton(text="🏋️ Запись", callback_data="CommandStart"),
        ],
        [
            InlineKeyboardButton(text="📊 Результат", callback_data="get_today"),
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


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

    return InlineKeyboardMarkup(inline_keyboard=kb)


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

    return InlineKeyboardMarkup(inline_keyboard=kb)


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

    return InlineKeyboardMarkup(inline_keyboard=kb)


def generate_authorized_user_discription() -> InlineKeyboardMarkup:
    kb = [[InlineKeyboardButton(text="🔙 Назад", callback_data="back")]]
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
    return InlineKeyboardMarkup(inline_keyboard=kb)


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
    return InlineKeyboardMarkup(inline_keyboard=kb)


if __name__ == "__main__":
    generate_main_menu_keyboard()
    generate_authorized_user_options_keyboard()
    generate_keyboard_personal_account()
    create_data_change_buttons()
    generate_authorized_user_discription()
    generate_admin_button()
    generate_admin_panel_keyboard()
