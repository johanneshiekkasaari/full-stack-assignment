from fastapi import APIRouter

from app.services.ship_service import ShipService
from app.repositories.ship_repository import ShipRepository

router = APIRouter()

repo = ShipRepository()
service = ShipService(repo)

@router.get("/ship")
async def get_ship():
    Ship = service.get_ship()
    return Ship