from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "ODIN-API NOT FOUND"
