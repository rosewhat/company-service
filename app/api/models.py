from pydantic import BaseModel
from typing import List, Optional


class CompanyIn(BaseModel):
    name: str
    description: str
    industry: int
    age: int
    employees_id: List[int]


class CompanyOut(CompanyIn):
    id: int


class CompanyUpdate(CompanyIn):
    name: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[int] = None
    age: Optional[int] = None
    employees_id: Optional[List[int]] = None