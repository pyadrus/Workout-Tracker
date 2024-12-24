from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from handlers.launch_bot import load_text_form_file
from database.database import (
    add_users,  # Импорт функции добавления зарегистрированного пользователя в базу.
)
from keyboards.keyboards import (
    generate_authorized_user_options_keyboard,
)
from utils.validators import is_float, is_int

registration_user_router = (
    Router()
)  # Создание маршрутизатора для обработки команд и сообщений.


class Registration(StatesGroup):
    name = State()  # Состояние изменения имени.
    height = State()  # Состояние изменения роста.
    weight = State()  # Состояние изменения веса.
    training_experience = State()  # Состояние изменения опыта тренировок.


# Обработчик сообщения с текстом "регистрация", начинающий процесс регистрации.
@registration_user_router.callback_query(F.data == "registration")
async def registration(callback_query: CallbackQuery, state: FSMContext) -> None:
    """
    Начинает процесс регистрации пользователя.

    Аргументы:
    :param message: Сообщение пользователя с текстом "регистрация".
    :param state: Контекст состояния FSM.
    """
    await state.set_state(Registration.name)
    await callback_query.message.answer("✍️ Для регистрации введите своё имя")


# Обработчик состояния ввода имени пользователя.
@registration_user_router.message(Registration.name)
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


# Обработчик состояния ввода роста пользователя.±
@registration_user_router.message(Registration.height)
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
@registration_user_router.message(Registration.weight)
async def get_training_experience(message: Message, state: FSMContext) -> None:
    """
    Запрашивает опыт тренировок пользователя после ввода веса.

    Аргументы:
    :param message: Сообщение пользователя с весом.
    :param state: Контекст состояния FSM.
    """
    input_weight = message.text
    if is_int(input_weight) or is_float(input_weight):
        await state.update_data(weight=input_weight)
        await state.set_state(Registration.training_experience)
        await message.answer("🏋️ Введите свой опыт в тренировках")
    else:
        await message.answer("🏋️ Вес должен содержать только числа")
        return


# Обработчик состояния ввода опыта тренировок, завершающий процесс регистрации.
@registration_user_router.message(Registration.training_experience)
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
    user_id = message.from_user.id
    await message.answer(
        f"{load_text_form_file('text_authorized_user_greeting.json')}",
        reply_markup=generate_authorized_user_options_keyboard(),
    )
    add_users(
        user_id,
        user_data["name"],
        user_data["height"],
        user_data["weight"],
        user_data["training_experience"],
    )

    await state.clear()  # Сброс состояния после завершения регистрации.
