import sqlite3
from logging import exception

from loguru import logger


def add_users(
    username: str, name: str, height: str, weight: str, training_experience: str
) -> None:
    """
    Добавляет нового пользователя

    Аргументы:
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
                    username TEXT,
                    name TEXT,
                    registered_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    height TEXT,
                    weight TEXT,
                    training_experience TEXT)"""
            )
            cursor.execute(
                """INSERT INTO users (username, name, height, weight, training_experience) VALUES (?, ?, ?, ?, ?)""",
                (username, name, height, weight, training_experience),
            )
            connection.commit()
    except Exception as error:
        logger.exception(error)


def get_user_data(username: str) -> None:
    """
    Получает пользователя из базы

    Аргументы:
    :param username: логин пользователя в телеграмме
    """
    try:
        with sqlite3.connect("sqlite3.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT username, name, height, weight, training_experience
                FROM users
                WHERE username = ?
                """,
                (username,),
            )
            return cursor.fetchone()

    except Exception as error:
        logger.exception(error)


def update_user_data(
    username: str,
    name: str = None,
    height: str = None,
    weight: str = None,
    training_experience: str = None,
) -> None:
    """
    Редактировать пользователя из базы

    Аргументы:
    :param username: логин пользователя в телеграмме
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
            values.append(username)

            cursor = connection.cursor()
            query = f"UPDATE users SET {', '.join(updates)} WHERE username = ?"
            cursor.execute(query, values)

    except Exception as error:
        logger.exception(error)
