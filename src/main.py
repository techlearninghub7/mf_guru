from fastapi import FastAPI
from .api import router as api_router
from .db import engine, metadata
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mf")

app = FastAPI(title="MF Guru API - Sprint 0")

# API routes
app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
def startup_event():
    try:
        # Non-blocking DB initialization
        metadata.create_all(bind=engine)
        logger.info("Startup: ensured metadata / tables.")
    except Exception as e:
        logger.exception(f"Startup DB init failed: {e}")

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}
