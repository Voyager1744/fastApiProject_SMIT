from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from routs import router_v1

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
                "user": "tortoise",
                "password": "qwerty123",
            },
        },
    },
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        },
    },
}

# Register Tortoise ORM with FastAPI
register_tortoise(app, config=TORTOISE_ORM)
