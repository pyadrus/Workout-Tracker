from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Словарь упражнений на трицепс: ключ (key) - callback_data, значение (value) - текст кнопки
biceps_exercises_dict = {
    "curls_with_a_barbell_or_EZ_bar": "Сгибание рук со штангой или EZ-штангой",
    "bend_the_arms_on_the_lower_block": "Сгибание рук на нижнем блоке",
    "dumbbell_curl": "Сгибание рук с гантелями",
    "reverse_grip_pull_ups": "Подтягивания обратным хватом",
    "bent_over_barbell_row_with_reverse_grip": "Тяга штанги в наклоне обратным хватом",
    "biceps_exercises_2": "Еще упражнения на бицепс",
    "start_handler": "В начальное меню",
}


def keyboard_biceps_exercises():
    """Клавиатура упражнений на трицепс. Источник информации: https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    biceps_exercises = [
        [InlineKeyboardButton(text=value, callback_data=key)]
        for key, value in biceps_exercises_dict.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=biceps_exercises)


# Словарь упражнений на трицепс: ключ (key) - callback_data, значение (value) - текст кнопки
biceps_exercises_dict_2 = {
    "hammer_grip_curl": "Сгибание рук хватом «молот»",
    "incline_dumbbell_curl": "Сгибание рук с гантелями на наклонной скамье",
    "concentrated_arm_curls": "Концентрированные сгибания рук",
    "scott_bench_curl": "Сгибание рук со штангой на скамье Скотта",
    "arm_bending_with_elbow_abduction": "Сгибание рук с отведением локтей",
    "biceps_exercises": "Назад",
    "start_handler": "В начальное меню",
}


def keyboard_biceps_exercises_2():
    """Клавиатура упражнений на трицепс. Источник информации: https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    biceps_exercises = [
        [InlineKeyboardButton(text=value, callback_data=key)]
        for key, value in biceps_exercises_dict_2.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=biceps_exercises)


return_to_biceps_exercises_dict = {
    "biceps_exercises": "Назад",
    "start_handler": "В начальное меню", }


def return_to_biceps_exercises():
    """Назад в меню выбора упражнения. Источник информации: https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    return_to_triceps = [
        [InlineKeyboardButton(text=value, callback_data=key)]
        for key, value in return_to_biceps_exercises_dict.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=return_to_triceps)


if __name__ == '__main__':
    keyboard_biceps_exercises()  # Клавиатура упражнений на бицепс
    keyboard_biceps_exercises_2()  # Клавиатура упражнений на бицепс 2
    return_to_biceps_exercises()  # Назад в меню выбора упражнения
