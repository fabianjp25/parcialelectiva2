from pydantic import BaseModel

class EquipoBase(BaseModel):
    marca: str
    modelo: str
    serial: str
    estado: str

class EquipoCreate(EquipoBase):
    pass

class EquipoOut(EquipoBase):
    id: int

    class Config:
        orm_mode = True
