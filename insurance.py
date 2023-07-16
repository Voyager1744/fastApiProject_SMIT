import json
import os

from fastapi import APIRouter, Path
from models import Insurance

ins_router = APIRouter(
    prefix="/insurance",
    tags=["insurance"]
)

basedir = os.path.abspath(os.path.dirname(__file__))

with open(basedir + "/tariffs.json", "r") as f:
    tariffs = json.load(f)


async def get_rate(date, cargo_type):
    """Получить ставку страхования по дате и типу груза."""

    if date not in tariffs:
        return None
    for date_str in tariffs[date]:
        if date_str["cargo_type"] == cargo_type:
            return date_str["rate"]


@ins_router.get(
    "/{date_string}/{cargo_type}/{declared_value}",
    responses={
        400: {
            "description": "Incorrect date",
        }
    })
async def get_insurance(
        date_string: str = Path(regex=r"\d{4}-\d{2}-\d{2}"),
        cargo_type: str = Path(..., description="Glass, Other"),
        declared_value: float = Path(...),
):
    """Получить стоимость страхования."""

    # insurance = await Insurance.filter(cargo_type=cargo_type).first()
    # if insurance is None:
    #     insurance = Insurance(cargo_type=cargo_type,
    #                           declared_value=declared_value)
    #     await insurance.save()

    rate = await get_rate(date_string, cargo_type)

    if rate is None:
        return 'The date is not included in the tariff'
    try:
        cost = float(rate) * float(declared_value)
    except ValueError:
        return 'The declared value is not a number or cargo type not found'
    return {"Cost_of_insurance": f"{cost:.2f}"}
