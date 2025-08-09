from fastapi import FastAPI
from .api import router as api_router
from .db import engine, metadata
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mf")

app = FastAPI(title="MF Guru API - Sprint 0")

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
def startup_event():
    # Ensure tables exist (useful for local SQLite fallback)
    metadata.create_all(bind=engine)
    logger.info("Startup: ensured metadata / tables.")

@app.get("/")
def root():
    return {"message": "MF Guru API is running"}
