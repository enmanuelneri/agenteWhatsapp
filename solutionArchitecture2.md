```mermaid
flowchart LR
    A[Grupo de Telegram] -->|Webhook| B["Servicio REST en .NET Core (IIS)"]
    B --> C[Azure OpenAI - Clasificación]
    B --> D[Base de datos Oracle / .NET Backend]
```