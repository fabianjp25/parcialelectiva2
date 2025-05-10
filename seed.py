from app.database import SessionLocal, engine
from app.models import Usuario, Base

Base.metadata.create_all(bind=engine)

db = SessionLocal()

usuario = Usuario(username="admin", password="1234")  # OJO: sin encriptar por ahora
db.add(usuario)
db.commit()
db.close()

print("Usuario creado")
