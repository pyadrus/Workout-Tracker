from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# # Словарь упражнений на трицепс: ключ (key) - callback_data, значение (value) - текст кнопки
# menu_dict = {
#     "types_of_exercises_for_muscle_groups": "Упражнения на группу мышц",
#     "help_with_work": "Помощь",
#     "CommandStart": "Начать запись тренировок",
#     "training_program": "Программа тренировок",
#     "get_today": "Получить результат тренировки на сегодня",
# }
#
#
# def keyboard_menu():
#     """Клавиатура приветствия. Источник информации: https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/"""
#     triceps_exercises = [
#         [InlineKeyboardButton(text=value, callback_data=key)]
#         for key, value in menu_dict.items()
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=triceps_exercises)


return_to_triceps_exercises_dict = {
    "start_handler": "В начальное меню", }


def keyboard_start_handler():
    """Назад в меню выбора упражнения. Источник информации: https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/"""
    return_to_triceps = [
        [InlineKeyboardButton(text=value, callback_data=key)]
        for key, value in return_to_triceps_exercises_dict.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=return_to_triceps)


if __name__ == '__main__':
    # keyboard_menu()
    keyboard_start_handler()
