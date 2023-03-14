from app.repositories.image_repository import ImageRepository
from app.models.image_model import Image

class ImageService:
    def __init__(self, image_repository: ImageRepository):
        self.image_repository = image_repository

    def get_image(self) -> Image:
        return self.image_repository.get_image()

