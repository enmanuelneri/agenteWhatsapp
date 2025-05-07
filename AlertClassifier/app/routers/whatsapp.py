# Este router se encargará de recibir los mensajes 
# enviados desde WhatsApp vía webhook. La estructura
#  y datos dependerán de la API de WhatsApp que 
# utilices (por ejemplo, WhatsApp Business API).
from fastapi import APIRouter, Request, HTTPException
import logging

router = APIRouter(prefix="/whatsapp", tags=["WhatsApp"])

@router.post("/webhook")
async def whatsapp_webhook(request: Request):
    try:
        data = await request.json()
        logging.info(f"Mensaje recibido desde WhatsApp: {data}")
        # Aquí extraes la información de data y la envías al endpoint de incidencias o realizas procesamiento
        return {"status": "Mensaje recibido"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))