import Map from 'react-map-gl';
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

const map = () => {
  return <Map
      mapLib={maplibregl}
      initialViewState={{
        longitude: 22.4673,
        latitude: 59.8613,
        zoom: 10
      }}
      style={{width: 1024, height: 600}}
      mapStyle="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
  />
}

export default map;
