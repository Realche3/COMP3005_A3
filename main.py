import psycopg2

conn = psycopg2.connect( host="localhost", dbname ="postgres", user="postgres", password="622950678", port="5432" )

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
       id SERIAL PRIMARY KEY,
       first_name VARCHAR(50) not null,
       last_name VARCHAR(50) not null,
       email VARCHAR(100) UNIQUE not null,
         enrollment_date DATE
    );
""")

cur.execute("""
   INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

""")

"""
    getAllStudents: Fetches and prints all student records from the database.
    returns: None
"""
def getAllStudents():
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

"""
    addStudent: Adds a new student record to the database.
    first_name: str - The first name of the student.
    last_name: str - The last name of the student.
    email: str - The email address of the student.
    enrollment_date: str - The enrollment date of the student in 'YYYY-MM-DD' format.
    
    returns: None
"""
def addStudent(first_name, last_name, email, enrollment_date):
    cur.execute("""
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s);
    """, (first_name, last_name, email, enrollment_date))

def updateStudentEmail(student_id, new_email):
    cur.execute("""
        UPDATE students
        SET email = %s
        WHERE id = %s;
    """, (new_email, student_id))

def deleteStudent(student_id):
    cur.execute("""
        DELETE FROM students
        WHERE id = %s;
    """, (student_id,))
    





conn.commit()
cur.close()
conn.close()

