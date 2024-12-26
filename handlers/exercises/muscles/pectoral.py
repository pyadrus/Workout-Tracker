"""Грудные мышцы"""
from aiogram import types, F
from aiogram.types import FSInputFile, InputMediaPhoto
from loguru import logger

from data.config import router, bot
from keyboards.exercises.pectoral import pectoral_kb, pectoral_kb2, return_pectoral_kb
from messages.text.pectoral.exercises_for_the_pectoral_muscles_text import \
    pectoral_text, bench_text, bent_over_barbell_press_text, \
    dumbbell_press_text, dumbbell_raises_text, a_sweater_text, \
    crossover_text, butterfly_text, \
    hummer_text, pushups_text


@router.callback_query(F.data == "pectoral")
async def pectoral_ex1(callback_query: types.CallbackQuery):
    """Грудные мышцы. Выводим список кнопок с упражнениями"""
    try:
        document = FSInputFile(
            'messages/images/pectoral/pectoral.jpg')
        media = InputMediaPhoto(media=document, caption=pectoral_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=pectoral_kb(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "exercises_for_the_pectoral_muscles_2")
async def pectoral_ex2(callback_query: types.CallbackQuery):
    """Грудные мышцы. Выводим список кнопок с упражнениями"""
    try:
        document = FSInputFile(
            'messages/images/pectoral/pectoral.jpg')
        media = InputMediaPhoto(media=document, caption=pectoral_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=pectoral_kb2(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "bench_press_horizontally")
async def bench_press(callback_query: types.CallbackQuery) -> None:
    """Жим штанги лежа горизонтально. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/pectoral/bench_press.jpg')
        media = InputMediaPhoto(media=document, caption=bench_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_pectoral_kb(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "bent_over_barbell_press")
async def incline_press(callback_query: types.CallbackQuery) -> None:
    """Жим штанги в наклоне. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/pectoral/incline_press.jpg')
        media = InputMediaPhoto(media=document, caption=bent_over_barbell_press_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_pectoral_kb(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "dumbbell_bench_press")
async def dumbbell_press(callback_query: types.CallbackQuery) -> None:
    """Жим гантелей лежа. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/pectoral/dumbbell_bench_press.jpg')
        media = InputMediaPhoto(media=document, caption=dumbbell_press_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_pectoral_kb(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "dumbbell_raises")
async def dumbbell_fly(callback_query: types.CallbackQuery) -> None:
    """Разведение рук с гантелями. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/pectoral/dumbbell_raises.jpg')
        media = InputMediaPhoto(media=document, caption=dumbbell_raises_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_pectoral_kb(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "a_sweater")
async def pullover(callback_query: types.CallbackQuery) -> None:
    """Пуловер. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/pectoral/a_sweater.jpg')
        media = InputMediaPhoto(media=document, caption=a_sweater_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_pectoral_kb(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "bringing_hands_together_on_the_lower_crossover_block")
async def crossover_low(callback_query: types.CallbackQuery) -> None:
    """Сведение рук на нижнем блоке кроссовера. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile(
            'messages/images/pectoral/bringing_hands_together_on_the_lower_crossover_block.jpg')
        media = InputMediaPhoto(media=document, caption=crossover_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_pectoral_kb(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "reduction_of_arms_in_the_butterfly_simulator")
async def butterfly(callback_query: types.CallbackQuery) -> None:
    """Сведение рук в тренажере бабочка. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile(
            'messages/images/pectoral/reduction_of_arms_in_the_butterfly_simulator.jpg')
        media = InputMediaPhoto(media=document, caption=butterfly_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_pectoral_kb(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "hummer")
async def hummer(callback_query: types.CallbackQuery) -> None:
    """Хаммер. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/pectoral/hummer.jpg')
        media = InputMediaPhoto(media=document, caption=hummer_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_pectoral_kb(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "push_ups")
async def pushups(callback_query: types.CallbackQuery) -> None:
    """Отжимания. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/pectoral/push_ups.jpg')
        media = InputMediaPhoto(media=document, caption=pushups_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_pectoral_kb(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


def register_pectoral():
    """Регистрация обработчиков для бота. Грудные мышцы"""
    router.callback_query.register(pectoral_ex1)  # Перечень упражнений Грудные мышцы
    router.callback_query.register(pectoral_ex2)  # Перечень упражнений Грудные мышцы 2
    router.callback_query.register(bench_press)  # Жим штанги лежа горизонтально
    router.callback_query.register(incline_press)  # Жим штанги в наклоне
    router.callback_query.register(dumbbell_press)  # Жим гантелей лежа
    router.callback_query.register(dumbbell_fly)  # Разведение рук с гантелями
    router.callback_query.register(pullover)  # Пуловер
    router.callback_query.register(crossover_low)  # Сведение рук на нижнем блоке кроссовера
    router.callback_query.register(butterfly)  # Сведение рук в тренажере бабочка
    router.callback_query.register(hummer)  # Хаммер
    router.callback_query.register(pushups)  # Отжимания
