from fastapi import FastAPI
from core.database import Base, engine

from api import auth, api_keys, usage, analytics

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(api_keys.router)
app.include_router(usage.router)
app.include_router(analytics.router)