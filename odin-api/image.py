import os
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import Response

router = APIRouter(
    prefix="/images",
)

images = {
    "SAR_image_20420212.png": {
        "name": "SAR_image_20420212",
        "coordinates": [
            [22.2908182629724, 59.91614254645401],
            [22.578806773313246, 59.947751078236365],
            [22.638044070378744, 59.809992490984754],
            [22.351391574531174, 59.77847599974091],
        ],
    }
}


@router.get("/")
async def sar(request: Request):
    url_prefix = str(request.url)
    images_with_path = []
    for image in images:
        images_with_path.append({"url": url_prefix + image, **images[image]})
    return images_with_path


@router.get("/{sar}")
async def get_file(sar: str):
    if sar not in images:
        return HTTPException(status_code=404)
    f = open(os.path.join("images", sar), "rb")
    return Response(content=f.read(), media_type="image/png")
