from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from data.config import router, ADMIN_USER_ID
from database.database import (
    get_user_data,  # Импорт функции получения пользователя из базы
    update_user_data,  # Импорт функции изменения данных пользователя в базе
)

from keyboards.keyboard_user.keyboards import (create_data_change_buttons,
                                               generate_keyboard_personal_account,
                                               generate_main_menu_keyboard,
                                               generate_admin_button)
from states.states import ChangeData
from utils.read_text import load_text_form_file


@router.callback_query(F.data == "personal_account")
async def users_personal_account(callback_query: CallbackQuery) -> None:
    """Обработчик состояния просмотра личного кабинета"""
    await callback_query.message.edit_text(
        f"{load_text_form_file('text_log_in_to_your_personal_account.json')}",
        reply_markup=generate_keyboard_personal_account(),
    )


@router.callback_query(F.data == "view_data")
async def user_data(callback_query: CallbackQuery) -> None:
    """Обработчик состояния, просмотр личных данных при регистрации"""
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


@router.callback_query(F.data == "back_personal_account")
async def back_to_personal_account(callback_query: CallbackQuery) -> None:
    """Обработчик состояния вернутся в основное меню"""
    await callback_query.message.edit_text(
        f"{load_text_form_file('text_log_in_to_your_personal_account.json')}",
        reply_markup=generate_keyboard_personal_account(),
    )


@router.callback_query(F.data == "update_name")
async def update_user_data_name(callback_query: CallbackQuery, state: FSMContext) -> None:
    """Обработчик состояния изменения имя профиля"""
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        await state.set_state(ChangeData.name)
        await callback_query.message.answer(
            f"{load_text_form_file('text_change_name.json')}"
        )


@router.message(ChangeData.name)
async def update_name(message: Message, state: FSMContext) -> None:
    """Обработчик состояния изменения имя профиля. Продолжение update_user_data_name"""
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


@router.callback_query(F.data == "update_height")
async def update_user_data_height(callback_query: CallbackQuery, state: FSMContext) -> None:
    """Обработчик состояния изменения рост профиля"""
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        await state.set_state(ChangeData.height)
        await callback_query.message.answer(
            f"{load_text_form_file('text_change_height.json')}"
        )


@router.message(ChangeData.height)
async def update_height(message: Message, state: FSMContext) -> None:
    """Обработчик состояния изменения имя профиля. Продолжение update_user_data_height"""
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


@router.callback_query(F.data == "update_weight")
async def update_user_data_weight(callback_query: CallbackQuery, state: FSMContext) -> None:
    """Обработчик состояния изменения вес профиля"""
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        await state.set_state(ChangeData.weight)
        await callback_query.message.answer(
            f"{load_text_form_file('text_change_weight.json')}"
        )


@router.message(ChangeData.weight)
async def update_weight(message: Message, state: FSMContext) -> None:
    """Обработчик состояния изменения вес профиля. Продолжение update_user_data_weight"""
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


@router.callback_query(F.data == "update_training_experience")
async def update_user_data_training_experience(callback_query: CallbackQuery, state: FSMContext) -> None:
    """Обработчик состояния изменения опыт тренировок профиля"""
    user_id = callback_query.from_user.id
    data_user = get_user_data(user_id)
    if data_user:
        await state.set_state(ChangeData.training_experience)
        await callback_query.message.answer(
            f"{load_text_form_file('text_change_training_experience.json')}"
        )


@router.message(ChangeData.training_experience)
async def update_training_experience(message: Message, state: FSMContext) -> None:
    """Обработчик состояния изменения опыт тренировок профиля. Продолжение update_user_data_training_experience"""
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


@router.callback_query(F.data == "back")
async def back_to_main_menu(callback_query: CallbackQuery) -> None:
    """Обработчик состояния вернутся в основное меню"""
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
                reply_markup=generate_main_menu_keyboard(),
            )
    else:
        await callback_query.message.edit_text(
            f"{load_text_form_file('text_hello_welcome.json')}",
            reply_markup=generate_main_menu_keyboard(),
        )
