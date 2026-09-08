import re


def clean_skills(skills):
    """
    Convert a skill string into a clean set of skills.
    Example:
    'Python, SQL, Java, Machine Learning'
    ->
    {'python', 'sql', 'java', 'machine learning'}
    """

    if not skills:
        return set()

    skills = skills.lower()

    # Support commas, semicolons, pipes and new lines
    skills = re.split(r"[,;|\n]+", skills)

    return {
        skill.strip()
        for skill in skills
        if skill.strip()
    }


def calculate_match(student_skills, required_skills):
    """
    Calculate percentage match between student skills
    and skills required by an opportunity.
    """

    student = clean_skills(student_skills)
    required = clean_skills(required_skills)

    if not required:
        return {
            "match_percentage": 0,
            "matched_skills": [],
            "missing_skills": []
        }

    matched = student.intersection(required)
    missing = required - student

    percentage = round(
        (len(matched) / len(required)) * 100,
        2
    )

    return {
        "match_percentage": percentage,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing)
    }


def rank_student(student_skills, required_skills):
    """
    Generate a match result for a student.
    """

    result = calculate_match(
        student_skills,
        required_skills
    )

    if result["match_percentage"] >= 80:
        level = "Excellent Match"
    elif result["match_percentage"] >= 60:
        level = "Good Match"
    elif result["match_percentage"] >= 40:
        level = "Partial Match"
    else:
        level = "Low Match"

    result["match_level"] = level

    return result
