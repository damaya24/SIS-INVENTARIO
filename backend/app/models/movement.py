from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Movement(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True)
    tipo = Column(String(20))
    cantidad = Column(Integer)
    producto_id = Column(Integer, ForeignKey("products.id"))
    usuario_id = Column(Integer, ForeignKey("users.id"))
