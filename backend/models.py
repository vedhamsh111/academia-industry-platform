from pydantic import BaseModel
from typing import Optional


class StudentCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    college: Optional[str] = None
    degree: Optional[str] = None
    branch: Optional[str] = None
    graduation_year: Optional[int] = None
    skills: Optional[str] = ""
    projects: Optional[str] = ""
    certifications: Optional[str] = ""
    desired_role: Optional[str] = ""


class CompanyCreate(BaseModel):
    name: str
    email: str
    industry: Optional[str] = None
    description: Optional[str] = None


class OpportunityCreate(BaseModel):
    company_id: int
    title: str
    opportunity_type: str
    description: Optional[str] = None
    required_skills: str
    location: Optional[str] = None
