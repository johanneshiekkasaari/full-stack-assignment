import Map, { Source, Layer } from "react-map-gl";
import type { CircleLayer, RasterLayer } from "react-map-gl";
import maplibregl from "maplibre-gl";
import { useState, useEffect } from "react";

import "maplibre-gl/dist/maplibre-gl.css";

type OdinImage = {
  url: string;
  name: string;
  coordinates: number[][];
};

const OdinMap = ({ apiUrl }: { apiUrl: string }) => {
  const [images, setImages] = useState<OdinImage[] | undefined>(undefined);

  useEffect(() => {
    fetch(`${apiUrl}/images`).then((res) => {
      res.json().then((resJson) => {
        // TODO validate with zod
        setImages(resJson);
      });
    });
  }, [apiUrl]);

  const lighthouseLayer: CircleLayer = {
    id: "lighthouses",
    type: "circle",
    paint: {
      "circle-radius": 5,
      "circle-color": "#555555",
    },
  };

  const shipLayer: CircleLayer = {
    id: "ship",
    type: "circle",
    paint: {
      "circle-radius": 10,
      "circle-color": "#007cbf",
    },
  };

  const imageLayer: Omit<RasterLayer, "id"> = {
    type: "raster",
    paint: {
      "raster-opacity": 0.5,
    },
  };

  return (
    <Map
      mapLib={maplibregl}
      initialViewState={{
        longitude: 22.4673,
        latitude: 59.8613,
        zoom: 10,
      }}
      style={{ width: 1024, height: 600 }}
      mapStyle={`${apiUrl}/style`}
    >
      <Source id="ship" type="geojson" data={`${apiUrl}/poi/ship`}>
        <Layer {...shipLayer} />
      </Source>
      <Source
        id="lighthouses"
        type="geojson"
        data={`${apiUrl}/poi/lighthouses`}
      >
        <Layer {...lighthouseLayer} />
      </Source>
      {images !== undefined &&
        images.map((image) => (
          <Source
            key={image.name}
            id={image.name}
            type="image"
            url={image.url}
            coordinates={image.coordinates}
          >
            <Layer {...imageLayer} id={image.name} beforeId="ship" />
          </Source>
        ))}
    </Map>
  );
};

export default OdinMap;
