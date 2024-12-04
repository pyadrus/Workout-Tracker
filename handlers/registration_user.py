from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from data.text import (  # Импорты текстов приветствия и описания.
    text_description,
    text_hello_welcome,
    text_authorized_user_greeting,
)
from database.database import (
    add_users,  # Импорт функции добавления пользователя в базу
    get_user_data,  # Импорт функции получения пользователя из базы
    update_user_data,  # Импорт функции изменения данных пользователя в базе
)
from keyboards.keyboards import (
    generate_user_options_keyboard,  # Импорт функции для создания клавиатуры.
    generate_keyboard_personal_account,
    generate_authorized_user_options_keyboard,
    create_data_change_buttons,
)

routerrrr = Router()  # Создание маршрутизатора для обработки команд и сообщений.


class Registration(StatesGroup):
    name = State()  # Состояние ввода имени.
    height = State()  # Состояние ввода роста.
    weight = State()  # Состояние ввода веса.
    training_experience = State()  # Состояние ввода опыта тренировок.


class ChangeData(StatesGroup):
    name = State()  # Состояние ввода имени.
    height = State()  # Состояние ввода роста.
    weight = State()  # Состояние ввода веса.
    training_experience = State()  # Состояние ввода опыта тренировок.


# Обработчик сообщения с текстом "регистрация", начинающий процесс регистрации.
@routerrrr.message(F.text.lower() == "📝 регистрация")
async def registration(message: Message, state: FSMContext) -> None:
    """
    Начинает процесс регистрации пользователя.

    Аргументы:
    :param message: Сообщение пользователя с текстом "регистрация".
    :param state: Контекст состояния FSM.
    """
    await state.set_state(Registration.name)
    await message.answer("✍️ Для регистрации введите своё имя")


# Обработчик состояния ввода имени пользователя.
@routerrrr.message(Registration.name)
async def get_name(message: Message, state: FSMContext) -> None:
    """
    Запрашивает рост пользователя после ввода имени.

    Аргументы:
    :param message: Сообщение пользователя с именем.
    :param state: Контекст состояния FSM.
    """
    await state.update_data(name=message.text)
    await state.set_state(Registration.height)
    await message.answer("📏 Введите свой рост в сантиметрах")


# Обработчик состояния ввода роста пользователя.
@routerrrr.message(Registration.height)
async def get_height(message: Message, state: FSMContext) -> None:
    """
    Запрашивает вес пользователя после ввода роста.

    Аргументы:
    :param message: Сообщение пользователя с ростом.
    :param state: Контекст состояния FSM.
    """
    await state.update_data(height=message.text)
    await state.set_state(Registration.weight)
    await message.answer("⚖️ Введите свой вес в килограммах")


# Обработчик состояния ввода веса пользователя.
@routerrrr.message(Registration.weight)
async def get_training_experience(message: Message, state: FSMContext) -> None:
    """
    Запрашивает опыт тренировок пользователя после ввода веса.

    Аргументы:
    :param message: Сообщение пользователя с весом.
    :param state: Контекст состояния FSM.
    """
    await state.update_data(weight=message.text)
    await state.set_state(Registration.training_experience)
    await message.answer("🏋️ Введите свой опыт в тренировках")


# Обработчик состояния ввода опыта тренировок, завершающий процесс регистрации.
@routerrrr.message(Registration.training_experience)
async def registration_info(message: Message, state: FSMContext) -> None:
    """
    Завершает процесс регистрации и отображает введенные пользователем данные.
    Добавляет пользователя в базу данных

    Аргументы:
    :param message: Сообщение пользователя с опытом тренировок.
    :param state: Контекст состояния FSM.
    """
    await state.update_data(training_experience=message.text)
    user_data = await state.get_data()
    await message.answer(
        f"Вы успешно зарегистрировались!\n\n"
        f"✅ Данные регистрации:\n"
        f"👤 Имя - {user_data['name']}\n"
        f"📏 Рост - {user_data['height']} см\n"
        f"⚖️ Вес - {user_data['weight']} кг\n"
        f"🏋️ Опыт тренировок - {user_data['training_experience']}",
        reply_markup=generate_authorized_user_options_keyboard(),
    )
    username = message.from_user.username
    add_users(
        username,
        user_data["name"],
        user_data["height"],
        user_data["weight"],
        user_data["training_experience"],
    )

    await state.clear()  # Сброс состояния после завершения регистрации.
