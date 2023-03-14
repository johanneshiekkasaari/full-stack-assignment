import React, { useEffect, useState } from 'react'
import { Marker } from 'react-map-gl'

import axiosInstance from '../common/axiosInstance'

interface Ship {
    latitude: number
    longitude: number
}

const Ship = () => {
    const [ship, setShip] = useState<Ship|undefined>()
    useEffect(() => {
        axiosInstance.get<Ship>("ship")
        .then(res => setShip(res.data))
    }, [])
    return (
        <div>
            {ship && (
                <Marker longitude={ship?.longitude} latitude={ship?.latitude} anchor="bottom">
                    <img src="images/marker.png" width={30} />
                </Marker>
            )}
        </div>
        
    )
}

export default Ship