# Основной файл, в котором будет содержать почти весь код бота
from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from data.text import text_hello_welcome, text_description

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
    await state.update_data(name=message.text)
    await state.set_state(Registration.name)
    await message.answer("Для регистрации введите своё имя")


@router.message(Registration.name)
async def get_name(message: Message, state: FSMContext) -> None:
    await state.update_data(height=message.text)
    await state.set_state(Registration.height)
    await message.answer("Введите свой рост в сантиметрах")


@router.message(Registration.height)
async def get_height(message: Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    await state.set_state(Registration.weight)
    await message.answer("Введите свой вес в килограммах")


@router.message(Registration.weight)
async def get_training_experience(message: Message, state: FSMContext) -> None:
    await state.update_data(training_experience=message.text)
    await state.set_state(Registration.training_experience)
    await message.answer("Введите свой опыт в тренировках")


@router.message(Registration.training_experience)
async def registration_info(message: Message) -> None:
    await message.answer(
        f"Данные регистрации:\n" f"Имя: \n" f"Рост: \n" f"Вес: \n" f"Опыт тренировок: "
    )
