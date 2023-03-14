import os
from typing import List

from app.models.image_model import Image

class ImageRepository:

    def get_image(self) -> Image:
        current_file = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(current_file, '..')
        image_path = os.path.join(
            image_path, 'images/SAR_image_20420212.png')
        if not os.path.exists(image_path):
            return None
        return Image(
            filename="SAR image",
            path=image_path,
            corner_coords=[
                [22.2908182629724, 59.91614254645401],
                [22.578806773313246, 59.947751078236365],
                [22.638044070378744, 59.809992490984754],
                [22.351391574531174, 59.77847599974091],
            ])
