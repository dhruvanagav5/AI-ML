def add():
    name = input("Enter name of the student :")
    with open("students.txt" , "a") as file:
        file.write(name + "\n")
    return "Student added successfully"
def view():
    try:
        with open("students.txt", "r") as file:
            students = file.read()

            if students:
                print("\nStudent List:")
                print(students)
            else:
                print("No students found.")

    except FileNotFoundError:
        print("No student records found.")
              
def delete():
    name = input("Enter name of the student to delete :")
    with open("students.txt","r") as file:
        students = file.readlines()
    with open("students.txt","w") as file:
        for student in students:
            if student.strip() != name:
                file.write(student)
    return "Student deleted successfully"

