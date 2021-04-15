import os

from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from fastpy.config import get_settings, Settings


app = FastAPI()

register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["fastpy.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True
)


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)) -> dict:
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }