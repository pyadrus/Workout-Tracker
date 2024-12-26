from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from bot.utils.read_text import load_text_form_file
from bot.database.database import (
    add_users,  # Импорт функции добавления зарегистрированного пользователя в базу.
)
from bot.keyboards.keyboards import (
    generate_authorized_user_options_keyboard,
)
from bot.utils.validators import (
    is_float,  # Имфорт функции валидации вещественных чисел.
    is_int,  # Имфорт функций валидации целых чисел.
)

router_registration_user = (
    Router()
)  # Создание маршрутизатора для обработки команд и сообщений.


class RegistrationStates(StatesGroup):
    name = State()  # Состояние ввода имени.
    height = State()  # Состояние ввода роста.
    weight = State()  # Состояние ввода веса.
    training_experience = State()  # Состояние ввода опыта тренировок.


# Обработчик сообщения с текстом "регистрация", начинающий процесс регистрации.
@router_registration_user.callback_query(F.data == "registration")
async def user_registration_command(callback_query: CallbackQuery, state: FSMContext) -> None:
    """
    Начинает процесс регистрации пользователя.

    Аргументы:
    :param message: Сообщение пользователя с текстом "регистрация".
    :param state: Контекст состояния FSM.
    """
    await state.set_state(RegistrationStates.name)
    await callback_query.message.answer(
        f"{load_text_form_file('text_input_name.json')}"
    )


# Обработчик состояния ввода имени пользователя.
@router_registration_user.message(RegistrationStates.name)
async def register_user_name(message: Message, state: FSMContext) -> None:
    """
    Запрашивает рост пользователя после ввода имени.

    Аргументы:
    :param message: Сообщение пользователя с именем.
    :param state: Контекст состояния FSM.
    """
    await state.update_data(name=message.text)
    await state.set_state(RegistrationStates.height)
    await message.answer(f"{load_text_form_file('text_input_height.json')}")


# Обработчик состояния ввода роста пользователя.±
@router_registration_user.message(RegistrationStates.height)
async def register_user_height(message: Message, state: FSMContext) -> None:
    """
    Запрашивает вес пользователя после ввода роста.

    Аргументы:
    :param message: Сообщение пользователя с ростом.
    :param state: Контекст состояния FSM.
    """
    input_heightttt = message.text
    if is_int(input_heightttt) or is_float(input_heightttt):
        await state.update_data(height=input_heightttt)
        await state.set_state(RegistrationStates.weight)
        await message.answer(f"{load_text_form_file('text_input_weight.json')}")
    else:
        await message.answer(f"{load_text_form_file('text_input_height_error.json')}")


# Обработчик состояния ввода веса пользователя.
@router_registration_user.message(RegistrationStates.weight)
async def register_user_training_experience(
        message: Message, state: FSMContext
) -> None:
    """
    Запрашивает опыт тренировок пользователя после ввода веса.

    Аргументы:
    :param message: Сообщение пользователя с весом.
    :param state: Контекст состояния FSM.
    """
    input_weight = message.text
    if is_int(input_weight) or is_float(input_weight):
        await state.update_data(weight=input_weight)
        await state.set_state(RegistrationStates.training_experience)
        await message.answer(
            f"{load_text_form_file('text_input_training_experience.json')}"
        )
    else:
        await message.answer(f"{load_text_form_file('text_input_weight_error.json')}")


# Обработчик состояния ввода опыта тренировок, завершающий процесс регистрации.
@router_registration_user.message(RegistrationStates.training_experience)
async def registration_user_info(message: Message, state: FSMContext) -> None:
    """
    Завершает процесс регистрации и отображает введенные пользователем данные.
    Добавляет пользователя в базу данных

    Аргументы:
    :param message: Сообщение пользователя с опытом тренировок.
    :param state: Контекст состояния FSM.
    """
    await state.update_data(training_experience=message.text)
    user_data = await state.get_data()
    user_id_telegram = message.from_user.id
    await message.answer(
        f"{load_text_form_file('text_authorized_user_greeting.json')}",
        reply_markup=generate_authorized_user_options_keyboard(),
    )
    add_users(
        user_id_telegram,
        user_data["name"],
        user_data["height"],
        user_data["weight"],
        user_data["training_experience"],
    )

    await state.clear()  # Сброс состояния после завершения регистрации.
