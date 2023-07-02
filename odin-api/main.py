from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from image import router as imageRouter
from poi import router as poiRouter

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])
app.include_router(imageRouter)
app.include_router(poiRouter)


@app.get("/")
async def root():
    response = RedirectResponse(url="/docs")
    return response


@app.get("/style")
async def style():
    return {
        "version": 8,
        "sources": {
            "sar": {
                "type": "image",
                "url": "http://localhost:8000/images/SAR_image_20420212.png",
                "coordinates": [
                    [22.2908182629724, 59.91614254645401],
                    [22.578806773313246, 59.947751078236365],
                    [22.638044070378744, 59.809992490984754],
                    [22.351391574531174, 59.77847599974091],
                ],
            },
            "terrain": {
                "type": "raster",
                "tiles": [
                    "https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg"
                ],
                "tileSize": 256,
            },
            "lighthouses": {
                "type": "geojson",
                "data": "http://localhost:8000/poi/lighthouses",
            },
            "ship": {"type": "geojson", "data": "http://localhost:8000/poi/ship"},
        },
        "layers": [
            {
                "id": "terrain",
                "type": "raster",
                "source": "terrain",
                "minzoom": 0,
                "maxzoom": 22,
            },
            {
                "id": "sar",
                "type": "raster",
                "source": "sar",
                "paint": {
                    "raster-opacity": 0.5,
                },
            },
            {
                "id": "ship",
                "type": "circle",
                "source": "ship",
                "paint": {"circle-radius": 10, "circle-color": "#007cbf"},
            },
            {
                "id": "lighthouses",
                "type": "circle",
                "source": "lighthouses",
                "paint": {"circle-radius": 5, "circle-color": "#555556"},
            },
        ],
    }
