from fastapi import FastAPI
from app.api.routes import router as api_router
from app.db import init_db

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    # Initialize the DB schema (MVP usage).
    await init_db.init_db()
    print("Database tables created (if not existing).")

app.include_router(api_router, prefix="/api")