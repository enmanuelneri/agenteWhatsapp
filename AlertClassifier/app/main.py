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

'''
- Explicación de los valores permitidos:
filesystem: Guarda los registros en el sistema de archivos del App Service. Puedes verlos en tiempo real con Log Stream o descargarlos desde el portal de Azure.
azureblobstorage: Guarda los registros en Azure Blob Storage (requiere configuración adicional).
off: Desactiva los registros.
Comando para habilitar los logs y ver en la shell
az webapp log config --name alertClassifier-webhook-service --resource-group alert_classifier --application-logging filesystem
- Habilitar el streaming de logs: Una vez configurados los registros, puedes verlos en tiempo real con:
az webapp log tail --name alertClassifier-webhook-service --resource-group alert_classifier

Telegram: 7612296835:AAEUxtmWF339MFPIl7l6DgmmAHQ5k9-7e7E

# Llamada a curl
curl -X POST "https://api.telegram.org/bot7612296835:AAEUxtmWF339MFPIl7l6DgmmAHQ5k9-7e7E/setWebhook?url=https://alertclassifier-webhook-service-eyhja6f8c8atffff.brazilsouth-01.azurewebsites.net/telegram/webhook"

# Azure Open AI
2B4gI3oPGOxKwDCtgDgEzGln1WaX4UnKOUt9np3vIJyblPlWgd5KJQQJ99BEACYeBjFXJ3w3AAABACOGM5UF
EndPoint
https://aopenaidpw.openai.azure.com/


# Deploy
tar -xvzf output.tar.gz
'''