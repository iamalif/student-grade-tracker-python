# student-grade-tracker-python

A Python command-line application to manage students and their grades, 
built using Object-Oriented Programming (OOP) principles.

## About
This program allows users to add students and grades, view grade 
summaries, calculate averages, and delete student records via a 
console menu. Data is persisted across sessions using two CSV files. 
Built as a personal OOP and CSV practice project.

## Features
- Two classes: Student and Grade with private attributes
- Auto-incrementing unique IDs for both students and grades
- Getter and setter methods for all attributes
- Add a new student
- Add a grade for a specific student
- List all students
- List all grades for a specific student
- Calculate average grade per student
- Calculate class average per subject
- Delete a student and all their associated grades
- Save/load data across two CSV files for persistence between runs
- Input validation separated into a dedicated validators.py module

## Project Structure
```
student-grade-tracker-python/
│
├── student_grade_tracker.py   ← main program
├── validators.py              ← input validation functions
├── students_db.csv            ← student records (auto-generated)
└── grades_db.csv              ← grade records (auto-generated)
```

## How to Run
```bash
python student_grade_tracker.py
```

## Built With
- Python 3
- OOP — two classes, private attributes, getter/setter methods
- CSV module for data persistence across two related files
- Separated input validation module for clean, reusable code

## Data Persistence
Student and grade data are automatically saved to their respective 
CSV files after every operation and reloaded on next launch.
