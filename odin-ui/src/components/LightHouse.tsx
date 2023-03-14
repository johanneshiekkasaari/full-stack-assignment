import React, { useEffect, useState } from 'react'
import { Marker } from 'react-map-gl'
import axiosInstance from '../common/axiosInstance'

interface LightHouse {
    latitude: number
    longitude: number
    seamark: string
    light: string
    range: number
}

const LightHouse = () => {
    const [lightHouses, setLightHouses] = useState<LightHouse[]>()
    useEffect(() => {
        axiosInstance.get<LightHouse[]>("lighthouses")
            .then(res => setLightHouses(res.data))
    }, [])
    return (
        <div>
            {
                lightHouses?.map((lh, index) =>
                (
                    <Marker
                        key={index}
                        longitude={lh.longitude}
                        latitude={lh.latitude}
                        
                    >
                        <img src="images/lighthouse.png" alt={lh.seamark} width={20} />
                    </Marker>
                )
                )
            }
        </div>
    )
}

export default LightHouse