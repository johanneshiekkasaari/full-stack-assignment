import './App.css';
import MapBox from './components/MapBox';

export const App = () => {
  if (!process.env.REACT_APP_MAPBOX_TOKEN) {
    return <>Please add valid Mapbox token</>
  }
  return (
    <div>
      <MapBox/>
    </div>
  );
}

