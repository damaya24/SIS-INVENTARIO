from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Product(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    codigo = Column(String(50), unique=True)
    nombre = Column(String(100))
    categoria = Column(String(100))
    cantidad = Column(Integer)
    precio = Column(Float)