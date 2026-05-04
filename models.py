from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    nickname = Column(String)
    level = Column(Integer, default=1)
    hp = Column(Integer, default=1000)
    max_hp = Column(Integer, default=1000)
    energy = Column(Integer, default=100)
    strength = Column(Integer, default=10)
    money = Column(BigInteger, default=1000)
