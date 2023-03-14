from pydantic import BaseModel

class Ship(BaseModel):
    latitude: float
    longitude: float
