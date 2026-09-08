import sqlite3

DATABASE_NAME = "platform.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            college TEXT,
            degree TEXT,
            branch TEXT,
            graduation_year INTEGER,
            skills TEXT,
            projects TEXT,
            certifications TEXT,
            desired_role TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            industry TEXT,
            description TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS opportunities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            opportunity_type TEXT NOT NULL,
            description TEXT,
            required_skills TEXT NOT NULL,
            location TEXT,
            FOREIGN KEY (company_id) REFERENCES companies(id)
        )
    """)

    connection.commit()
    connection.close()


initialize_database()
