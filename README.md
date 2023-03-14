# Installation

The frontend server is a Node project using typescript and React. It needs node (v18) installed and can be run with

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
# The Tasks

### 1. Create Odin again

Create the Odin frontend again with React and any map library you choose (we recommend Mapbox GL). The map should open up centered in the coordinates `59.8613` latitude and `22.4673` longitude.

### 2. Overlay a SAR image to the map

You were able to task the SAR constellation to take a new image. The image has now downlinked and you can find it from `odin-api/SAR_image_20420212.png`.

The corner coordinates starting from top left are

```
[
    [22.2908182629724, 59.91614254645401],
    [22.578806773313246, 59.947751078236365],
    [22.638044070378744, 59.809992490984754],
    [22.351391574531174, 59.77847599974091],
]
```

Write the functionality to serve this image from the Odin backend to the frontend and overlay it to the map.

### 3. Add the locations of lighthouses to the map

The best way to help the ship navigate is to show the locations of lighthouses on the map. You managed to salvage the old corrupted codebase only a bit, revealing a string related to this data source, it says `seamark:light:range`.

Pull the lighthouse locations with the backend and serve them to the frontend through an endpoint. Visualise them on the map

Also visualise the ship itself. It is currently in coordinates `59.89134, 22.30606`

### 4. Write a short document for the production deployment plan

You remember the magnificently robust way Odin was deployed into production previously. How did it go again?

Write a text document and/or draw a diagram explaining how you would deploy Odin to a production environment. Add it to your repository

### 5. (Optional) Add any other dataset or functionality that could make Odin more useful

If you still have time, visualize any other kind of dataset or add a new functionality that might be useful for Isla when entering the dangerous waters
