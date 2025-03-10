import sqlite3
from datetime import datetime
from typing import Any

from loguru import logger

path_database = 'database/database.db'


def check_for_bot_launch(user_id: int) -> bool:
    """
    Проверяет, есть ли пользователь с заданным `user_id` в базе данных.

    :param user_id: ID пользователя Telegram.
    :return: True, если пользователь найден, иначе False.
    """
    try:
        with sqlite3.connect(path_database) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS launch_bot (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user,
                is_bot,
                first_name,
                last_name,
                username,
                language_code,
                is_premium,
                added_to_attachment_menu,
                can_join_groups,
                can_read_all_group_messages,
                supports_inline_queries,
                can_connect_to_business,
                has_main_web_app,
                user_date)""")
            cursor.execute("SELECT 1 FROM launch_bot WHERE id_user = ?", (user_id,))
            return cursor.fetchone() is not None
    except Exception as error:
        logger.exception(f"Ошибка при проверке пользователя в базе данных: {error}")
        return False


def add_user_starting_the_bot(id_user, is_bot, first_name, last_name, username, language_code, is_premium,
                              added_to_attachment_menu, can_join_groups, can_read_all_group_messages,
                              supports_inline_queries, can_connect_to_business, has_main_web_app, user_date) -> None:
    """
    Добавляет нового не авторизованного пользователя

    Аргументы:
    :param user_date: дата добавления пользователя
    :param language_code: язык пользователя
    :param is_premium:
    :param can_read_all_group_messages:
    :param can_connect_to_business:
    :param has_main_web_app:
    :param supports_inline_queries:
    :param can_join_groups:
    :param added_to_attachment_menu:
    :param last_name:
    :param first_name:
    :param is_bot:
    :param id_user: id пользователя телеграмма
    :param username: имя пользователя телеграмма
    """

    logger.info(f"User Info: {id_user}, {username}, {first_name}, {last_name}, {user_date}")

    try:
        with sqlite3.connect(path_database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS launch_bot (id INTEGER PRIMARY KEY AUTOINCREMENT, id_user, is_bot, first_name, last_name, username, language_code, is_premium, added_to_attachment_menu, can_join_groups, can_read_all_group_messages, supports_inline_queries, can_connect_to_business, has_main_web_app, user_date)""")
            cursor.execute(
                """INSERT INTO launch_bot (id_user, is_bot, first_name, last_name, username, language_code, is_premium, added_to_attachment_menu,   can_join_groups, can_read_all_group_messages, supports_inline_queries, can_connect_to_business, has_main_web_app, user_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (id_user, is_bot, first_name, last_name, username, language_code, is_premium, added_to_attachment_menu,
                 can_join_groups, can_read_all_group_messages, supports_inline_queries, can_connect_to_business,
                 has_main_web_app, user_date))
            connection.commit()

    except Exception as error:
        logger.exception(error)


async def get_user_data_for_today(user_id):
    """
    Получение данных пользователя за текущий день.

    :param user_id: ID пользователя Telegram.
    :return: Форматированная строка с данными тренировок или сообщение о том, что данных нет.
    """
    try:
        # Подключение к базе данных
        conn = sqlite3.connect(path_database)
        cursor = conn.cursor()

        # Получаем текущую дату как имя таблицы
        table_name = f"workout_{datetime.now().strftime('%Y_%m_%d')}"

        # Проверяем, существует ли таблица
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        if not cursor.fetchone():
            return "За сегодня данных о тренировках нет."

        # Запрос данных для конкретного пользователя
        cursor.execute(f"""
        SELECT exercise_name, repetitions, approaches, weight, total_weight, created_at
        FROM [{table_name}]
        WHERE user_id = ?
        """, (user_id,))

        rows = cursor.fetchall()
        if not rows:
            return "За сегодня данных о ваших тренировках нет."

        # Форматирование результата
        result = ["Ваши тренировки за сегодня:"]
        for i, (exercise_name, repetitions, approaches, weight, total_weight, created_at) in enumerate(rows, 1):
            result.append(
                f"{i}. Упражнение: {exercise_name}\n"
                f"Повторений: {repetitions}, \n"
                f"Подходов: {approaches}\n"
                f"Вес за подход: {weight} кг, \n"
                f"Общий вес: {total_weight} кг\n"
                f"Время записи: {created_at}"
            )

        conn.close()
        return "\n\n".join(result)

    except sqlite3.Error as e:
        logger.error(f"Ошибка при работе с базой данных: {e}")
        return "Произошла ошибка при получении данных. Пожалуйста, попробуйте позже."


def save_data_to_db(user_id, exercise_name, repetitions, approaches, weight, total_weight):
    """
    Функция для записи данных в базу данных SQLite.

    :param user_id: ID аккаунта пользователя.
    :param exercise_name: Название упражнения.
    :param repetitions: Количество повторений.
    :param approaches: Количество подходов.
    :param weight: Вес за подход.
    :param total_weight: Общий поднятый вес.
    """
    try:
        # Подключаемся к базе данных (создаётся автоматически, если её нет)
        conn = sqlite3.connect(path_database)
        cursor = conn.cursor()

        # Получаем текущую дату как имя таблицы
        table_name = f"workout_{datetime.now().strftime('%Y_%m_%d')}"

        # Создаём таблицу, если она ещё не существует
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            exercise_name TEXT NOT NULL,
            repetitions INTEGER NOT NULL,
            approaches INTEGER NOT NULL,
            weight INTEGER NOT NULL,
            total_weight INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Вставляем данные в таблицу
        cursor.execute(f"""
        INSERT INTO {table_name} (
            user_id, exercise_name, repetitions, approaches, weight, total_weight
        ) VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, exercise_name, repetitions, approaches, weight, total_weight))

        # Сохраняем изменения
        conn.commit()
        conn.close()

        logger.info(f"Данные успешно записаны в таблицу {table_name} для пользователя {user_id}.")
    except sqlite3.Error as e:
        logger.error(f"Ошибка при работе с базой данных: {e}")


def is_user_authorized(user_id: int) -> bool:
    """
    Проверяет, зарегистрирован ли пользователь в базе данных.

    :param user_id: ID пользователя Telegram.
    :return: True, если пользователь зарегистрирован, иначе False.
    """
    try:
        with sqlite3.connect(path_database) as connection:
            cursor = connection.cursor()

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS authorized_user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_user_telegram TEXT,
                    name TEXT,
                    height TEXT,
                    weight TEXT,
                    training_experience TEXT,
                    registered_at TEXT DEFAULT CURRENT_TIMESTAMP)"""
            )

            cursor.execute("SELECT id_user_telegram FROM authorized_user WHERE id_user_telegram = ?", (user_id,))
            result = cursor.fetchone()
            return result is not None
    except Exception as error:
        logger.exception(error)
        return False


def add_users(id_user_telegram: int, name: str, height: str, weight: str, training_experience: str) -> None:
    """
    Добавляет нового авторизованного пользователя

    Аргументы:
    :param id_user_telegram: id пользователя телеграмма
    :param name: имя пользователя
    :param height: рост пользователя
    :param weight: вес пользователя
    :param training_experience: опыт тренировок пользователя
    """
    try:
        with sqlite3.connect(path_database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS authorized_user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_user_telegram TEXT,
                    name TEXT,
                    height TEXT,
                    weight TEXT,
                    training_experience TEXT,
                    registered_at TEXT DEFAULT CURRENT_TIMESTAMP)"""
            )
            cursor.execute(
                """INSERT INTO authorized_user (id_user_telegram, name, height, weight, training_experience) VALUES (?, ?, ?, ?, ?)""",
                (id_user_telegram, name, height, weight, training_experience),
            )
            connection.commit()
    except Exception as error:
        logger.exception(error)


def get_user_data(id_user_telegram: str) -> None:
    """
    Получает пользователя из базы

    Аргументы:
    :param id_user_telegram: логин пользователя в телеграмме
    """
    try:
        with sqlite3.connect(path_database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT id_user_telegram, name, height, weight, training_experience FROM authorized_user WHERE id_user_telegram = ?""",
                (id_user_telegram,), )
            return cursor.fetchone()

    except Exception as error:
        logger.exception(error)


def update_user_data(id_user_telegram: str, name: str = None, height: str = None, weight: str = None,
                     training_experience: str = None) -> None:
    """
    Редактировать пользователя из базы

    Аргументы:
    :param id_user_telegram: id пользователя в телеграмме
    :param name: имя пользователя
    :param height: рост пользователя
    :param weight: вес пользователя
    :param training_experience: опыт тренировок пользователя
    """
    try:
        with sqlite3.connect(path_database) as connection:
            # Создаем словарь для обновляемых значений
            updates = []
            values = []
            if name:
                updates.append("name = ?")
                values.append(name)
            if height:
                updates.append("height = ?")
                values.append(height)
            if weight:
                updates.append("weight = ?")
                values.append(weight)
            if training_experience:
                updates.append("training_experience = ?")
                values.append(training_experience)

            # Добавляем ID в список значений
            values.append(id_user_telegram)

            cursor = connection.cursor()
            query = f"UPDATE authorized_user SET {', '.join(updates)} WHERE id_user_telegram = ?"
            cursor.execute(query, values)

    except Exception as error:
        logger.exception(error)


def get_user_starting_the_bot() -> list[Any] | None:
    """
    Получение не авторизованных пользователей
    """
    try:
        with sqlite3.connect(path_database) as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT id_user, username FROM not_authorized_user""")
            return cursor.fetchall()
    except Exception as error:
        logger.exception(error)
