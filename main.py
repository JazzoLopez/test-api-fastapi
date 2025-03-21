from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import protected_route as user
from routes.material import protected_route as material
from routes.loans import protected_route as loan
from routes.auth import auth

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las URLs (cámbialo si es necesario)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, OPTIONS, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

# Rutas
app.include_router(auth, prefix="/api/auth")
app.include_router(user, prefix="/api")
app.include_router(material, prefix="/api")
app.include_router(loan, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
