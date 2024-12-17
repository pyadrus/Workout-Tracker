from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from handlers.start import ADMIN_USER_ID, load_text_form_file
from database.database import (
    get_user_data,  # Импорт функции получения пользователя из базы
    update_user_data,  # Импорт функции изменения данных пользователя в базе
)
from keyboards.keyboards import (
    create_data_change_buttons,
    generate_authorized_user_options_keyboard,
    generate_keyboard_personal_account,
    generate_user_options_keyboard,
    generate_admin_panel_keyboard,
    generate_admin_button,
)


routerr = Router()  # Создание маршрутизатора для обработки команд и сообщений.


class ChangeData(StatesGroup):
    name = State()  # Состояние ввода имени.
    height = State()  # Состояние ввода роста.
    weight = State()  # Состояние ввода веса.
    training_experience = State()  # Состояние ввода опыта тренировок.


# Обработчик состояния просмотра личного кабинета
@routerr.callback_query(F.data == "personal_account")
async def users_personal_account(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer(
        "Вы вошли в личный кабинет", reply_markup=generate_keyboard_personal_account()
    )


# Обработчик состояния просмотря личных данных при регистрации
@routerr.callback_query(F.data == "view_data")
async def user_data(callback_query: CallbackQuery) -> None:
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        _, name, height, weight, training_experience = data_user
        await callback_query.message.answer(
            f"📋 Ваш профиль:\n"
            f"👤 Имя - {name}\n"
            f"📏 Рост - {height} см\n"
            f"⚖️ Вес - {weight} кг\n"
            f"🏋️ Опыт тренировок - {training_experience}",
            reply_markup=create_data_change_buttons(),
        )


# Обработчик состояния вернутся в основное меню
@routerr.callback_query(F.data == "back_personal_account")
async def back_to_personal_account(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer(
        "Вы вошли в личный кабинет",
        reply_markup=generate_keyboard_personal_account(),
    )


# Обработчик состояния изменения имя профиля
@routerr.callback_query(F.data == "update_name")
async def update_user_data_name(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        await state.set_state(ChangeData.name)
        await callback_query.message.answer("👤 Введите имя на которое нужно изменить")


# Обработчик состояния изменения имя профиля. Продолжение update_user_data_name
@routerr.message(ChangeData.name)
async def update_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    state_user_data = await state.get_data()
    user_id = message.from_user.id
    changed_name = state_user_data["name"]
    update_user_data(id_user_telegram=user_id, name=changed_name)
    await message.answer("👤 Вы изменили имя")
    await message.answer(
        "Вы вошли в личный кабинет",
        reply_markup=generate_keyboard_personal_account(),
    )
    await state.clear()


# Обработчик состояния изменения рост профиля
@routerr.callback_query(F.data == "update_height")
async def update_user_data_height(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        await state.set_state(ChangeData.height)
        await callback_query.message.answer("📏 Введите рост на которое нужно изменить")


# Обработчик состояния изменения имя профиля. Продолжение update_user_data_height
@routerr.message(ChangeData.height)
async def update_height(message: Message, state: FSMContext) -> None:
    await state.update_data(height=message.text)
    state_user_data = await state.get_data()
    user_id = message.from_user.id
    changed_height = state_user_data["height"]
    update_user_data(id_user_telegram=user_id, height=changed_height)
    await message.answer("📏 Вы изменили рост")
    await message.answer(
        "Вы вошли в личный кабинет",
        reply_markup=generate_keyboard_personal_account(),
    )
    await state.clear()


# Обработчик состояния изменения вес профиля
@routerr.callback_query(F.data == "update_weight")
async def update_user_data_weight(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        await state.set_state(ChangeData.weight)
        await callback_query.message.answer("⚖️ Введите вес на которое нужно изменить")


# Обработчик состояния изменения вес профиля. Продолжение update_user_data_weight
@routerr.message(ChangeData.weight)
async def update_weight(message: Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    state_user_data = await state.get_data()
    user_id = message.from_user.id
    changed_weight = state_user_data["weight"]
    update_user_data(id_user_telegram=user_id, weight=changed_weight)
    await message.answer("⚖️ Вы изменили вес")
    await message.answer(
        "Вы вошли в личный кабинет",
        reply_markup=generate_keyboard_personal_account(),
    )
    await state.clear()


# Обработчик состояния изменения опыт тренировок профиля
@routerr.callback_query(F.data == "update_training_experience")
async def update_user_data_training_experience(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        await state.set_state(ChangeData.training_experience)
        await callback_query.message.answer("🏋️ Введите рост на которое нужно изменить")


# Обработчик состояния изменения опыт тренировок профиля. Продолжение update_user_data_training_experience
@routerr.message(ChangeData.training_experience)
async def update_training_experience(message: Message, state: FSMContext) -> None:
    await state.update_data(training_experience=message.text)
    state_user_data = await state.get_data()
    user_id = message.from_user.id
    changed_training_experience = state_user_data["training_experience"]
    update_user_data(
        id_user_telegram=user_id, training_experience=changed_training_experience
    )
    await message.answer("🏋️ Вы изменили опыт тренировок")
    await message.answer(
        "Вы вошли в личный кабинет",
        reply_markup=generate_keyboard_personal_account(),
    )
    await state.clear()


# Обработчик состояния вернутся в основное меню
@routerr.callback_query(F.data == "back")
async def back_to_main_menu(callback_query: CallbackQuery) -> None:
    username = callback_query.from_user.username
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        if get_user_data(ADMIN_USER_ID):
            await callback_query.message.answer(
                f"👋 Приветствую тебя, @{username}{load_text_form_file('text_authorized_user_greeting.json')}",
                reply_markup=generate_admin_button(),
            )
        else:
            await callback_query.message.answer(
                f"👋 Приветствую тебя, @{username}{load_text_form_file('text_authorized_user_greeting.json')}",
                reply_markup=generate_authorized_user_options_keyboard(),
            )
    else:
        await callback_query.message.answer(
            f"👋 Приветствую тебя, @{username}{load_text_form_file('text_hello_welcome.json')}",
            reply_markup=generate_user_options_keyboard(),
        )


# Обработчик состояния админской-панели
@routerr.callback_query(F.data == "admin_panel")
async def login_to_the_admin_panel(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer(
        "Админ-панель", reply_markup=generate_admin_panel_keyboard()
    )


# Обработчик состояния рассылка сообщений пользователям
@routerr.callback_query(F.data == "sending_messages")
async def sending_messages_by_user(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer("Разослать сообщения")


# Обработчик состояния статистики
@routerr.callback_query(F.data == "statistics")
async def user_activity_analysis(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer("Статистика")
