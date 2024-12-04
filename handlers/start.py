# Основной файл Telegram-бота, использующего aiogram для взаимодействия с пользователями.
# В этом файле создается логика обработки сообщений и FSM (Finite State Machine) для регистрации пользователей.

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from data.text import (  # Импорты текстов приветствия и описания.
    text_authorized_user_greeting,
    text_description,
    text_hello_welcome,
)
from database.database import (
    get_user_data,  # Импорт функции получения пользователя из базы
)
from keyboards.keyboards import (
    generate_authorized_user_options_keyboard,
    generate_user_options_keyboard,  # Импорт функции для создания клавиатуры.
)

router = Router()  # Создание маршрутизатора для обработки команд и сообщений.


# Обработчик команды /start, отправляющий приветственное сообщение и клавиатуру с вариантами.
@router.message(CommandStart())
async def start_bot(message: Message) -> None:
    """
    Отправляет приветственное сообщение пользователю при старте бота.

    Аргументы:
    :param message: Сообщение пользователя с командой /start.
    """
    username = message.from_user.username
    data_user = get_user_data(username)
    if not data_user:
        await message.answer(
            f"👋 Приветствую тебя, @{username}{text_hello_welcome()}",
            reply_markup=generate_user_options_keyboard(),
        )
    else:
        await message.answer(
            f"👋 Приветствую тебя, @{username}{text_authorized_user_greeting()}",
            reply_markup=generate_authorized_user_options_keyboard(),
        )


@router.callback_query(F.data == "description")
async def description(callback_query: CallbackQuery) -> None:
    """
    Отправляет описание бота пользователю.

    Аргументы:
    :param message: Сообщение пользователя с текстом "описание".
    """
    await callback_query.message.answer(f"ℹ️ {text_description()}")
