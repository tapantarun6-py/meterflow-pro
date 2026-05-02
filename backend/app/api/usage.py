from fastapi import APIRouter
from services.usage_service import calculate_bill

router = APIRouter()

fake_usage = {}

@router.get("/use-api")
def use_api(api_key: str):
    if api_key not in fake_usage:
        fake_usage[api_key] = 1
    else:
        fake_usage[api_key] += 1

    count = fake_usage[api_key]

    return {
        "usage": count,
        "bill": calculate_bill(count)
    }