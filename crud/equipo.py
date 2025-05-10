from sqlalchemy.orm import Session
from app.models.equipo import Equipo
from app.schemas.equipo import EquipoCreate

def crear_equipo(db: Session, equipo: EquipoCreate):
    db_equipo = Equipo(**equipo.dict())
    db.add(db_equipo)
    db.commit()
    db.refresh(db_equipo)
    return db_equipo

def obtener_equipos(db: Session):
    return db.query(Equipo).all()

def obtener_equipo(db: Session, equipo_id: int):
    return db.query(Equipo).filter(Equipo.id == equipo_id).first()

def actualizar_equipo(db: Session, equipo_id: int, datos: EquipoCreate):
    equipo = db.query(Equipo).filter(Equipo.id == equipo_id).first()
    if equipo:
        for k, v in datos.dict().items():
            setattr(equipo, k, v)
        db.commit()
        db.refresh(equipo)
    return equipo

def eliminar_equipo(db: Session, equipo_id: int):
    equipo = db.query(Equipo).filter(Equipo.id == equipo_id).first()
    if equipo:
        db.delete(equipo)
        db.commit()
    return equipo
