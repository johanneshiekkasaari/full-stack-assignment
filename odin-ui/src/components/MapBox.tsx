import React, { useEffect, useState } from 'react'
import Map, { Source, Layer, LayerProps } from 'react-map-gl'
import 'mapbox-gl/dist/mapbox-gl.css'

import axiosInstance from '../common/axiosInstance';
import Ship from './Ship';
import LightHouse from './LightHouse';
import { AxiosError } from 'axios';

const layerStyle: LayerProps = {
    type: "raster",
    paint: {
        "raster-fade-duration": 0
    }
};

type Coord = [number, number]

interface Pointer {
    latitude: number
    longitude: number
}

interface ImageResponse {
    url: string
    corner_coords: Coord[]
}

const MapBox = () => {
    const [coords, setCoords] = useState<Coord[]>([])
    const [img, setImg] = useState("")
    const [pointer, setPointer] = useState<Pointer>()
    const [error, setError] = useState("");
    useEffect(() => {
        axiosInstance.get<ImageResponse>("images/get")
            .then(res => {
                setCoords(res.data.corner_coords)
                setImg(res.data.url)
            })
            .catch(e => {
                const axiosError = e as AxiosError
                setError(axiosError.message)
            })
    }, [])
    if (error) {
        return (
            <div>
                <p>{ error}</p>
            </div>
        )
    }
    return (
        <div>
            <div>
                {pointer && <p>Current location: latitude {pointer?.latitude}, longitude {pointer?.longitude}</p>}
            </div>
            <Map
                mapboxAccessToken={process.env.REACT_APP_MAPBOX_TOKEN}
                initialViewState={{
                    longitude: 22.4673,
                    latitude: 59.8613,
                    zoom: 10
                }}
                mapStyle="mapbox://styles/mapbox/streets-v9"
                style={{ width: '100vw', height: '100vh' }}
                onMouseMove={(e) => setPointer({ latitude: e.lngLat.lat, longitude: e.lngLat.lng })}
            >
                <Source type="image" url={img} coordinates={coords}>
                    <Layer {...layerStyle} />
                </Source>
                <Ship />
                <LightHouse />
            </Map>
        </div>
    )
}

export default MapBox