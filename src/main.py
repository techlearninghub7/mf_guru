import os
import logging
import uvicorn
from fastapi import FastAPI
from .api import router as api_router
from .db import engine, metadata

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mf")

app = FastAPI(title="MF Guru API - Sprint 0")
app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
def startup_event():
    metadata.create_all(bind=engine)
    logger.info("Startup: ensured metadata / tables.")

@app.get("/")
def root():
    return {"message": "MF Guru API is running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("src.main:app", host="0.0.0.0", port=port)
