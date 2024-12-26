from datetime import datetime

from aiogram import F
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from loguru import logger

from bot.data.data import save_data_to_db
from bot.keyboards.keyboard_user.keyboard_help import keyboard_help
from bot.states.states import FormeditMainMenu
from system.dispatcher import router, bot


@router.callback_query(F.data == "CommandStart")
async def workout_recording_handlers(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    """Начать запись тренировок"""
    try:
        await state.clear()  # Очистка предыдущих состояний

        user_id = callback_query.from_user.id
        user_name = callback_query.from_user.username or ""
        user_first_name = callback_query.from_user.first_name or ""
        user_last_name = callback_query.from_user.last_name or ""

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"User Info: {user_id}, {user_name}, {user_first_name}, {user_last_name}, {current_time}")

        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Приветствую! Я помогу вести журнал тренировок. Введите название упражнения:",
            reply_markup=keyboard_help()  # Убедитесь, что функция keyboard_menu() возвращает правильную клавиатуру
        )

        await state.set_state(FormeditMainMenu.text_edit_main_menu)

    except Exception as e:
        logger.error(f"Ошибка: {e}")


# Обработчики для каждого состояния
@router.message(FormeditMainMenu.text_edit_main_menu)
async def process_exercise_name(message: Message, state: FSMContext):
    try:
        exercise_name = message.text.strip()
        await state.update_data(exercise_name=exercise_name)
        await message.answer("Введите количество повторений:", reply_markup=keyboard_help())
        await state.set_state(FormeditMainMenu.repetitions)

    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.message(FormeditMainMenu.repetitions)
async def process_repetitions(message: Message, state: FSMContext):
    try:
        repetitions = message.text.strip()
        await state.update_data(repetitions=repetitions)
        await message.answer("Введите количество подходов:", reply_markup=keyboard_help())
        await state.set_state(FormeditMainMenu.approaches)

    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.message(FormeditMainMenu.approaches)
async def process_approaches(message: Message, state: FSMContext):
    try:
        approaches = message.text.strip()
        await state.update_data(approaches=approaches)
        await message.answer("Введите вес:", reply_markup=keyboard_help())
        await state.set_state(FormeditMainMenu.weight)

    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.message(FormeditMainMenu.weight)
async def process_weight(message: Message, state: FSMContext):
    try:
        weight = message.text.strip()
        if not weight.isdigit():
            await message.answer("Пожалуйста, введите вес в виде числа.", keyboard_help())
            return

        weight = int(weight)  # Преобразуем вес в число
        data = await state.get_data()

        user_id = message.from_user.id
        exercise_name = data["exercise_name"]
        repetitions = int(data["repetitions"])  # Преобразуем количество повторений в число
        approaches = int(data["approaches"])  # Преобразуем количество подходов в число

        # Подсчёт общего веса
        total_weight = weight * repetitions * approaches

        # Сохранение данных в базу данных
        save_data_to_db(
            user_id=user_id,
            exercise_name=exercise_name,
            repetitions=repetitions,
            approaches=approaches,
            weight=weight,
            total_weight=total_weight
        )

        result = (
            f"Вы ввели данные:\n"
            f"Упражнение: {exercise_name}\n"
            f"Повторений: {repetitions}\n"
            f"Подходов: {approaches}\n"
            f"Вес за один подход: {weight} кг\n\n"
            f"Общий вес: {total_weight} кг\n\n"
            f"Данные успешно сохранены в базу данных!"
        )
        await message.answer(result, reply_markup=keyboard_help())
        await state.clear()  # Очистка состояния

    except ValueError:
        await message.answer("Пожалуйста, убедитесь, что все введённые данные — это числа.",
                             reply_markup=keyboard_help())
    except Exception as e:
        logger.error(f"Ошибка: {e}")


def register_workout_recording_handlers():
    """Регистрация обработчиков для бота."""
    router.callback_query.register(workout_recording_handlers)  # Запись тренировки в базу данных