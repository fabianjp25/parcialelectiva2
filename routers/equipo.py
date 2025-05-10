from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.equipo import EquipoCreate, EquipoOut
from app.crud import equipo as crud

router = APIRouter(prefix="/equipos", tags=["equipos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EquipoOut)
def crear_equipo(equipo: EquipoCreate, db: Session = Depends(get_db)):
    return crud.crear_equipo(db, equipo)

@router.get("/", response_model=list[EquipoOut])
def listar_equipos(db: Session = Depends(get_db)):
    return crud.obtener_equipos(db)

@router.get("/{equipo_id}", response_model=EquipoOut)
def obtener_equipo(equipo_id: int, db: Session = Depends(get_db)):
    equipo = crud.obtener_equipo(db, equipo_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return equipo

@router.put("/{equipo_id}", response_model=EquipoOut)
def actualizar_equipo(equipo_id: int, equipo_data: EquipoCreate, db: Session = Depends(get_db)):
    return crud.actualizar_equipo(db, equipo_id, equipo_data)

@router.delete("/{equipo_id}")
def eliminar_equipo(equipo_id: int, db: Session = Depends(get_db)):
    if crud.eliminar_equipo(db, equipo_id):
        return {"ok": True}
    raise HTTPException(status_code=404, detail="Equipo no encontrado")
