import databases
import sqlalchemy
from datetime import datetime
from pydantic import BaseModel

class Coupon(Base):
    __tablename__ = 'coupon'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    time = Column(DateTime, default=datetime.now())
    window = Column(String, nullable=False)
    active = Column(Boolean, default=True)

# Создать базу данных в памяти
engine = create_engine('sqlite:///:memory:', echo=True)

# Создать таблицы на основе моделей
Base.metadata.create_all(engine)