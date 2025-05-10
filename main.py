from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import equipo

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes cambiar esto por el dominio específico de tu frontend si quieres restringir acceso
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar base de datos
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(equipo.router)

# Configurar plantillas HTML (login, etc.)
templates = Jinja2Templates(directory="app/templates")

# Ruta GET para mostrar formulario login
@app.get("/login", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Ruta POST para procesar login
@app.post("/login")
async def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
    # Validación básica (reemplazar luego por validación con base de datos)
    if username == "admin" and password == "1234":
        return RedirectResponse(url="/", status_code=302)
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Credenciales inválidas"})
