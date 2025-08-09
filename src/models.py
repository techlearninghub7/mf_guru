from sqlalchemy import Table, Column, String, Float
from sqlalchemy.sql import func
from .db import metadata

funds = Table(
    "funds",
    metadata,
    Column("scheme_code", String(64), primary_key=True),
    Column("fund_name", String(255), nullable=False),
    Column("amc", String(128)),
    Column("category", String(128)),
    Column("last_nav_date", String(32)),
    Column("last_nav", Float),
)
