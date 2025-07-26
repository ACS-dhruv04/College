def add_student(students):
    """Function to add student details"""
    roll_no = input("Enter Roll Number: ")
    if roll_no in students:
        print("Student with this Roll Number already exists!")
        return
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))
    # Storing details in nested dictionary
    students[roll_no] = {"Name": name, "Marks": marks}
    print(f"Student {name} added successfully!")

def display_students(students):
    """Function to display all student details"""
    if not students:
        print("No student records found.")
    else:
        print("\nStudent Records:")
        for roll, details in students.items():
            print(f"Roll No: {roll}, Name: {details['Name']}, Marks: {details['Marks']}")

def search_student(students):
    """Function to search for a student by roll number"""
    roll_no = input("Enter Roll Number to search: ")
    if roll_no in students:
        print(f"Student Found: Name: {students[roll_no]['Name']}, Marks: {students[roll_no]['Marks']}")
    else:
        print("Student not found.")

def update_marks(students):
    """Function to update marks of a student"""
    roll_no = input("Enter Roll Number to update marks: ")
    if roll_no in students:
        new_marks = float(input("Enter new marks: "))
        students[roll_no]['Marks'] = new_marks
        print("Marks updated successfully!")
    else:
        print("Student not found.")

def delete_student(students):
    """Function to delete student record"""
    roll_no = input("Enter Roll Number to delete: ")
    if roll_no in students:
        del students[roll_no]
        print("Student record deleted successfully!")
    else:
        print("Student not found.")

# Main Program
students = {}
while True:
    print("\n===== Student Management Menu =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        add_student(students)
    elif choice == '2':
        display_students(students)
    elif choice == '3':
        search_student(students)
    elif choice == '4':
        update_marks(students)
    elif choice == '5':
        delete_student(students)
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
