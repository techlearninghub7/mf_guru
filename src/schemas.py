from pydantic import BaseModel
from typing import Optional

class FundOut(BaseModel):
    scheme_code: str
    fund_name: str
    amc: Optional[str] = None
    category: Optional[str] = None
    last_nav_date: Optional[str] = None
    last_nav: Optional[float] = None

    class Config:
        orm_mode = True
