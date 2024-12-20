import json

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from handlers.start import load_text_form_file
from database.database import (
    add_users,  # Импорт функции добавления пользователя в базу
)
from keyboards.keyboards import (
    generate_authorized_user_options_keyboard,
)

routerrrr = Router()  # Создание маршрутизатора для обработки команд и сообщений.

# Чтение файла json для выборки текстов
# with open("data/text.json", "r", encoding="utf-8") as file:
#     texts = json.load(file)


class Registration(StatesGroup):
    name = State()  # Состояние изменения имени.
    height = State()  # Состояние изменения роста.
    weight = State()  # Состояние изменения веса.
    training_experience = State()  # Состояние изменения опыта тренировок.


# Обработчик сообщения с текстом "регистрация", начинающий процесс регистрации.
@routerrrr.callback_query(F.data == "registration")
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


# Обработчик состояния ввода роста пользователя.±
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


# Проверка веса на float
def is_float(value: str) -> bool:
    try:
        _ = float(value)
        return True
    except ValueError:
        return False


# Проверка веса на int
def is_int(value: str) -> bool:
    try:
        _ = int(value)
        return True
    except ValueError:
        return False


# Обработчик состояния ввода веса пользователя.
@routerrrr.message(Registration.weight)
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
    username = message.from_user.username
    user_id = message.from_user.id
    await message.answer(
        f"👋 Приветствую тебя, @{username}{load_text_form_file('text_authorized_user_greeting.json')}",
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
