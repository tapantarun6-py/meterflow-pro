from fastapi import APIRouter, HTTPException
from schemas.user_schema import UserLogin
from core.security import create_token

router = APIRouter()

# demo login
if True:
    DEMO_USER = "tarun1206"
    DEMO_PASS = "ttt111"

@router.post("/login")
def login(user: UserLogin):
    if user.username == DEMO_USER and user.password == DEMO_PASS:
        token = create_token(1)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")