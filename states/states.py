from aiogram.fsm.state import StatesGroup, State


# Определение состояний
class FormeditMainMenu(StatesGroup):
    text_edit_main_menu = State()  # Название упражнения
    repetitions = State()  # Количество повторений
    approaches = State()  # Количество подходов
    weight = State()  # Вес


class MessageStorage(StatesGroup):
    message_to_be_sent = State()  # Состояние хранения сообщения.



class ChangeData(StatesGroup):
    name = State()  # Состояние ввода для изменения имени.
    height = State()  # Состояние ввода для изменения роста.
    weight = State()  # Состояние ввода для изменения веса.
    training_experience = State()  # Состояние ввода для изменения опыта тренировок.


class RegistrationStates(StatesGroup):
    name = State()  # Состояние ввода имени.
    height = State()  # Состояние ввода роста.
    weight = State()  # Состояние ввода веса.
    training_experience = State()  # Состояние ввода опыта тренировок.