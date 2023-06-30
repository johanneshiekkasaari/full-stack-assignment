import './App.css';
import Map from './Map';

const ErrorMessage = () => {
  return (
      <div className="error-message-container">
        <h1 className="error-message">
        ERROR 404 - ODIN NOT FOUND
        </h1>
      </div>
  );
};

export const App = (): JSX.Element => {
  return (
    <Map/>
  );
}

