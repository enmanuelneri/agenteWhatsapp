# Aquí podrías definir endpoints para procesar o 
# guardar incidencias. Esto es opcional y lo usas 
# según tu diseño.
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Incident(BaseModel):
    description: str
    category: str = None

@router.post("/incidents")
async def create_incident(incident: Incident):
    # Aquí integras la lógica con LangChain / LLM o envías la incidencia a otro servicio
    incident.category = "Clasificado"  # ejemplo simulado
    return incident