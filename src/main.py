from fastapi import FastAPI
from .api import router as api_router
from .db import engine, metadata
import logging
import threading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mf")

app = FastAPI(title="MF Guru API - Sprint 0")

app.include_router(api_router, prefix="/api/v1")


def init_db():
    try:
        metadata.create_all(bind=engine)
        logger.info("Startup: ensured metadata / tables.")
    except Exception as e:
        logger.exception("DB init failed: %s", e)


@app.on_event("startup")
def startup_event():
    # Run DB init in background so app can respond quickly
    threading.Thread(target=init_db, daemon=True).start()


@app.get("/")
def root():
    return {"message": "MF Guru API is running"}
