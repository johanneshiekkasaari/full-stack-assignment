from typing import List

from app.models.lighthouse_model import LightHouse

class LightHouseRepository:
    def get_lighthouses(self) -> List[LightHouse]:
        # Implementation to get lighthouses from backend and return as a list of Lighthouse objects
        # Example:
        return [
            LightHouse(latitude = 59.84209027426223,longitude = 22.468528252845005, seamark = "seamark1",light= "light1", range = 5),
            LightHouse(latitude = 59.90797985396648, longitude = 22.43235828858468, seamark = "seamark2", light="light2",range = 10),
            LightHouse(latitude = 59.83562876053932, longitude = 22.399135506598554, seamark = "seamark3", light="light3",range =15),
            LightHouse(latitude = 59.841601858423815, longitude = 22.396821382618526, seamark = "seamark4", light="light4", range =20),
        ]
