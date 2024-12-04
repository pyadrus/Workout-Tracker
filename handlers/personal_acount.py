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


@routerr.message(ChangeData.name)
async def update_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    state_user_data = await state.get_data()
    username = message.from_user.username
    changed_name = state_user_data["name"]
    update_user_data(username=username, name=changed_name)
    await message.answer("Вы изменили имя")
    await state.clear()


# Обработчик состояния вернутся в основное меню
@routerr.message(F.text.lower() == "🔙 назад")
async def back_to_main_menu(message: Message) -> None:
    await message.answer(
        "Вы вернулись в сновное меню",
        reply_markup=generate_authorized_user_options_keyboard(),
    )
