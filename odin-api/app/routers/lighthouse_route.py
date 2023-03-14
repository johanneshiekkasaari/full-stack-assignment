from fastapi import APIRouter

from app.services.lighthouse_service import LightHouseService
from app.repositories.lighthouse_repository import LightHouseRepository

router = APIRouter()

repo = LightHouseRepository()
service = LightHouseService(repo)

@router.get("/lighthouses")
async def get_lighthouses():
    lighthouses = service.get_lighthouses()
    return [l.__dict__ for l in lighthouses]