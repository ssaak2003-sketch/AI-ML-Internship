students = []

def add_student():
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    student = {
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\n===== Student Records =====")
        for i, student in enumerate(students, start=1):
            print(f"\nStudent {i}")
            print("Name :", student["Name"])
            print("Age :", student["Age"])
            print("Course :", student["Course"])

def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["Name"].lower() == name.lower():
            print("\nStudent Found")
            print(student)
            return

    print("Student not found.")

def update_student():
    name = input("Enter student name to update: ")

    for student in students:
        if student["Name"].lower() == name.lower():
            student["Age"] = input("Enter New Age: ")
            student["Course"] = input("Enter New Course: ")
            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    name = input("Enter student name to delete: ")

    for student in students:
        if student["Name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")

while True:

    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")