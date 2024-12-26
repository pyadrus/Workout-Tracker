from aiogram.fsm.state import StatesGroup, State


# Определение состояний
class FormeditMainMenu(StatesGroup):
    text_edit_main_menu = State()  # Название упражнения
    repetitions = State()  # Количество повторений
    approaches = State()  # Количество подходов
    weight = State()  # Вес
