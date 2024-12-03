def text_hello_welcome() -> str:
    """
    Возвращает приветственный текст с описанием проекта.

    :return: Строка с приветствием и кратким описанием проекта.
    """
    text = (
        "\n\n💪 Хочу познакомить тебя с нашим проектом!\n\n"
        "'🏋️ StrongTrack_Bot' — это веб-приложение для учета тренировок. "
        "Пользователь может выбрать день недели, указать количество подходов, вес и количество повторений, "
        "после чего приложение рассчитает общий поднятый вес за тренировку."
    )
    return text


def text_description() -> str:
    """
    Возвращает описание функционала проекта.

    :return: Строка с форматированным описанием функций проекта.
    """
    text = (
        "<b>⚙️ Функционал проекта:</b>\n\n"
        "    • <b>📅 Выбор дня недели:</b> Пользователь выбирает день, для которого будет добавлена тренировка.\n"
        "    • <b>📝 Ввод данных о тренировке:</b> Пользователь вводит количество подходов, вес и количество повторений для каждого подхода.\n"
        "    • <b>📊 Расчет общего веса:</b> Приложение рассчитывает суммарный поднятый вес за тренировку.\n"
        "    • <b>📈 Отображение результата:</b> Итоговый результат отображается в удобном формате."
    )
    return text


def text_authorized_user_greeting() -> str:
    """
    Возвращает приветственный текст для авторизованного пользователя.

    :return: Строка с приветствием авторизованного пользователя.
    """
    text = (
        "\n\n'🏋️ StrongTrack_Bot' — это веб-приложение для учета тренировок. "
        "Пользователь может выбрать день недели, указать количество подходов, вес и количество повторений, "
        "после чего приложение рассчитает общий поднятый вес за тренировку."
    )
    return text


if __name__ == "__main__":
    text_hello_welcome()
    text_description()
    text_authorized_user_greeting()
