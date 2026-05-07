from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, nullable=True)
    cantidad = Column(Integer, default=0)
    precio_unitario = Column(Float)
