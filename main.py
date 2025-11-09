from db.schema import initialize_schema
from models.student import (
    get_all_students,
    add_student,
    update_student_email,
    delete_student
)

def menu():
    print("\nStudent Management Menu")
    print("1. View all students")
    print("2. Add a new student")
    print("3. Update student email")
    print("4. Delete a student")
    print("5. Exit")

def main():
    initialize_schema()

    while True:
        menu()
        choice = input("Enter your choice (1–5): ").strip()

        if choice == "1":
            students = get_all_students()
            print("\nAll Students:")
            for student in students:
                print(student)

        elif choice == "2":
            print("\nAdd New Student")
            first_name = input("First name: ").strip()
            last_name = input("Last name: ").strip()
            email = input("Email: ").strip()
            enrollment_date = input("Enrollment date (YYYY-MM-DD): ").strip()
            add_student(first_name, last_name, email, enrollment_date)
            print("Student added successfully.")

        elif choice == "3":
            print("\nUpdate Student Email")
            student_id = int(input("Student ID: ").strip())
            new_email = input("New email: ").strip()
            update_student_email(student_id, new_email)
            print("Email updated successfully.")

        elif choice == "4":
            print("\nDelete Student")
            student_id = int(input("Student ID: ").strip())
            delete_student(student_id)
            print("Student deleted successfully.")

        elif choice == "5":
            print("Exiting program. Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()