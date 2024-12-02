import sqlite3
from logging import exception

from loguru import logger

# def get_connection():
#     connection = sqlite3.connect("sqlite3.db")
#     return connection


# def init_db() -> None:
#     """
#     Создает подключение к базе данных
#     """
#
#     conn = get_connection()
#
#     cursor = conn.cursor()
#     _ = cursor.execute(
#         """CREATE TABLE IF NOT EXISTS users (
#             word_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name VARCHAR(255) NOT NULL,
#             height VARCHAR(255) NOT NULL,
#             weight VARCHAR(255) NOT NULL,
#             training_experience VARCHAR(255) NOT NULL);"""
#     )
#     conn.commit()
#     conn.close


def add_users(name: str, height: str, weight: str, training_experience: str) -> None:
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
                """CREATE TABLE IF NOT EXISTS users (name ,height ,weight ,training_experience)"""
            )
            cursor.execute(
                """INSERT INTO users (name, height, weight, training_experience) VALUES (?, ?, ?, ?)""",
                (name, height, weight, training_experience),
            )
            connection.commit()
    except Exception as error:
        logger.exception(error)

# if __name__ == "__main__":
#     init_db()
