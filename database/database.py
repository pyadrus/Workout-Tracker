import sqlite3

from loguru import logger


def add_users(
    id_user_telegram: str, name: str, height: str, weight: str, training_experience: str
) -> None:
    """
    Добавляет нового пользователя

    Аргументы:
    :id_user_telegram: id пользователя телеграмма
    :param name: имя пользователя
    :param height: рост пользователя
    :param weight: вес пользователя
    :param training_experience: опыт тренировок пользователя
    """
    try:
        with sqlite3.connect("sqlite3.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_user_telegram TEXT,
                    name TEXT,
                    height TEXT,
                    weight TEXT,
                    training_experience TEXT,
                    registered_at TEXT DEFAULT CURRENT_TIMESTAMP)"""
            )
            cursor.execute(
                """INSERT INTO users (id_user_telegram, name, height, weight, training_experience) VALUES (?, ?, ?, ?, ?)""",
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
        with sqlite3.connect("sqlite3.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT id_user_telegram, name, height, weight, training_experience
                FROM users
                WHERE id_user_telegram = ?
                """,
                (id_user_telegram,),
            )
            return cursor.fetchone()

    except Exception as error:
        logger.exception(error)


def update_user_data(
    id_user_telegram: str,
    name: str = None,
    height: str = None,
    weight: str = None,
    training_experience: str = None,
) -> None:
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
        with sqlite3.connect("sqlite3.db") as connection:
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
            query = f"UPDATE users SET {', '.join(updates)} WHERE id_user_telegram = ?"
            cursor.execute(query, values)

    except Exception as error:
        logger.exception(error)
