from fastapi import FastAPI
from app.routers import incidents, whatsapp, telegram

app = FastAPI(title="Integración API MDA")

app.include_router(incidents.router)
app.include_router(whatsapp.router)
app.include_router(telegram.router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la Integración API de Incidentes"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Para probar que está entrando al servicio entras al navegador a la
# dirección http://localhost:8000/docs y verás la documentación de la API.

