from fastapi import APIRouter, HTTPException
from typing import List
from .db import engine, SessionLocal
from .models import funds
from .schemas import FundOut
from .amfi_fetcher import seed_amfi
from sqlalchemy import select
import logging

router = APIRouter()
logger = logging.getLogger("mf.api")

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/funds", response_model=List[FundOut])
def list_funds(limit: int = 50):
    with SessionLocal() as session:
        stmt = select(funds).limit(limit)
        rows = session.execute(stmt).fetchall()
        results = []
        for row in rows:
            # row is a Row object; first element is the table row mapping
            row_dict = dict(row._mapping)
            results.append(FundOut(**row_dict))
        return results

@router.api_route("/funds/seed", methods=["GET", "POST"])
def seed_funds(limit: int = 50):
    count = seed_amfi(limit=limit)
    if count == 0:
        raise HTTPException(status_code=500, detail="Seed failed or no rows parsed")
    return {"status": "ok", "seeded": count}
