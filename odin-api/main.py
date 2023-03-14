from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.routers import image_route
from app.routers import lighthouse_route
from app.routers import ship_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def home():
    return RedirectResponse(url="/docs")

app.include_router(image_route.router)
app.include_router(lighthouse_route.router)
app.include_router(ship_route.router)
