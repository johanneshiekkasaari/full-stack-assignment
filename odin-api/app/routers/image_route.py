from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
from tempfile import NamedTemporaryFile
import numpy as np

from app.services.image_service import ImageService
from app.repositories.image_repository import ImageRepository

router = APIRouter()

image_repository = ImageRepository()
image_service = ImageService(image_repository)

@router.get("/images/sar")
async def get_sar():
    image = image_service.get_image()
    if not image:
        return {"error": "Image not found"}
    return FileResponse(image.path)

@router.get("/images/get")
async def get_image(request:Request):
    image = image_service.get_image()
    if not image:
        return {"error": "Image not found"}
    return {
        "url": str(request.base_url) + "images/sar",
        "corner_coords": image.corner_coords
    }