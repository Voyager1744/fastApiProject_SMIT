from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from app.api import router_v1

app = FastAPI()

app.include_router(router_v1)

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": "insurance_db",
                "host": "localhost",
                "port": "5432",
                "user": "postgres",
                "password": "postgres",
            },
        },
    },
    "apps": {
        "models": {
            "models": ["app.api.models"],
            "default_connection": "default",
        },
    },
}

# Register Tortoise ORM with FastAPI
register_tortoise(app, config=TORTOISE_ORM)


@app.on_event("startup")
async def startup():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()


@app.on_event("shutdown")
async def shutdown():
    await Tortoise.close_connections()
