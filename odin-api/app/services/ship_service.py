from app.repositories.ship_repository import ShipRepository

class ShipService:
    def __init__(self, repository: ShipRepository):
        self.repository = repository

    def get_ship(self):
        return self.repository.get_ship()