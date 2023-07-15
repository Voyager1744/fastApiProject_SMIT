from fastapi import APIRouter

ins_router = APIRouter(
    prefix="/insurance",
    tags=["insurance"]
)


@ins_router.get(
    "/{date_string}",
    responses={
        400: {
            "description": "Incorrect date",
        }
    })
async def get_insurance(date_string: str):
    return f"Insurance for {date_string}"
