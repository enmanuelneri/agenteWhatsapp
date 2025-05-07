```mermaid
flowchart LR
    A[Grupo de Telegram] -->|Webhook| B["Azure Function (HTTP Trigger)"]
    B --> C[Azure OpenAI - Clasificación]
    B --> D[Base de datos Oracle / .NET Backend]

```
