# Mapbox locations with FastAPI

![React](https://img.shields.io/badge/React-v.18-pink)
![MapBox](https://img.shields.io/badge/react--map--gl-v.7.0-brightgreen)
![fastAPI](https://img.shields.io/badge/FastApi-v.0.45-red)
![Python](https://img.shields.io/badge/Python-v.3.11-blue)

This project use FastAPI in the backend to build minimum apis to return locations with longitude an lattitude from dummy data. Frontend is built with React and MapBox react-map-gl library. This project would require access token from MapBox to retrieve map data.

## Installation

The frontend server is a Node project using typescript and React. Access to ken to MapBox should be created as environment variable in file .env (created in subfolder directory) as name `REACT_APP_MAPBOX_TOKEN`. It needs node (v18) installed and can be run with

```
cd odin-ui
npm install
npm start
```

The backend is a python FastAPI backend. It needs an empty python 3.11 environment (like conda, pyenv or poetry) and can be set up and started with

```
cd odin-api
pip install -r requirements.txt
uvicorn main:app --reload
```

## odin-api

1. This sub-project is created in OOP methodology, with 3 models: Image, LightHouse, Ship
2. There are 4 layers in the app: 
    * Model (create entity)
    * Repositoty (return raw data, connected to Model layer)
    * Service (get and transform data, call to Repository layer)
    * Router (handle request and response, call to Service layer)
3. SAR image is stored in the backend and retrievable via image router
4. Ship returns the current (hard-coded) location of ship
5. LightHouse returns the locations of (hard-coded) lighthouses

## odin-ui

1. This is minimum (no styling so far) map layout with image overlay on map.
2. Information about image, ship, and available lighthourses are obtained from odin-api

## Overview

![screen-gif](./view.gif)

## Issues and future improvements

1. odin-api has been deployed in Deta Space [https://mapboxapi-1-x6118897.deta.app](deta app). However, the server has Cors issue despite Cors middleware has been added. Local deployment has no Cors issue so far, so that could be FastAPI version in deployment.
2. odin-ui has minimum theme. Possible styling such as lighthouse animation (ex: lighting dots, ininite illuminating) can be added.
3. Possibility to turn odin-ui to server side rendering to track realtime location updates.