from aiogram import types, F
from aiogram.types import FSInputFile, InputMediaPhoto
from loguru import logger

from bot.data.config import router, bot
from bot.keyboards.exercises.keyboard_triceps_exercises import (keyboard_triceps_exercises,
                                                                return_to_triceps_exercises,
                                                                keyboard_triceps_exercises_2)
from bot.messages.text.triceps_exercises.triceps_exercises_text import (triceps_exercises_text, diamond_push_ups_text,
                                                                        reverse_push_ups_on_a_bench_text, dips_text,
                                                                        french_bench_press_with_barbell_text,
                                                                        dumbbell_overhead_press_text,
                                                                        bent_over_arm_extension_with_dumbbells_text,
                                                                        extension_of_one_arm_with_support_on_the_bench_text,
                                                                        extension_of_arms_on_a_block_with_a_rope_handle_text,
                                                                        extension_of_arms_on_a_block_with_a_reverse_grip_text,
                                                                        extension_on_the_block_from_behind_the_head_text)


@router.callback_query(F.data == "triceps_exercises")
async def triceps_exercises(callback_query: types.CallbackQuery):
    """Упражнения на трицепс. Выводим список кнопок с упражнениями"""
    try:
        document = FSInputFile('messages/images/triceps_exercises/triceps_exercises.jpg')
        media = InputMediaPhoto(media=document, caption=triceps_exercises_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=keyboard_triceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "triceps_exercises_2")
async def triceps_exercises(callback_query: types.CallbackQuery):
    """Упражнения на трицепс. Выводим список кнопок с упражнениями"""
    try:
        document = FSInputFile('messages/images/triceps_exercises/triceps_exercises.jpg')
        media = InputMediaPhoto(media=document, caption=triceps_exercises_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=keyboard_triceps_exercises_2(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "diamond_push_ups")
async def diamond_push_ups(callback_query: types.CallbackQuery) -> None:
    """Алмазные отжимания. Источник информации https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/"""
    try:
        document = FSInputFile('messages/images/triceps_exercises/diamond_push_ups.jpg')
        media = InputMediaPhoto(media=document, caption=diamond_push_ups_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_triceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "reverse_push_ups_on_a_bench")
async def reverse_push_ups_on_a_bench(callback_query: types.CallbackQuery) -> None:
    """Обратные отжимания на скамье. Источник информации https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/"""
    try:
        document = FSInputFile('messages/images/triceps_exercises/reverse_push_ups_on_a_bench.jpg')
        media = InputMediaPhoto(media=document, caption=reverse_push_ups_on_a_bench_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_triceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "dips")
async def dips(callback_query: types.CallbackQuery) -> None:
    """Отжимания на брусьях. Источник информации https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/"""
    try:
        document = FSInputFile('messages/images/triceps_exercises/dips.jpg')
        media = InputMediaPhoto(media=document, caption=dips_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_triceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "french_bench_press_with_barbell")
async def french_bench_press_with_barbell(callback_query: types.CallbackQuery) -> None:
    """Французский жим лёжа со штангой. Источник информации https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/"""
    try:
        document = FSInputFile('messages/images/triceps_exercises/french_bench_press_with_barbell.jpg')
        media = InputMediaPhoto(media=document, caption=french_bench_press_with_barbell_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_triceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "dumbbell_overhead_press")
async def dumbbell_overhead_press(callback_query: types.CallbackQuery) -> None:
    """Жим гантели из-за головы. Источник информации https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/"""
    try:
        document = FSInputFile('messages/images/triceps_exercises/dumbbell_overhead_press.jpg')
        media = InputMediaPhoto(media=document, caption=dumbbell_overhead_press_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_triceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "bent_over_arm_extension_with_dumbbells")
async def bent_over_arm_extension_with_dumbbells(callback_query: types.CallbackQuery) -> None:
    """Разгибание рук с гантелями в наклоне. Источник информации https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/"""
    try:
        document = FSInputFile('messages/images/triceps_exercises/bent_over_arm_extension_with_dumbbells.jpg')
        media = InputMediaPhoto(media=document, caption=bent_over_arm_extension_with_dumbbells_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_triceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "extension_of_one_arm_with_support_on_the_bench")
async def one_arm_extension(callback_query: types.CallbackQuery) -> None:
    """
    Обрабатывает нажатие на кнопку "Разгибание одной руки с опорой на лавку".

    Загружает изображение упражнения и обновляет сообщение с описанием и
    кнопками для возврата к другим упражнениям на трицепс.

    Источник информации: https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/

    Args:
        callback_query (types.CallbackQuery): Объект колбэка с данными от Telegram.

    Raises:
        Exception: Логирует ошибки, если возникает проблема с загрузкой изображения
        или обновлением сообщения.
    """
    try:
        document = FSInputFile('messages/images/triceps_exercises/extension_of_one_arm_with_support_on_the_bench.jpg')
        media = InputMediaPhoto(media=document, caption=extension_of_one_arm_with_support_on_the_bench_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_triceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "extension_of_arms_on_a_block_with_a_rope_handle")
async def block_rope_extension(callback_query: types.CallbackQuery) -> None:
    """
    Обрабатывает нажатие на кнопку "Разгибание рук на блоке с канатной рукоятью".

    Загружает изображение упражнения и обновляет сообщение с описанием,
    добавляя кнопки для возврата к другим упражнениям на трицепс.

    Источник информации: https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/

    Args:
        callback_query (types.CallbackQuery): Объект колбэка с данными от Telegram.

    Raises:
        Exception: Логирует ошибки, если возникают проблемы с загрузкой изображения
        или обновлением сообщения.
    """
    try:
        document = FSInputFile('messages/images/triceps_exercises/extension_of_arms_on_a_block_with_a_rope_handle.jpg')
        media = InputMediaPhoto(media=document, caption=extension_of_arms_on_a_block_with_a_rope_handle_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_triceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "extension_of_arms_on_a_block_with_a_reverse_grip")
async def reverse_grip_extension(callback_query: types.CallbackQuery) -> None:
    """
    Обрабатывает нажатие на кнопку "Разгибание рук на блоке обратным хватом".

    Загружает изображение упражнения и обновляет сообщение с описанием,
    добавляя кнопки для возврата к другим упражнениям на трицепс.

    Источник информации: https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/

    Args:
        callback_query (types.CallbackQuery): Объект колбэка с данными от Telegram.

    Raises:
        Exception: Логирует ошибки, если возникают проблемы с загрузкой изображения
        или обновлением сообщения.
    """
    try:
        document = FSInputFile('messages/images/triceps_exercises/extension_of_arms_on_a_block_with_a_reverse_grip.jpg')
        media = InputMediaPhoto(media=document, caption=extension_of_arms_on_a_block_with_a_reverse_grip_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_triceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


@router.callback_query(F.data == "extension_on_the_block_from_behind_the_head")
async def extension_on_the_block_from_behind_the_head(callback_query: types.CallbackQuery) -> None:
    """Разгибания на блоке из-за головы. Источник информации https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/"""
    try:
        document = FSInputFile('messages/images/triceps_exercises/extension_on_the_block_from_behind_the_head.jpg')
        media = InputMediaPhoto(media=document, caption=extension_on_the_block_from_behind_the_head_text)
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=return_to_triceps_exercises(),
        )
    except Exception as e:
        logger.error(f"Ошибка: {e}")


def register_triceps():
    """Регистрация обработчиков для бота"""
    router.callback_query.register(triceps_exercises)  # Перечень упражнений
    router.callback_query.register(diamond_push_ups)  # Алмазные отжимания
    router.callback_query.register(reverse_push_ups_on_a_bench)  # Обратные отжимания на скамье
    router.callback_query.register(dips)  # Отжимания на брусьях
    router.callback_query.register(french_bench_press_with_barbell)  # Французский жим лёжа со штангой
    router.callback_query.register(dumbbell_overhead_press)  # Жим гантели из-за головы
    router.callback_query.register(bent_over_arm_extension_with_dumbbells)  # Разгибание рук с гантелями в наклоне
    router.callback_query.register(one_arm_extension)  # Разгибание одной руки с опорой на лавку
    router.callback_query.register(block_rope_extension)  # Разгибание рук на блоке с канатной рукоятью
    router.callback_query.register(reverse_grip_extension)  # Разгибание рук на блоке обратным хватом
    router.callback_query.register(extension_on_the_block_from_behind_the_head)  # Разгибания на блоке из-за головы
