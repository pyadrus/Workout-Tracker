# Основной файл, в котором будет содержать почти весь код бота
from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from data.text import text_description, text_hello_welcome

router = Router()


class Registration(StatesGroup):
    name = State()
    height = State()
    weight = State()
    training_experience = State()


@router.message(CommandStart())
async def start_bot(message: Message) -> None:
    kb = [
        [
            KeyboardButton(text="Регистрация"),
            KeyboardButton(text="Описание"),
        ]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите один из вариантов",
    )
    username = message.from_user.username
    await message.answer(
        f"Приветствую тебя, @{username}{text_hello_welcome()}",
        reply_markup=keyboard,
    )


@router.message(F.text.lower() == "описание")
async def description(message: Message) -> None:
    await message.answer(f"{text_description()}")


@router.message(F.text.lower() == "регистрация")
async def registration(message: Message, state: FSMContext) -> None:
    await state.set_state(Registration.name)
    await message.answer("Для регистрации введите своё имя")


@router.message(Registration.name)
async def get_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Registration.height)
    await message.answer("Введите свой рост в сантиметрах")


@router.message(Registration.height)
async def get_height(message: Message, state: FSMContext) -> None:
    await state.update_data(height=message.text)
    await state.set_state(Registration.weight)
    await message.answer("Введите свой вес в килограммах")


@router.message(Registration.weight)
async def get_training_experience(message: Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    await state.set_state(Registration.training_experience)
    await message.answer("Введите свой опыт в тренировках")


@router.message(Registration.training_experience)
async def registration_info(message: Message, state: FSMContext) -> None:
    await state.update_data(training_experience=message.text)
    data = await state.get_data()
    await message.answer(
        f"Данные регистрации:\n"
        f"Имя: {data.get('name')}\n"
        f"Рост: {data.get('height')}\n"
        f"Вес: {data.get('weight')}\n"
        f"Опыт тренировок: {data.get('training_experience')}"
    )
