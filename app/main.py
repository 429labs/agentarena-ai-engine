from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Initialize DB or other startup actions
    pass

@app.on_event("shutdown")
async def shutdown():
    # Clean up actions
    pass

app.include_router(api_router, prefix="/api")