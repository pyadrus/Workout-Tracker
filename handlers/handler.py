# Основной файл Telegram-бота, использующего aiogram для взаимодействия с пользователями.
# В этом файле создается логика обработки сообщений и FSM (Finite State Machine) для регистрации пользователей.

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from data.text import text_hello_welcome, text_description  # Импорты текстов приветствия и описания.
from keyboards.keyboards import generate_user_options_keyboard  # Импорт функции для создания клавиатуры.

router = Router()  # Создание маршрутизатора для обработки команд и сообщений.


class Registration(StatesGroup):
    name = State()  # Состояние ввода имени.
    height = State()  # Состояние ввода роста.
    weight = State()  # Состояние ввода веса.
    training_experience = State()  # Состояние ввода опыта тренировок.


# Обработчик команды /start, отправляющий приветственное сообщение и клавиатуру с вариантами.
@router.message(CommandStart())
async def start_bot(message: Message) -> None:
    """
    Отправляет приветственное сообщение пользователю при старте бота.

    Аргументы:
    :param message: Сообщение пользователя с командой /start.
    """
    username = message.from_user.username
    await message.answer(
        f"👋 Приветствую тебя, @{username}{text_hello_welcome()}",
        reply_markup=generate_user_options_keyboard(),
    )


# Обработчик сообщения с текстом "описание", отправляющий описание бота.
@router.message(F.text.lower() == "описание")
async def description(message: Message) -> None:
    """
    Отправляет описание бота пользователю.

    Аргументы:
    :param message: Сообщение пользователя с текстом "описание".
    """
    await message.answer(f"ℹ️ {text_description()}")


# Обработчик сообщения с текстом "регистрация", начинающий процесс регистрации.
@router.message(F.text.lower() == "регистрация")
async def registration(message: Message, state: FSMContext) -> None:
    """
    Начинает процесс регистрации пользователя.

    Аргументы:
    :param message: Сообщение пользователя с текстом "регистрация".
    :param state: Контекст состояния FSM.
    """
    await state.update_data(name=message.text)
    await state.set_state(Registration.name)
    await message.answer("✍️ Для регистрации введите своё имя")


# Обработчик состояния ввода имени пользователя.
@router.message(Registration.name)
async def get_name(message: Message, state: FSMContext) -> None:
    """
    Запрашивает рост пользователя после ввода имени.

    Аргументы:
    :param message: Сообщение пользователя с именем.
    :param state: Контекст состояния FSM.
    """
    await state.update_data(name=message.text)
    await state.set_state(Registration.height)
    await message.answer("📏 Введите свой рост в сантиметрах")


# Обработчик состояния ввода роста пользователя.
@router.message(Registration.height)
async def get_height(message: Message, state: FSMContext) -> None:
    """
    Запрашивает вес пользователя после ввода роста.

    Аргументы:
    :param message: Сообщение пользователя с ростом.
    :param state: Контекст состояния FSM.
    """
    await state.update_data(height=message.text)
    await state.set_state(Registration.weight)
    await message.answer("⚖️ Введите свой вес в килограммах")


# Обработчик состояния ввода веса пользователя.
@router.message(Registration.weight)
async def get_training_experience(message: Message, state: FSMContext) -> None:
    """
    Запрашивает опыт тренировок пользователя после ввода веса.

    Аргументы:
    :param message: Сообщение пользователя с весом.
    :param state: Контекст состояния FSM.
    """
    await state.update_data(weight=message.text)
    await state.set_state(Registration.training_experience)
    await message.answer("🏋️ Введите свой опыт в тренировках")


# Обработчик состояния ввода опыта тренировок, завершающий процесс регистрации.
@router.message(Registration.training_experience)
async def registration_info(message: Message, state: FSMContext) -> None:
    """
    Завершает процесс регистрации и отображает введенные пользователем данные.

    Аргументы:
    :param message: Сообщение пользователя с опытом тренировок.
    :param state: Контекст состояния FSM.
    """
    user_data = await state.get_data()
    await message.answer(
        f"✅ Данные регистрации:\n"
        f"👤 Имя: {user_data['name']}\n"
        f"📏 Рост: {user_data['height']} см\n"
        f"⚖️ Вес: {user_data['weight']} кг\n"
        f"🏋️ Опыт тренировок: {user_data['training_experience']}"
    )
    await state.clear()  # Сброс состояния после завершения регистрации.
