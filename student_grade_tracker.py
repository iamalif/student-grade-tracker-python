"""
Student Grade Tracker

Add students and their grades per subject
Calculate average grade per student
Calculate class average per subject
Save/load to CSV
Good practice: reading, writing, updating specific rows
"""

"""
Classes:
Class - Attributes
Student - student_id, name
Grade - grade_id, student_id, subject, grade
Features:

Add a student
Add a grade for a student
List all students
List all grades for a specific student
Calculate average grade per student
Calculate class average per subject
Delete a student
Save/load all data to/from CSV

Two CSV files:

students.csv — stores student records
grades.csv — stores grade records
"""

# Imports

from validators import *
import csv

# Classes

class Student:
    counter = 0

    def __init__(self, name):
        Student.counter += 1
        self.__student_id = Student.counter
        self.__name = name

    def get_student_id(self):
        return self.__student_id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def __str__(self):
        return f"Student ID: {self.__student_id}, Name: {self.__name}"

class Grade:
    counter = 0

    def __init__(self, student_id, subject, grade):
        Grade.counter += 1
        self.__grade_id = Grade.counter
        self.__student_id = student_id
        self.__subject = subject
        self.__grade = grade

    def get_grade_id(self):
        return self.__grade_id
    
    def get_student_id(self):
        return self.__student_id
    
    def get_subject(self):
        return self.__subject
    
    def get_grade(self):
        return self.__grade

    def set_subject(self, subject):
        self.__subject = subject

    def set_grade(self, grade):
        self.__grade = grade
    
    def __str__(self):
        return f"Grade ID: {self.__grade_id}, Student ID: {self.__student_id}, Subject: {self.__subject}, Grade: {self.__grade}"
    

# Functions

students = []
grades = []

def add_student():
    name = get_non_empty_string("Please enter student name: ")
    student = Student(name)
    students.append(student)
    save_student_to_csv()

def add_grade():
    student_id = get_positive_int("Please enter student ID: ")
    if not any(student.get_student_id() == student_id for student in students):
        print("Student not found.")
        return
    subject = get_non_empty_string("Please enter subject: ")
    grade = get_positive_float("Please enter grade: ")
    new_grade = Grade(student_id, subject, grade)
    grades.append(new_grade)
    save_grades_to_csv()

def list_students():
    if len(students) == 0:
        print("No student records available.")
    else:
        for student in students:
            print(student)

def list_grades():
    student_id = get_positive_int("Please enter student ID: ")
    student_grades = [grade  for grade in grades if grade.get_student_id() == student_id]
    if len(student_grades) == 0:
        print("No grades available for this student.")
    else:
        for grade in student_grades:
            print(grade)

def average_grade():
    student_id = get_positive_int("Please enter student ID: ")
    student_grades = [grade for grade in grades if grade.get_student_id() == student_id]
    if len(student_grades) == 0:
        print("No grades available for this student.")
    else:
        average = sum(grade.get_grade() for grade in student_grades)/len(student_grades)
        print(average)

def class_average():
    subject = get_non_empty_string("Please enter subject: ")
    subject_grades = [grade for grade in grades if grade.get_subject() == subject]
    if len(subject_grades) == 0:
        print("No grades available for this subject.")
    else:
        average = sum(grade.get_grade() for grade in subject_grades)/len(subject_grades)
        print(average)

def delete_student():
    student_id = get_positive_int("Please enter student ID: ")
    for student in students:
        if student.get_student_id() == student_id:
            students.remove(student)
            grades[:] = [grade for grade in grades if grade.get_student_id() != student_id]
            save_student_to_csv()
            save_grades_to_csv()
            return
    print("Student not available.")



def user_menu():
    """Main interactive loop that displays the menu and routes user choices."""
    while True:
        print("\nEnter 1 to add student")
        print("Enter 2 to add grade")
        print("Enter 3 to list students")
        print("Enter 4 to list grades")
        print("Enter 5 to find average grade")
        print("Enter 6 to find class average")
        print("Enter 7 to delete student")
        print("Enter 0 to Exit\n")

        # Re-prompt until the user enters a value in the valid menu range
        while True:
            choice = get_positive_int("Type your choice and press enter: ")
            if 0 <= choice <= 7:
                break
            print("\nChoice needs to be between 0 to 7.")

        if choice == 1:
            add_student()
        elif choice == 2:
            add_grade()
        elif choice == 3:
            list_students()
        elif choice == 4:
            list_grades()
        elif choice == 5:
            average_grade()
        elif choice == 6:
            class_average()
        elif choice == 7:
            delete_student()
        elif choice == 0:
            print("\nGoodbye!")
            break

# CSV functions

def save_student_to_csv():
        # Overwrite the CSV file with the current state of all expenses
        # newline="" prevents csv.writer from adding extra blank lines on Windows
        with open("students_db.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name"])  # Header row
            for student in students:
                writer.writerow([
                    student.get_student_id(),
                    student.get_name()
                ])

def load_student_from_csv():
        try:
            with open("students_db.csv", "r") as file:
                # DictReader maps each row to a dict using the header row as keys
                reader = csv.DictReader(file)
                for row in reader:
                    # Set the class counter to one below the saved ID so that
                    # __init__'s increment restores the exact original ID
                    Student.counter = int(row["Student ID"]) - 1
                    student = Student(row["Name"])
                    students.append(student)
        except FileNotFoundError:
            pass  # No CSV file yet — normal on first run, just start with an empty list

def save_grades_to_csv():
    with open("grades_db.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Grade ID", "Student ID", "Subject", "Grade"])
        for grade in grades:
            writer.writerow([
                grade.get_grade_id(),
                grade.get_student_id(),
                grade.get_subject(),
                grade.get_grade()
            ])

def load_grades_from_csv():
    try:
        with open("grades_db.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Grade.counter = int(row["Grade ID"]) - 1
                grade = Grade(int(row["Student ID"]), row["Subject"], float(row["Grade"]))
                grades.append(grade)
    except FileNotFoundError:
        pass


def main():
    load_student_from_csv()
    load_grades_from_csv()
    user_menu()

if __name__ == "__main__":
    main()