import json
import os

# =====================================
# STUDENT MANAGEMENT SYSTEM
# =====================================

FILE_NAME = "students.json"

SUBJECTS = [
    "Python",
    "Maths",
    "Physics",
    "English",
    "Computer"
]


# Store student records
students = {}


# =====================================
# LOAD AND SAVE DATA
# =====================================

def load_students():
    global students

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                students = json.load(file)
        except (json.JSONDecodeError, OSError):
            students = {}
            print("Could not load saved records.")
    else:
        students = {}


def save_students():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("Warning: Could not save records.")


# =====================================
# CALCULATIONS
# =====================================

def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks):
    return sum(marks) / len(marks)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


# =====================================
# ADD STUDENT
# =====================================

def add_student():
    print("\n===== ADD STUDENT =====")

    roll = input("Enter roll number: ").strip()

    if not roll:
        print("Roll number cannot be empty.")
        return

    if roll in students:
        print("Roll number already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    marks = []

    for subject in SUBJECTS:
        while True:
            try:
                mark = float(
                    input("Enter " + subject + " marks: ")
                )

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    students[roll] = {
        "name": name,
        "marks": marks
    }

    save_students()
    print("\nStudent added successfully!")


# =====================================
# VIEW ALL STUDENTS
# =====================================

def view_students():
    print("\n===== ALL STUDENTS =====")

    if len(students) == 0:
        print("No student records found.")
        return

    for roll, student in students.items():
        marks = student["marks"]
        name = student["name"]

        total = calculate_total(marks)
        percentage = calculate_percentage(marks)
        grade = calculate_grade(percentage)

        print("\n----------------------------")
        print("Roll Number:", roll)
        print("Name:", name)

        for i in range(len(SUBJECTS)):
            print(SUBJECTS[i] + ":", marks[i])

        print("Total:", total, "/ 500")
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)
        print("----------------------------")


# =====================================
# SEARCH STUDENT
# =====================================

def search_student():
    print("\n===== SEARCH STUDENT =====")

    roll = input("Enter roll number: ").strip()

    if roll not in students:
        print("Student not found.")
        return

    student = students[roll]
    marks = student["marks"]

    print("\nRoll Number:", roll)
    print("Name:", student["name"])

    for i in range(len(SUBJECTS)):
        print(SUBJECTS[i] + ":", marks[i])

    total = calculate_total(marks)
    percentage = calculate_percentage(marks)

    print("Total:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", calculate_grade(percentage))


# =====================================
# CLASS AVERAGE
# =====================================

def class_average():
    print("\n===== CLASS AVERAGE =====")

    if len(students) == 0:
        print("No student records found.")
        return

    total = 0

    for student in students.values():
        total += calculate_percentage(student["marks"])

    average = total / len(students)

    print("Number of students:", len(students))
    print("Class average:", round(average, 2), "%")


# =====================================
# FIND TOPPER
# =====================================

def find_topper():
    print("\n===== CLASS TOPPER =====")

    if len(students) == 0:
        print("No student records found.")
        return

    topper_roll = None
    highest = -1

    for roll, student in students.items():
        percentage = calculate_percentage(student["marks"])

        if percentage > highest:
            highest = percentage
            topper_roll = roll

    topper = students[topper_roll]

    print("Roll Number:", topper_roll)
    print("Name:", topper["name"])
    print("Percentage:", round(highest, 2), "%")
    print("Grade:", calculate_grade(highest))


# =====================================
# DELETE STUDENT
# =====================================

def delete_student():
    print("\n===== DELETE STUDENT =====")

    roll = input("Enter roll number: ").strip()

    if roll in students:
        del students[roll]
        save_students()
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# =====================================
# SORT STUDENTS
# =====================================

def sort_students():
    print("\n===== RANK LIST =====")

    if len(students) == 0:
        print("No student records found.")
        return

    ranked = sorted(
        students.items(),
        key=lambda item: calculate_percentage(
            item[1]["marks"]
        ),
        reverse=True
    )

    rank = 1

    for roll, student in ranked:
        percentage = calculate_percentage(student["marks"])

        print(
            str(rank) + ".",
            student["name"],
            "| Roll:", roll,
            "| Percentage:", round(percentage, 2), "%"
        )

        rank += 1


# =====================================
# MAIN MENU
# =====================================

def main():
    load_students()

    while True:
        print("\n")
        print("===================================")
        print("      STUDENT MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Calculate Class Average")
        print("5. Find Class Topper")
        print("6. Delete Student")
        print("7. Sort Students by Marks")
        print("8. Exit")
        print("===================================")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            class_average()

        elif choice == "5":
            find_topper()

        elif choice == "6":
            delete_student()

        elif choice == "7":
            sort_students()

        elif choice == "8":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 8.")


# =====================================
# START PROGRAM
# =====================================

if __name__ == "__main__":
    main()
