from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from database.database import (
    get_user_data,  # Импорт функции получения пользователя из базы
    update_user_data,  # Импорт функции изменения данных пользователя в базе
)
from keyboards.keyboards import (
    generate_keyboard_personal_account,
    generate_authorized_user_options_keyboard,
    create_data_change_buttons,
)

routerr = Router()  # Создание маршрутизатора для обработки команд и сообщений.


class ChangeData(StatesGroup):
    name = State()  # Состояние ввода имени.
    height = State()  # Состояние ввода роста.
    weight = State()  # Состояние ввода веса.
    training_experience = State()  # Состояние ввода опыта тренировок.


# Обработчик состояния просмотра личного кабинета
@routerr.message(F.text.lower() == "⚙️ личный кабинет")
async def users_personal_account(message: Message) -> None:
    await message.answer(
        "Вы вошли в личный кабинет", reply_markup=generate_keyboard_personal_account()
    )


# Обработчик состояния просмотря личных данных при регистрации
@routerr.message(F.text.lower() == "📋 просмотр данных")
async def user_data(message: Message) -> None:
    username = message.from_user.username
    data_user = get_user_data(username)
    if data_user:
        _, name, height, weight, training_experience = data_user
        await message.answer(
            f"📋 Ваш профиль:\n"
            f"👤 Имя - {name}\n"
            f"📏 Рост - {height} см\n"
            f"⚖️ Вес - {weight} кг\n"
            f"🏋️ Опыт тренировок - {training_experience}",
            reply_markup=create_data_change_buttons(),
        )


# Обработчик состояния изменения имя профиля
@routerr.callback_query(F.data == "update_name")
async def update_user_data_name(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    username = callback_query.from_user.username
    data_user = get_user_data(username)
    if data_user:
        await state.set_state(ChangeData.name)
        await callback_query.message.answer("Введите имя на которое нужно изменить")


# Обработчик состояния изменения имя профиля. Продолжение update_user_data_name
@routerr.message(ChangeData.name)
async def update_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    state_user_data = await state.get_data()
    username = message.from_user.username
    changed_name = state_user_data["name"]
    update_user_data(username=username, name=changed_name)
    await message.answer("Вы изменили имя")
    await state.clear()


# Обработчик состояния изменения рост профиля
@routerr.callback_query(F.data == "update_height")
async def update_user_data_height(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    username = callback_query.from_user.username
    data_user = get_user_data(username)
    if data_user:
        await state.set_state(ChangeData.height)
        await callback_query.message.answer("Введите рост на которое нужно изменить")


# Обработчик состояния изменения имя профиля. Продолжение update_user_data_height
@routerr.message(ChangeData.height)
async def update_height(message: Message, state: FSMContext) -> None:
    await state.update_data(height=message.text)
    state_user_data = await state.get_data()
    username = message.from_user.username
    changed_height = state_user_data["height"]
    update_user_data(username=username, height=changed_height)
    await message.answer("Вы изменили рост")
    await state.clear()


# Обработчик состояния изменения вес профиля
@routerr.callback_query(F.data == "update_weight")
async def update_user_data_weight(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    username = callback_query.from_user.username
    data_user = get_user_data(username)
    if data_user:
        await state.set_state(ChangeData.weight)
        await callback_query.message.answer("Введите рост на которое нужно изменить")


# Обработчик состояния изменения вес профиля. Продолжение update_user_data_weight
@routerr.message(ChangeData.weight)
async def update_weight(message: Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    state_user_data = await state.get_data()
    username = message.from_user.username
    changed_weight = state_user_data["weight"]
    update_user_data(username=username, weight=changed_weight)
    await message.answer("Вы изменили рост")
    await state.clear()


# Обработчик состояния изменения опыт тренировок профиля
@routerr.callback_query(F.data == "update_training_experience")
async def update_user_data_training_experience(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    username = callback_query.from_user.username
    data_user = get_user_data(username)
    if data_user:
        await state.set_state(ChangeData.training_experience)
        await callback_query.message.answer("Введите рост на которое нужно изменить")


# Обработчик состояния изменения опыт тренировок профиля. Продолжение update_user_data_training_experience
@routerr.message(ChangeData.training_experience)
async def update_training_experience(message: Message, state: FSMContext) -> None:
    await state.update_data(training_experience=message.text)
    state_user_data = await state.get_data()
    username = message.from_user.username
    changed_training_experience = state_user_data["training_experience"]
    update_user_data(username=username, training_experience=changed_training_experience)
    await message.answer("Вы изменили рост")
    await state.clear()


# Обработчик состояния вернутся в основное меню
@routerr.message(F.text.lower() == "🔙 назад")
async def back_to_main_menu(message: Message) -> None:
    await message.answer(
        "Вы вернулись в сновное меню",
        reply_markup=generate_authorized_user_options_keyboard(),
    )
