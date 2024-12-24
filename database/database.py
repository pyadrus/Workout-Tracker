import sqlite3
from typing import Any

from loguru import logger


def add_users(
    id_user_telegram: str, name: str, height: str, weight: str, training_experience: str
) -> None:
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
        with sqlite3.connect("sqlite3.db") as connection:
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
        with sqlite3.connect("sqlite3.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT id_user_telegram, name, height, weight, training_experience
                FROM authorized_user
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
            query = f"UPDATE authorized_user SET {', '.join(updates)} WHERE id_user_telegram = ?"
            cursor.execute(query, values)

    except Exception as error:
        logger.exception(error)


def add_user_starting_the_bot(
    id_user: str,
    is_bot: str,
    first_name: str,
    last_name: str,
    username: str,
    language_code: str,
    is_premium: str,
    added_to_attachment_menu: str,
    can_join_groups: str,
    can_read_all_group_messages: str,
    supports_inline_queries: str,
    can_connect_to_business: str,
    has_main_web_app: str,
) -> None:
    """
    Добавляет нового не авторизованного пользователя

    Аргументы:
    :param id_user: id пользователя телеграмма
    :param username: имя пользователя телеграмма
    """
    try:
        with sqlite3.connect("sqlite3.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS not_authorized_user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user TEXT UNIQUE,
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
                has_main_web_app)"""
            )
            cursor.execute(
                """INSERT INTO not_authorized_user (
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
                    has_main_web_app) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
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
                ),
            )
            connection.commit()

    except Exception as error:
        logger.exception(error)


def get_user_starting_the_bot() -> list[Any] | None:
    """
    Получение не авторизованных пользователей

    Аргументы:
    :param id_user: id пользователя телеграмма
    """
    try:
        with sqlite3.connect("sqlite3.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT id_user, username FROM not_authorized_user""",
            )
            return cursor.fetchall()
    except Exception as error:
        logger.exception(error)
