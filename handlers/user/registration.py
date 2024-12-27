from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from data.config import router
from database.database import add_users  # Импорт функции добавления зарегистрированного пользователя в базу.
from keyboards.keyboard_user.keyboards import generate_main_menu_keyboard
from states.states import RegistrationStates
from utils.messages_loader import text_input_name, text_input_height, text_input_weight, text_input_height_error, \
    text_input_training_experience, text_input_weight_error, menu_text
from utils.validators import is_float, is_int


@router.callback_query(F.data == "registration")
async def user_registration_command(callback_query: CallbackQuery, state: FSMContext) -> None:
    """
    Начинает процесс регистрации пользователя. Обработчик сообщения с текстом "регистрация", начинающий процесс регистрации.

    Аргументы:
    :param callback_query: CallbackQuery: Сообщение пользователя с текстом "регистрация".
    :param state: Контекст состояния FSM.
    """
    await state.set_state(RegistrationStates.name)
    await callback_query.message.answer(text_input_name, parse_mode="HTML")


@router.message(RegistrationStates.name)
async def register_user_name(message: Message, state: FSMContext) -> None:
    """
    Запрашивает рост пользователя после ввода имени. Обработчик состояния ввода имени пользователя.

    Аргументы:
    :param message: Сообщение пользователя с именем.
    :param state: Контекст состояния FSM.
    """
    await state.update_data(name=message.text)
    await state.set_state(RegistrationStates.height)
    await message.answer(text_input_height, parse_mode="HTML")


@router.message(RegistrationStates.height)
async def register_user_height(message: Message, state: FSMContext) -> None:
    """
    Запрашивает вес пользователя после ввода роста. Обработчик состояния ввода роста пользователя.±

    Аргументы:
    :param message: Сообщение пользователя с ростом.
    :param state: Контекст состояния FSM.
    """
    input_heightttt = message.text
    if is_int(input_heightttt) or is_float(input_heightttt):
        await state.update_data(height=input_heightttt)
        await state.set_state(RegistrationStates.weight)
        await message.answer(text_input_weight, parse_mode="HTML")
    else:
        await message.answer(text_input_height_error, parse_mode="HTML")


@router.message(RegistrationStates.weight)
async def register_user_training_experience(message: Message, state: FSMContext) -> None:
    """
    Запрашивает опыт тренировок пользователя после ввода веса. Обработчик состояния ввода веса пользователя.

    Аргументы:
    :param message: Сообщение пользователя с весом.
    :param state: Контекст состояния FSM.
    """
    input_weight = message.text
    if is_int(input_weight) or is_float(input_weight):
        await state.update_data(weight=input_weight)
        await state.set_state(RegistrationStates.training_experience)
        await message.answer(text_input_training_experience, parse_mode="HTML")
    else:
        await message.answer(text_input_weight_error, parse_mode="HTML")


@router.message(RegistrationStates.training_experience)
async def registration_user_info(message: Message, state: FSMContext) -> None:
    """
    Завершает процесс регистрации и отображает введенные пользователем данные.
    Добавляет пользователя в базу данных. Обработчик состояния ввода опыта тренировок, завершающий процесс регистрации.

    Аргументы:
    :param message: Сообщение пользователя с опытом тренировок.
    :param state: Контекст состояния FSM.
    """
    await state.update_data(training_experience=message.text)
    user_data = await state.get_data()
    user_id_telegram = message.from_user.id
    await message.answer(menu_text, reply_markup=generate_main_menu_keyboard(), parse_mode="HTML")
    add_users(user_id_telegram, user_data["name"], user_data["height"], user_data["weight"],
              user_data["training_experience"])

    await state.clear()  # Сброс состояния после завершения регистрации.


def register_registration_user():
    """Регистрация обработчиков для бота"""
    router.callback_query.register(user_registration_command)  # Регистрация пользователя
