from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get("/")
async def root():
    return "ODIN-API NOT FOUND"

@app.get("/tms/{z}/{x}/{y}.png")
async def tms(x:int,y:int,z:int):
    return (x,y,z)

@app.get("/sar.png")
async def sar():
    f = open('SAR_image_20420212.png','rb');
    return Response(content=f.read(), media_type="image/png")


@app.get("/mapstylesimple")
async def mapstylesimple():
    return(
        {
            'version': 8,
            'sources': {
                'sar': {
                    'type': 'image',
                    'url': 'http://localhost:8000/sar.png',
                    'coordinates': [
                        [22.2908182629724, 59.91614254645401],
                        [22.578806773313246, 59.947751078236365],
                        [22.638044070378744, 59.809992490984754],
                        [22.351391574531174, 59.77847599974091],
                    ]
                },
                'terrain': {
                    'type': 'raster',
                    'tiles': [
                        'https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg'
                        ],
                    'tileSize': 256,
                    }
                },
            'layers': [
                {
                    'id': 'terrain',
                    'type': 'raster',
                    'source': 'terrain',
                    'minzoom': 0,
                    'maxzoom': 22
                },
                {
                    'id': 'sar',
                    'type': 'raster',
                    'source': 'sar',
                    'paint': {
                        'raster-opacity': 0.5,
                    }
                },
            ]
        }
    )
