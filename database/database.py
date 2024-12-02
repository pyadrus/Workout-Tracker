import sqlite3
from logging import exception

from loguru import logger


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
