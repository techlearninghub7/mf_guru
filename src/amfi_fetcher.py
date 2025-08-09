import httpx
import logging
from datetime import datetime
from .db import SessionLocal, engine
from .models import funds
from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger("mf.amfi")

AMFI_DAILY_URL = "https://www.amfiindia.com/spages/NAVAll.txt"

def parse_line_to_row(line):
    line = line.strip()
    if not line:
        return None
    # Try splitting by common delimiters
    for sep in (";", ",", "|"):
        if sep in line:
            parts = [p.strip() for p in line.split(sep)]
            break
    else:
        parts = line.split()

    # Heuristic: scheme_code, scheme_name, nav, date
    try:
        scheme_code = parts[0]
        fund_name = parts[1] if len(parts) > 1 else "UNKNOWN"
        nav = None
        nav_date = None
        # find float value for nav scanning from right
        for p in reversed(parts):
            try:
                v = float(p.replace(",", ""))
                nav = v
                break
            except Exception:
                continue
        # find date-like token
        for p in reversed(parts):
            if "/" in p or "-" in p:
                nav_date = p
                break
        if nav is None:
            return None
        return {
            "scheme_code": str(scheme_code)[:64],
            "fund_name": fund_name[:255],
            "amc": "UNKNOWN",
            "category": "Uncategorized",
            "last_nav_date": nav_date or datetime.utcnow().strftime("%Y-%m-%d"),
            "last_nav": float(nav),
        }
    except Exception:
        return None

def fetch_amfi(limit=50):
    """
    Fetch AMFI NAVAll and return parsed rows (best-effort).
    """
    try:
        with httpx.Client(timeout=30) as client:
            resp = client.get(AMFI_DAILY_URL)
            resp.raise_for_status()
            text = resp.text
    except Exception as e:
        logger.exception("AMFI fetch failed: %s", e)
        return []

    rows = []
    for line in text.splitlines():
        if len(rows) >= limit:
            break
        r = parse_line_to_row(line)
        if r:
            rows.append(r)
    logger.info("Parsed %d AMFI rows", len(rows))
    return rows



def seed_amfi(limit=50):
    parsed = fetch_amfi(limit=limit)
    if not parsed:
        return 0

    session = SessionLocal()
    try:
        for r in parsed:
            stmt = (
                insert(funds)
                .values(**r)
                .on_conflict_do_update(
                    index_elements=[funds.c.scheme_code],  # must match unique constraint
                    set_={
                        "fund_name": r["fund_name"],
                        "amc": r["amc"],
                        "category": r["category"],
                        "last_nav_date": r["last_nav_date"],
                        "last_nav": r["last_nav"],
                    },
                )
            )
            session.execute(stmt)

        session.commit()
        return len(parsed)

    except SQLAlchemyError as e:
        session.rollback()
        logger.exception("DB seed failed: %s", e)
        return 0

    finally:
        session.close()

