from db.connection import get_connection

def get_all_students():
    """
    Retrieves all student records from the database.

    Returns:
        list of tuple: Each tuple contains the fields of a student record.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def add_student(first_name, last_name, email, enrollment_date):
    """
    Inserts a new student record into the database.

    Args:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        email (str): The student's email address.
        enrollment_date (str): Enrollment date in 'YYYY-MM-DD' format.

    Returns:
        None
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s);
    """, (first_name, last_name, email, enrollment_date))
    conn.commit()
    cur.close()
    conn.close()

def update_student_email(student_id, new_email):
    """
    Updates the email address of a student by their ID.

    Args:
        student_id (int): The unique ID of the student.
        new_email (str): The new email address to assign.

    Returns:
        None
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE students
        SET email = %s
        WHERE id = %s;
    """, (new_email, student_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_student(student_id):
    """
    Deletes a student record from the database by ID.

    Args:
        student_id (int): The unique ID of the student to delete.

    Returns:
        None
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = %s;", (student_id,))
    conn.commit()
    cur.close()
    conn.close()