from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from bot.handlers.launch_bot import ADMIN_USER_ID
from bot.utils.read_text import load_text_form_file
from bot.database.database import (
    get_user_data,  # Импорт функции получения пользователя из базы
    update_user_data,  # Импорт функции изменения данных пользователя в базе
)
from bot.keyboards.keyboards import (
    create_data_change_buttons,
    generate_authorized_user_options_keyboard,
    generate_keyboard_personal_account,
    generate_user_options_keyboard,
    generate_admin_button,
)

router_personal_acount = (
    Router()
)  # Создание маршрутизатора для обработки команд и сообщений.


class ChangeData(StatesGroup):
    name = State()  # Состояние ввода для изменения имени.
    height = State()  # Состояние ввода для изменения роста.
    weight = State()  # Состояние ввода для изменения веса.
    training_experience = State()  # Состояние ввода для изменения опыта тренировок.


# Обработчик состояния просмотра личного кабинета
@router_personal_acount.callback_query(F.data == "personal_account")
async def users_personal_account(callback_query: CallbackQuery) -> None:
    await callback_query.message.edit_text(
        f"{load_text_form_file('text_log_in_to_your_personal_account.json')}",
        reply_markup=generate_keyboard_personal_account(),
    )


# Обработчик состояния просмотря личных данных при регистрации
@router_personal_acount.callback_query(F.data == "view_data")
async def user_data(callback_query: CallbackQuery) -> None:
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        _, name, height, weight, training_experience = data_user
        await callback_query.message.edit_text(
            load_text_form_file("text_data_profile.json").format(
                name=name,
                height=height,
                weight=weight,
                training_experience=training_experience,
            ),
            reply_markup=create_data_change_buttons(),
        )


# Обработчик состояния вернутся в основное меню
@router_personal_acount.callback_query(F.data == "back_personal_account")
async def back_to_personal_account(callback_query: CallbackQuery) -> None:
    await callback_query.message.edit_text(
        f"{load_text_form_file('text_log_in_to_your_personal_account.json')}",
        reply_markup=generate_keyboard_personal_account(),
    )


# Обработчик состояния изменения имя профиля
@router_personal_acount.callback_query(F.data == "update_name")
async def update_user_data_name(
        callback_query: CallbackQuery, state: FSMContext
) -> None:
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        await state.set_state(ChangeData.name)
        await callback_query.message.answer(
            f"{load_text_form_file('text_change_name.json')}"
        )


# Обработчик состояния изменения имя профиля. Продолжение update_user_data_name
@router_personal_acount.message(ChangeData.name)
async def update_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    state_user_data = await state.get_data()
    user_id = message.from_user.id
    changed_name = state_user_data["name"]
    update_user_data(id_user_telegram=user_id, name=changed_name)
    await message.answer("👤 Вы изменили имя")
    await message.answer(
        f"{load_text_form_file('text_log_in_to_your_personal_account.json')}",
        reply_markup=generate_keyboard_personal_account(),
    )
    await state.clear()


# Обработчик состояния изменения рост профиля
@router_personal_acount.callback_query(F.data == "update_height")
async def update_user_data_height(
        callback_query: CallbackQuery, state: FSMContext
) -> None:
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        await state.set_state(ChangeData.height)
        await callback_query.message.answer(
            f"{load_text_form_file('text_change_height.json')}"
        )


# Обработчик состояния изменения имя профиля. Продолжение update_user_data_height
@router_personal_acount.message(ChangeData.height)
async def update_height(message: Message, state: FSMContext) -> None:
    await state.update_data(height=message.text)
    state_user_data = await state.get_data()
    user_id = message.from_user.id
    changed_height = state_user_data["height"]
    update_user_data(id_user_telegram=user_id, height=changed_height)
    await message.answer("📏 Вы изменили рост")
    await message.answer(
        f"{load_text_form_file('text_log_in_to_your_personal_account.json')}",
        reply_markup=generate_keyboard_personal_account(),
    )
    await state.clear()


# Обработчик состояния изменения вес профиля
@router_personal_acount.callback_query(F.data == "update_weight")
async def update_user_data_weight(
        callback_query: CallbackQuery, state: FSMContext
) -> None:
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        await state.set_state(ChangeData.weight)
        await callback_query.message.answer(
            f"{load_text_form_file('text_change_weight.json')}"
        )


# Обработчик состояния изменения вес профиля. Продолжение update_user_data_weight
@router_personal_acount.message(ChangeData.weight)
async def update_weight(message: Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    state_user_data = await state.get_data()
    user_id = message.from_user.id
    changed_weight = state_user_data["weight"]
    update_user_data(id_user_telegram=user_id, weight=changed_weight)
    await message.answer("⚖️ Вы изменили вес")
    await message.answer(
        f"{load_text_form_file('text_log_in_to_your_personal_account.json')}",
        reply_markup=generate_keyboard_personal_account(),
    )
    await state.clear()


# Обработчик состояния изменения опыт тренировок профиля
@router_personal_acount.callback_query(F.data == "update_training_experience")
async def update_user_data_training_experience(
        callback_query: CallbackQuery, state: FSMContext
) -> None:
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        await state.set_state(ChangeData.training_experience)
        await callback_query.message.answer(
            f"{load_text_form_file('text_change_training_experience.json')}"
        )


# Обработчик состояния изменения опыт тренировок профиля. Продолжение update_user_data_training_experience
@router_personal_acount.message(ChangeData.training_experience)
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
        f"{load_text_form_file('text_log_in_to_your_personal_account.json')}",
        reply_markup=generate_keyboard_personal_account(),
    )
    await state.clear()


# Обработчик состояния вернутся в основное меню
@router_personal_acount.callback_query(F.data == "back")
async def back_to_main_menu(callback_query: CallbackQuery) -> None:
    username = callback_query.from_user.username
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        if get_user_data(ADMIN_USER_ID):
            await callback_query.message.edit_text(
                f"{load_text_form_file('text_authorized_user_greeting.json')}",
                reply_markup=generate_admin_button(),
            )
        else:
            await callback_query.message.edit_text(
                f"{load_text_form_file('text_authorized_user_greeting.json')}",
                reply_markup=generate_authorized_user_options_keyboard(),
            )
    else:
        await callback_query.message.edit_text(
            f"{load_text_form_file('text_hello_welcome.json')}",
            reply_markup=generate_user_options_keyboard(),
        )
