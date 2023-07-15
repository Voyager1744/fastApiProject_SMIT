from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api import router_v1

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(router_v1)
