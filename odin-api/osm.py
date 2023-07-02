from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import Overpass
from OSMPythonTools.overpass import overpassQueryBuilder


def getOsmPoi(region, selector):
    # Should switch to a better library that supports types, but this is
    # old code from a project done earlier and won't try fixing it for this
    nominatim = Nominatim()
    overpass = Overpass()
    features = []

    area = nominatim.query(region)
    query = overpassQueryBuilder(
        area=area.areaId(), elementType="node", selector=selector, out="body"
    )
    pois = overpass.query(query, timeout=120)

    for poi in pois.nodes():
        features.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [poi.lon(), poi.lat()]},
            }
        )

    return {
        "type": "FeatureCollection",
        "features": features,
    }
