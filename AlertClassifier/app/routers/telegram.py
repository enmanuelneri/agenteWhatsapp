# De forma similar, este router maneja los mensajes 
# de Telegram (usando webhook).
from fastapi import APIRouter, Request, HTTPException
import logging
logging.basicConfig(level=logging.INFO)
import openai

# Configura tu clave de API y endpoint de Azure OpenAI
openai.api_type = "azure"

openai.api_base = "https://aopenaidpw.openai.azure.com/"
openai.api_version = "2025-05-05-preview"  # Ajusta según la versión de tu recurso


router = APIRouter(prefix="/telegram", tags=["Telegram"])

def classify_message(text: str) -> str:
    try:
        # Llama al modelo de Azure OpenAI
        response = openai.ChatCompletion.acreate(  # Cambiado a "acreate" para la nueva API
            model="gpt-3.5-turbo",  # Cambia "engine" por "model"
            messages=[
                {"role": "system", "content": """
Eres un asistente que clasifica incidencias en categorías específicas. Usa las siguientes categorías como base para clasificar los mensajes:

- Dport Alta/Creación de usuario:
  Ejemplo: Equipo TI, buenas tardes. Por favor brindar acceso y roles al "modulo listado de presupuestos" Dport para nuestro colaborador (ingreso reciente) quien realizara labores de PTI Y reparación de contenedor reefers sede Gambetta 01.

- Intranet - Alta/Creación de usuario - Logistics:
  Ejemplo: Buenas tardes, Estimados. Solicito que me puedan brindar los accesos solicitados de INTRANET, en adjunto encontraran el word con los detalles y el correo de aprobación.
  Nombre: Luis Fernando Perez Echavarria
  Usuario: lpereze
  Correo: luis.pereze@dpworld.com

- VPN - Modificación de permisos:
  Ejemplo: Por motivos de las pruebas del upgrade a 19c dar acceso: https://uatn4apps.dpwc.local:20443/DpwcSecurityWebService2/service/DpwcSa ACCESO_APLICACIONES_DPW , ACCESO_FINANZAS.

Si el mensaje no está relacionado con un incidente, responde con "No es un incidente".
"""},
                {"role": "user", "content": f"Clasifica la siguiente incidencia: {text}"}
            ],
            max_tokens=50,
            temperature=0.5
        )

        # Extrae la respuesta del modelo
        category = response["choices"][0]["message"]["content"].strip()

        # Si la categoría está vacía o no es válida, asigna "Otros MDA"
        if not category or category.lower() in ["no clasificado", ""]:
            category = f"Otros MDA - Posible clasificación en base a su descripción: {text[:50]}..."

        return category

    except Exception as e:
        logging.error(f"Error al clasificar el mensaje con Azure OpenAI: {e}")
        return "Otros MDA - Error al clasificar"
         
@router.post("/webhook")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()
        logging.info(f"Mensaje recibido desde Telegram: {data}")

        # Extrae el texto del mensaje
        message_text = data.get("message", {}).get("text", "")
        if not message_text:
            raise ValueError("No se encontró texto en el mensaje.")

        # Clasificar el mensaje
        category = classify_message(message_text)

        # Registrar el mensaje y la categoría en los logs
        logging.info(f"Mensaje: {message_text} | Categoría: {category}")

        return {"status": "Mensaje procesado", "category": category}
    except Exception as e:
        logging.error(f"Error procesando el mensaje: {e}")
        raise HTTPException(status_code=400, detail=str(e))