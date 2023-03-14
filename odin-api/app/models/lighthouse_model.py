from pydantic import BaseModel

class LightHouse(BaseModel):
    latitude: float
    longitude: float
    seamark: str
    light: str
    range: int
