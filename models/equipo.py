from sqlalchemy import Column, Integer, String
from app.database import Base

class Equipo(Base):
    __tablename__ = "equipos"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    serial = Column(String, unique=True, nullable=False)
    estado = Column(String, nullable=False)
