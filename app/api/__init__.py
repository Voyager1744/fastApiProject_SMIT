from fastapi import APIRouter
from app.api.insurance import ins_router

router_v1 = APIRouter(prefix="/api/v1")

router_v1.include_router(
    ins_router
)
