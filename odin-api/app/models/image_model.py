from pydantic import BaseModel
from typing import List

class Image(BaseModel):
    filename: str
    path: str
    corner_coords: List[List[float]]
