from aiogram import types, F
from aiogram.types import FSInputFile, InputMediaPhoto
from loguru import logger

from bot.data.config import router, bot
from bot.keyboards.exercises.keyboard_biceps_exercises import (return_to_biceps_exercises,
                                                               keyboard_biceps_exercises,
                                                               keyboard_biceps_exercises_2)
from bot.messages.text.biceps_exercises.biceps_exercises_text import (biceps_exercises_text,
                                                                      arm_bending_with_elbow_abduction_execution,
                                                                      scott_bench_curl_execution,
                                                                      concentrated_arm_curls_execution,
                                                                      incline_dumbbell_curl_execution,
                                                                      hammer_grip_curl_execution,
                                                                      bent_over_barbell_row_with_reverse_grip_execution,
                                                                      reverse_grip_pull_ups_execution,
                                                                      dumbbell_curl_execution,
                                                                      bend_the_arms_on_the_lower_block_execution,
                                                                      curls_with_a_barbell_or_EZ_bar_execution)


@router.callback_query(F.data == "biceps_exercises")
async def biceps_exercises(callback_query: types.CallbackQuery):
    """Упражнения на трицепс. Выводим список кнопок с упражнениями"""
    try:
        document = FSInputFile('messages/images/biceps_exercises/biceps_exercises.jpg')
        media = InputMediaPhoto(media=document, caption=biceps_exercises_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=keyboard_biceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "biceps_exercises_2")
async def biceps_exercises_2(callback_query: types.CallbackQuery):
    """Упражнения на трицепс. Выводим список кнопок с упражнениями"""
    try:
        document = FSInputFile('messages/images/biceps_exercises/biceps_exercises.jpg')
        media = InputMediaPhoto(media=document, caption=biceps_exercises_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=keyboard_biceps_exercises_2(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "curls_with_a_barbell_or_EZ_bar")
async def curls_with_a_barbell_or_EZ_bar(callback_query: types.CallbackQuery) -> None:
    """Сгибание рук со штангой или EZ-штангой. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/biceps_exercises/curls_with_a_barbell_or_EZ_bar.jpg')
        media = InputMediaPhoto(media=document, caption=curls_with_a_barbell_or_EZ_bar_execution)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_biceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "bend_the_arms_on_the_lower_block")
async def bend_the_arms_on_the_lower_block(callback_query: types.CallbackQuery) -> None:
    """Сгибание рук на нижнем блоке. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/biceps_exercises/bend_the_arms_on_the_lower_block.jpg')
        media = InputMediaPhoto(media=document, caption=bend_the_arms_on_the_lower_block_execution)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_biceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "dumbbell_curl")
async def dumbbell_curl(callback_query: types.CallbackQuery) -> None:
    """Сгибание рук с гантелями. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/biceps_exercises/dumbbell_curl.jpg')
        media = InputMediaPhoto(media=document, caption=dumbbell_curl_execution)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_biceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "reverse_grip_pull_ups")
async def reverse_grip_pull_ups(callback_query: types.CallbackQuery) -> None:
    """Подтягивания обратным хватом. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/biceps_exercises/reverse_grip_pull_ups.jpg')
        media = InputMediaPhoto(media=document, caption=reverse_grip_pull_ups_execution)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_biceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "bent_over_barbell_row_with_reverse_grip")
async def bent_over_barbell_row_with_reverse_grip(callback_query: types.CallbackQuery) -> None:
    """Тяга штанги в наклоне обратным хватом. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/biceps_exercises/bent_over_barbell_row_with_reverse_grip.jpg')
        media = InputMediaPhoto(media=document, caption=bent_over_barbell_row_with_reverse_grip_execution)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_biceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "hammer_grip_curl")
async def hammer_grip_curl(callback_query: types.CallbackQuery) -> None:
    """Сгибание рук хватом «молот». Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/biceps_exercises/hammer_grip_curl.jpg')
        media = InputMediaPhoto(media=document, caption=hammer_grip_curl_execution)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_biceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "incline_dumbbell_curl")
async def incline_dumbbell_curl(callback_query: types.CallbackQuery) -> None:
    """Сгибание рук с гантелями на наклонной скамье. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/biceps_exercises/incline_dumbbell_curl.jpg')
        media = InputMediaPhoto(media=document, caption=incline_dumbbell_curl_execution)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_biceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "concentrated_arm_curls")
async def concentrated_arm_curls(callback_query: types.CallbackQuery) -> None:
    """Концентрированные сгибания рук. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/biceps_exercises/concentrated_arm_curls.jpg')
        media = InputMediaPhoto(media=document, caption=concentrated_arm_curls_execution)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_biceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "scott_bench_curl")
async def scott_bench_curl(callback_query: types.CallbackQuery) -> None:
    """Сгибание рук со штангой на скамье Скотта. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/biceps_exercises/scott_bench_curl.jpg')
        media = InputMediaPhoto(media=document, caption=scott_bench_curl_execution)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_biceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "arm_bending_with_elbow_abduction")
async def arm_bending_with_elbow_abduction(callback_query: types.CallbackQuery) -> None:
    """Сгибание рук с отведением локтей. Источник информации https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    try:
        document = FSInputFile('messages/images/biceps_exercises/arm_bending_with_elbow_abduction.jpg')
        media = InputMediaPhoto(media=document, caption=arm_bending_with_elbow_abduction_execution)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_biceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


def register_biceps():
    """Регистрация обработчиков для бота. Упражнения на бицепс"""
    router.callback_query.register(biceps_exercises)  # Перечень упражнений на бицепс
    router.callback_query.register(biceps_exercises_2)  # Перечень упражнений на бицепс 2
    router.callback_query.register(curls_with_a_barbell_or_EZ_bar)  # Сгибание рук со штангой или EZ-штангой
    router.callback_query.register(bend_the_arms_on_the_lower_block)  # Сгибание рук на нижнем блоке
    router.callback_query.register(dumbbell_curl)  # Сгибание рук с гантелями
    router.callback_query.register(reverse_grip_pull_ups)  # Подтягивания обратным хватом
    router.callback_query.register(bent_over_barbell_row_with_reverse_grip)  # Тяга штанги в наклоне обратным хватом
    router.callback_query.register(hammer_grip_curl)  # Сгибание рук хватом «молот»
    router.callback_query.register(incline_dumbbell_curl)  # Сгибание рук с гантелями на наклонной скамье.
    router.callback_query.register(concentrated_arm_curls)  # Концентрированные сгибания рук
    router.callback_query.register(scott_bench_curl)  # Сгибание рук со штангой на скамье Скотта.
    router.callback_query.register(arm_bending_with_elbow_abduction)  # Сгибание рук с отведением локтей
