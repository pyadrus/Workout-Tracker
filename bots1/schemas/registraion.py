from sqlalchemy import Column, BigInteger, Integer, String, sql, Float, DateTime
from datetime import datetime


class User:
    __tablename__ = "registration"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    weight = Column(String(250))
    training_experience = Column(String(250))
    created_ad = Column(DateTime, default=datetime.now)
