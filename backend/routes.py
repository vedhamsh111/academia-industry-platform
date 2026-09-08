from fastapi import APIRouter, HTTPException
from .database import get_connection
from .models import StudentCreate, CompanyCreate, OpportunityCreate
from ai.matching import calculate_match
router = APIRouter()


# ---------------- STUDENTS ----------------

@router.post("/students")
def create_student(student: StudentCreate):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO students
            (name, email, phone, college, degree, branch,
             graduation_year, skills, projects, certifications, desired_role)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            student.name,
            student.email,
            student.phone,
            student.college,
            student.degree,
            student.branch,
            student.graduation_year,
            student.skills,
            student.projects,
            student.certifications,
            student.desired_role
        ))

        connection.commit()

        return {
            "message": "Student created successfully",
            "student_id": cursor.lastrowid
        }

    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        connection.close()


@router.get("/students")
def get_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return students


@router.get("/students/{student_id}")
def get_student(student_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()
    connection.close()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return dict(student)


# ---------------- COMPANIES ----------------

@router.post("/companies")
def create_company(company: CompanyCreate):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO companies
            (name, email, industry, description)
            VALUES (?, ?, ?, ?)
        """, (
            company.name,
            company.email,
            company.industry,
            company.description
        ))

        connection.commit()

        return {
            "message": "Company created successfully",
            "company_id": cursor.lastrowid
        }

    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        connection.close()


@router.get("/companies")
def get_companies():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM companies")
    companies = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return companies


# ---------------- OPPORTUNITIES ----------------

@router.post("/opportunities")
def create_opportunity(opportunity: OpportunityCreate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id FROM companies WHERE id = ?",
        (opportunity.company_id,)
    )

    company = cursor.fetchone()

    if not company:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    cursor.execute("""
        INSERT INTO opportunities
        (company_id, title, opportunity_type, description,
         required_skills, location)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        opportunity.company_id,
        opportunity.title,
        opportunity.opportunity_type,
        opportunity.description,
        opportunity.required_skills,
        opportunity.location
    ))

    connection.commit()

    opportunity_id = cursor.lastrowid
    connection.close()

    return {
        "message": "Opportunity created successfully",
        "opportunity_id": opportunity_id
    }


@router.get("/opportunities")
def get_opportunities():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            opportunities.*,
            companies.name AS company_name
        FROM opportunities
        JOIN companies
        ON opportunities.company_id = companies.id
    """)

    opportunities = [dict(row) for row in cursor.fetchall()]
    @router.post("/match")
def match_skills(student_skills: str, required_skills: str):
    result = calculate_match(
        student_skills,
        required_skills
    )

    return result

    connection.close()

    return opportunities

