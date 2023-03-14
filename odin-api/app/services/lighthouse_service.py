from typing import List

from app.models.lighthouse_model import LightHouse
from app.repositories.lighthouse_repository import LightHouseRepository

class LightHouseService:
    def __init__(self, repository: LightHouseRepository):
        self.repository = repository

    def get_lighthouses(self) -> List[LightHouse]:
        return self.repository.get_lighthouses()
          