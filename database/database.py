import sqlite3


def get_connection():
    connection = sqlite3.connect("sqlite3.db")
    return connection


def init_db() -> None:
    """
    Создает подключение к базе данных
    """

    conn = get_connection()

    cursor = conn.cursor()
    _ = cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
            word_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            height VARCHAR(255) NOT NULL,
            weight VARCHAR(255) NOT NULL,
            training_experience VARCHAR(255) NOT NULL);"""
    )
    conn.commit()
    conn.close


def add_users(name: str, height: str, weight: str, training_experience: str) -> None:
    """
    Добавляет нового пользователя
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO users (name, height, weight, training_experience) VALUES (?, ?, ?, ?)""",
        (name, height, weight, training_experience),
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
