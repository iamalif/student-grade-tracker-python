# Python Student Grade Tracker

A command-line application for managing student records and numerical grades. Built as a Python practice project, it demonstrates object-oriented programming, relationships between records, filtering, arithmetic summaries and CSV persistence.

## Features

- Add students and list their IDs and names.
- Record a subject and numerical score for an existing student.
- List all grade records for a student.
- Calculate a student's mean across their recorded grades.
- Calculate a subject's mean across matching grade records.
- Delete a student and their associated grades.
- Save students and grades in separate CSV files and load them at startup.

## Getting started

Python 3 is required. The application uses the standard library and needs no third-party packages.

Download or clone the repository, open a terminal in its root folder, and run:

```bash
python student_grade_tracker.py
```

Use `python3 student_grade_tracker.py` if your system uses `python3` for Python 3. Running from the repository folder ensures the application uses the included CSV files.

## Example workflow

1. Choose **1** to add a fictional student such as `Alex Example`.
2. Choose **3** to list students and find their IDs.
3. Choose **2** to enter the student's ID, a subject such as `Mathematics` and a score.
4. Choose **4** to inspect that student's grade records.
5. Choose **5** for the student's mean or **6** for a subject mean.
6. Choose **0** to exit.

## Score and average semantics

The input helper accepts non-negative numerical scores without enforcing an upper limit. The application does not impose a 0-100 scale, letter grades, pass thresholds or a particular national grading system. Use comparable score scales when interpreting averages.

Each recorded grade receives equal weight. Adding another grade for the same student and subject creates a separate record rather than replacing the previous one. Consequently, the subject mean is calculated across grade records, not across one equally weighted average per student. Subject matching is exact and case-sensitive.

## Structure

| Component | Responsibility |
|---|---|
| `Student` | Student ID and name |
| `Grade` | Grade ID, associated student ID, subject and score |
| `student_grade_tracker.py` | Classes, menu, record operations, summaries and CSV persistence |
| `validators.py` | Reusable input helpers |
| `students_db.csv` | Saved student records |
| `grades_db.csv` | Saved grade records linked to students by ID |

A student can have multiple grade records. The application checks that a student exists before adding a grade for their ID.

## Persistence

Adding a student writes the student file; adding a grade writes the grade file. Deleting a student removes their associated grades and writes both files. Startup loads the saved records, treating a missing file as an empty collection.

Paths are relative to the working directory. The two CSV files are written separately, without database transactions or automatic backups. This is a local learning application, not a production student-information system.

## Skills demonstrated

Python, classes and encapsulation, related data records, CSV file handling, input validation, filtering, arithmetic aggregation and command-line interaction.
