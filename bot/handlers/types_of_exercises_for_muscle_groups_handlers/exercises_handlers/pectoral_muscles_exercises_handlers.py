"""Грудные мышцы"""
from aiogram import types, F
from aiogram.types import FSInputFile, InputMediaPhoto
from loguru import logger

from bot.keyboards.keyboard_exercises.exercises_for_the_pectoral_muscles_keyboard import \
    keyboard_exercises_for_the_pectoral_muscles_keyboard, keyboard_exercises_for_the_pectoral_muscles_keyboard_2, \
    return_to_exercises_for_the_pectoral_muscles_keyboard
from bot.messages.text.exercises_for_the_pectoral_muscles.exercises_for_the_pectoral_muscles_text import \
    exercises_for_the_pectoral_muscles_text, bench_press_horizontally_text, bent_over_barbell_press_text, \
    dumbbell_bench_press_text, dumbbell_raises_text, a_sweater_text, \
    bringing_hands_together_on_the_lower_crossover_block_text, reduction_of_arms_in_the_butterfly_simulator_text, \
    hummer_text, push_ups_text
from system.dispatcher import router, bot


@router.callback_query(F.data == "exercises_for_the_pectoral_muscles")
async def exercises_for_the_pectoral_muscles(callback_query: types.CallbackQuery):
    """Грудные мышцы. Выводим список кнопок с упражнениями"""
    try:
        document = FSInputFile('messages/images/exercises_for_the_pectoral_muscles/exercises_for_the_pectoral_muscles.jpg')
        media = InputMediaPhoto(media=document, caption=exercises_for_the_pectoral_muscles_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=keyboard_exercises_for_the_pectoral_muscles_keyboard(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")

@router.callback_query(F.data == "exercises_for_the_pectoral_muscles_2")
async def exercises_for_the_pectoral_muscles_2(callback_query: types.CallbackQuery):
    """Грудные мышцы. Выводим список кнопок с упражнениями"""
    try:
        document = FSInputFile('messages/images/exercises_for_the_pectoral_muscles/exercises_for_the_pectoral_muscles.jpg')
        media = InputMediaPhoto(media=document, caption=exercises_for_the_pectoral_muscles_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=keyboard_exercises_for_the_pectoral_muscles_keyboard_2(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "bench_press_horizontally")
async def bench_press_horizontally(callback_query: types.CallbackQuery) -> None:
    """Жим штанги лежа горизонтально. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/exercises_for_the_pectoral_muscles/bench_press_horizontally.jpg')
        media = InputMediaPhoto(media=document, caption=bench_press_horizontally_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_exercises_for_the_pectoral_muscles_keyboard(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "bent_over_barbell_press")
async def bent_over_barbell_press(callback_query: types.CallbackQuery) -> None:
    """Жим штанги в наклоне. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/exercises_for_the_pectoral_muscles/bent_over_barbell_press.jpg')
        media = InputMediaPhoto(media=document, caption=bent_over_barbell_press_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_exercises_for_the_pectoral_muscles_keyboard(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")

@router.callback_query(F.data == "dumbbell_bench_press")
async def dumbbell_bench_press(callback_query: types.CallbackQuery) -> None:
    """Жим гантелей лежа. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/exercises_for_the_pectoral_muscles/dumbbell_bench_press.jpg')
        media = InputMediaPhoto(media=document, caption=dumbbell_bench_press_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_exercises_for_the_pectoral_muscles_keyboard(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "dumbbell_raises")
async def dumbbell_raises(callback_query: types.CallbackQuery) -> None:
    """Разведение рук с гантелями. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/exercises_for_the_pectoral_muscles/dumbbell_raises.jpg')
        media = InputMediaPhoto(media=document, caption=dumbbell_raises_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_exercises_for_the_pectoral_muscles_keyboard(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "a_sweater")
async def a_sweater(callback_query: types.CallbackQuery) -> None:
    """Пуловер. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/exercises_for_the_pectoral_muscles/a_sweater.jpg')
        media = InputMediaPhoto(media=document, caption=a_sweater_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_exercises_for_the_pectoral_muscles_keyboard(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "bringing_hands_together_on_the_lower_crossover_block")
async def bringing_hands_together_on_the_lower_crossover_block(callback_query: types.CallbackQuery) -> None:
    """Сведение рук на нижнем блоке кроссовера. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/exercises_for_the_pectoral_muscles/bringing_hands_together_on_the_lower_crossover_block.jpg')
        media = InputMediaPhoto(media=document, caption=bringing_hands_together_on_the_lower_crossover_block_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_exercises_for_the_pectoral_muscles_keyboard(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "reduction_of_arms_in_the_butterfly_simulator")
async def reduction_of_arms_in_the_butterfly_simulator(callback_query: types.CallbackQuery) -> None:
    """Сведение рук в тренажере бабочка. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/exercises_for_the_pectoral_muscles/reduction_of_arms_in_the_butterfly_simulator.jpg')
        media = InputMediaPhoto(media=document, caption=reduction_of_arms_in_the_butterfly_simulator_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_exercises_for_the_pectoral_muscles_keyboard(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "hummer")
async def hummer(callback_query: types.CallbackQuery) -> None:
    """Хаммер. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/exercises_for_the_pectoral_muscles/hummer.jpg')
        media = InputMediaPhoto(media=document, caption=hummer_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_exercises_for_the_pectoral_muscles_keyboard(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")

@router.callback_query(F.data == "push_ups")
async def push_ups(callback_query: types.CallbackQuery) -> None:
    """Отжимания. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/exercises_for_the_pectoral_muscles/push_ups.jpg')
        media = InputMediaPhoto(media=document, caption=push_ups_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_exercises_for_the_pectoral_muscles_keyboard(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


def register_exercises_for_the_pectoral_muscles():
    """Регистрация обработчиков для бота. Грудные мышцы"""
    router.callback_query.register(exercises_for_the_pectoral_muscles)  # Перечень упражнений Грудные мышцы
    router.callback_query.register(exercises_for_the_pectoral_muscles_2)  # Перечень упражнений Грудные мышцы 2
    router.callback_query.register(bench_press_horizontally)  # Жим штанги лежа горизонтально
    router.callback_query.register(bent_over_barbell_press)  # Жим штанги в наклоне
    router.callback_query.register(dumbbell_bench_press)  # Жим гантелей лежа
    router.callback_query.register(dumbbell_raises)  # Разведение рук с гантелями
    router.callback_query.register(a_sweater)  # Пуловер
    router.callback_query.register(bringing_hands_together_on_the_lower_crossover_block)  # Сведение рук на нижнем блоке кроссовера
    router.callback_query.register(reduction_of_arms_in_the_butterfly_simulator)  # Сведение рук в тренажере бабочка
    router.callback_query.register(hummer)  # Хаммер
    router.callback_query.register(push_ups)  # Отжимания
