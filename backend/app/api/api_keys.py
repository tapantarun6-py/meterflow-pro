import uuid
from fastapi import APIRouter

router = APIRouter()

@router.post("/generate-key")
def generate_key():
    return {"api_key": str(uuid.uuid4())}