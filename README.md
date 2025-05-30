# Introduction

This is the recruitment assignment for a full stack engineer position. We have created an empty frontend and backend project for you. You are expected to finish the tasks in this assigment and return a working local application along with this repository either as a forked public github repository or a zipped project via email.

If you hit a wall on some task or you're just unable to finish it in time, you can still return whatever code you have with comments why you think it's not working and what would you do with better time.

We expect the tasks to take 4-6h of time.

# Installation

The frontend server is a Node project using typescript and React. It needs node (v18) installed and can be run with

```
cd odin-ui
npm install
npm start
```

The backend is a python FastAPI backend. It needs an empty python 3.12 environment (like conda or pyenv) and can be set up and started with

```
cd odin-api
pip install -r requirements.txt
uvicorn main:app --reload
```

# The Prequel

The year is 2075. The Gulf stream has shut down 30 years ago and you're alone on an old ice monitoring station in the Turku archipelago. A massive solar storm lights up the night sky with an intense aurora borealis. Beautiful, but very disastrous for electronics.

Suddenly, a crackling voice cuts through the static on the radio:
```
---CChhHHRrrZZZ can anyone hear me? Our ship's AI is down---CHzzRR help!
I'm a mechanical engineer on an hydrogen tanker,
we're heading towards treacherous waters!
```

Your best hope is Odin, the legacy ice monitoring platform visualising the near real time imagery from ICEYE SAR satellites. But the solar flare was too much. As you try to boot it up, a stark message appears:
ERROR 404 - ODIN NOT FOUND

Odin's memory is wiped. The source code is empty. The tanker has about 4-6 hours before it hits the dangerous ice and rocks. It's time to code.

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

### 4. Write a document or diagram for the production deployment plan

Write a text document and/or draw a diagram explaining how you would deploy Odin to a production environment. Add it or link to it to your repository.

You can use any tool you'd like, one great option for diagrams is https://excalidraw.com/

### 5. (Optional) Make the project more robust

If you still have time, you can make the existing project more robust with e.g tests.
