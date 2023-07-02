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


# TODO probably get rid of this entirely and just define it in frontend
@app.get("/style")
async def style():
    return {
        "version": 8,
        "sources": {
            "terrain": {
                "type": "raster",
                "tiles": [
                    "https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg"
                ],
                "tileSize": 256,
            },
        },
        "layers": [
            {
                "id": "terrain",
                "type": "raster",
                "source": "terrain",
                "minzoom": 0,
                "maxzoom": 22,
            },
        ],
    }
