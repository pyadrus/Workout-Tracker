# Основной файл, в котором будет содержать почти весь код бота
from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from text import text_hello_welcome, text_description

router = Router()


@router.message(CommandStart())
async def hello(message: Message) -> None:
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


@router.message(F.text.lower() == "регистрация")
async def registration(message: Message) -> None:
    await message.answer("Отличный выбор")


@router.message(F.text.lower() == "описание")
async def description(message: Message) -> None:
    await message.answer(f"{text_description()}")
