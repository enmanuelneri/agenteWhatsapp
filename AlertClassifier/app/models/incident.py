from pydantic import BaseModel

class Incident(BaseModel):
    description: str
    category: str = None