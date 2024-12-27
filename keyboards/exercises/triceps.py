from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Словарь упражнений на трицепс: ключ (key) - callback_data, значение (value) - текст кнопки
triceps_exercises_dict = {
    "diamond_push_ups": "Алмазные отжимания",
    "reverse_push_ups_on_a_bench": "Обратные отжимания на скамье",
    "dips": "Отжимания на брусьях",
    "french_bench_press_with_barbell": "Французский жим лёжа со штангой",
    "dumbbell_overhead_press": "Жим гантели из-за головы",
    "biceps_exercises_2": "Еще упражнения на трицепс",
    "start_handler": "В начальное меню",
}


def keyboard_triceps_exercises():
    """Клавиатура упражнений на трицепс. Источник информации: https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/"""
    triceps_exercises = [
        [InlineKeyboardButton(text=value, callback_data=key)]
        for key, value in triceps_exercises_dict.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=triceps_exercises)


# Словарь упражнений на трицепс: ключ (key) - callback_data, значение (value) - текст кнопки
triceps_exercises_dict_2 = {
    "bent_over_arm_extension_with_dumbbells": "Разгибание рук с гантелями в наклоне",
    "extension_of_one_arm_with_support_on_the_bench": "Разгибание одной руки с опорой на лавку",
    "extension_of_arms_on_a_block_with_a_rope_handle": "Разгибание рук на блоке с канатной рукоятью",
    "extension_of_arms_on_a_block_with_a_reverse_grip": "Разгибание рук на блоке обратным хватом",
    "extension_on_the_block_from_behind_the_head": "Разгибания на блоке из-за головы",
    "triceps": "🔙  Назад",
    "start_handler": "В начальное меню",
}


def keyboard_triceps_exercises_2():
    """Клавиатура упражнений на трицепс. Источник информации: https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/"""
    triceps_exercises = [
        [InlineKeyboardButton(text=value, callback_data=key)]
        for key, value in triceps_exercises_dict_2.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=triceps_exercises)


return_to_triceps_exercises_dict = {
    "triceps": "🔙  Назад",
    "start_handler": "В начальное меню", }


def return_to_triceps_exercises():
    """Назад в меню выбора упражнения. Источник информации: https://lifehacker.ru/luchshie-uprazhneniya-na-triceps/"""
    return_to_triceps = [
        [InlineKeyboardButton(text=value, callback_data=key)]
        for key, value in return_to_triceps_exercises_dict.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=return_to_triceps)


if __name__ == '__main__':
    keyboard_triceps_exercises()  # Клавиатура упражнений на трицепс
    keyboard_triceps_exercises_2()  # Клавиатура упражнений на трицепс 2
    return_to_triceps_exercises()  # Назад в меню выбора упражнения
