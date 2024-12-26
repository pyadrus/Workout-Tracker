import sqlite3
from datetime import datetime
from loguru import logger


async def get_user_data_for_today(user_id):
    """
    Получение данных пользователя за текущий день.

    :param user_id: ID пользователя Telegram.
    :return: Форматированная строка с данными тренировок или сообщение о том, что данных нет.
    """
    try:
        # Подключение к базе данных
        conn = sqlite3.connect("../../gym_data.db")
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
        conn = sqlite3.connect("../../gym_data.db")
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
