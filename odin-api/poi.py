from fastapi import APIRouter
from osm import getOsmPoi

router = APIRouter(
    prefix="/poi",
)


@router.get("/ship")
async def ship():
    return {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [22.30606, 59.89134]},
        "properties": {
            "title": "Ship",
        },
    }


@router.get("/lighthouses")
async def lighthouses():
    return getOsmPoi("Finland", '"seamark:light:range"')
