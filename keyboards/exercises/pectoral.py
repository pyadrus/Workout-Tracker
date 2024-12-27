from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Словарь упражнений на трицепс: ключ (key) - callback_data, значение (value) - текст кнопки
exercises_for_the_pectoral_muscles_keyboard_dict = {
    "bench_press_horizontally": "Жим штанги лежа горизонтально",  # Готово
    "bent_over_barbell_press": "Жим штанги в наклоне",  # Готово
    "dumbbell_bench_press": "Жим гантелей лежа",  # Готово
    "dumbbell_raises": "Разведение рук с гантелями",  # Готово
    "a_sweater": "Пуловер",  # Готово

    "exercises_for_the_pectoral_muscles_2": "Еще упражнения на Грудные мышцы",
    "start_handler": "В начальное меню",
}


def pectoral_kb():
    """Клавиатура упражнений на трицепс. Источник информации: https://donsport.ru/blog/kompleks-effektivnykh-uprazhneniy-dlya-myshts-grudi/"""
    biceps_exercises = [
        [InlineKeyboardButton(text=value, callback_data=key)]
        for key, value in exercises_for_the_pectoral_muscles_keyboard_dict.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=biceps_exercises)


# Словарь упражнений на трицепс: ключ (key) - callback_data, значение (value) - текст кнопки
exercises_for_the_pectoral_muscles_keyboard_dict_2 = {
    "bringing_hands_together_on_the_lower_crossover_block": "Сведение рук на нижнем блоке кроссовера",  # Готово
    "reduction_of_arms_in_the_butterfly_simulator": "Сведение рук в тренажере бабочка",  # Готово
    "dips": "Отжимания на брусьях",  # Готово
    "hummer": "Хаммер",  # Готово
    "push_ups": "Отжимания",

    "pectoral": "🔙  Назад",
    "start_handler": "В начальное меню",
}


def pectoral_kb2():
    """Клавиатура упражнений на трицепс. Источник информации: https://donsport.ru/blog/kompleks-effektivnykh-uprazhneniy-dlya-myshts-grudi/"""
    biceps_exercises = [
        [InlineKeyboardButton(text=value, callback_data=key)]
        for key, value in exercises_for_the_pectoral_muscles_keyboard_dict_2.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=biceps_exercises)


return_to_biceps_exercises_dict = {
    "pectoral": " 🔙 Назад",
    "start_handler": "В начальное меню", }


def return_pectoral_kb():
    """Назад в меню выбора упражнения. Источник информации: https://neodent82.ru/blog/10-luchshih-uprazhnenij-na-bitseps"""
    return_to_triceps = [
        [InlineKeyboardButton(text=value, callback_data=key)]
        for key, value in return_to_biceps_exercises_dict.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=return_to_triceps)


if __name__ == '__main__':
    pectoral_kb()  # Клавиатура упражнений на Грудные мышцы
    pectoral_kb2()  # Клавиатура упражнений на Грудные мышцы 2
    return_pectoral_kb()  # Назад в меню выбора упражнения Грудные мышцы
