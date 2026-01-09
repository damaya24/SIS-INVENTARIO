from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    rol = Column(String(50))