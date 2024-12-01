from datetime import datetime

from sqlalchemy import Column, BigInteger, String, DateTime


class User:
    """
    Модель пользователя для таблицы регистрации.

    Атрибуты:
    - id: Уникальный идентификатор пользователя.
    - name: Имя пользователя.
    - height: Рост пользователя.
    - weight: Вес пользователя.
    - training_experience: Опыт тренировок пользователя.
    - created_at: Дата и время создания записи.
    """
    __tablename__ = "registration"
    id = Column(BigInteger, primary_key=True)  # Уникальный идентификатор.
    name = Column(String(250))  # Имя пользователя.
    height = Column(String(250))  # Рост пользователя.
    weight = Column(String(250))  # Вес пользователя.
    training_experience = Column(String(250))  # Опыт тренировок.
    created_ad = Column(DateTime, default=datetime.now)  # Дата создания записи.
