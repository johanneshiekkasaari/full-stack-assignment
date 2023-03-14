from app.models.ship_model import Ship

class ShipRepository:
    def get_ship(self):
        return Ship(latitude=59.89134,  longitude = 22.30606)