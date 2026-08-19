from datetime import datetime
# ===============================
# FILE SETTINGS
# ===============================

CSV_FILE = "data/students.csv"

# ===============================
# SCHOOL SETTINGS
# ===============================

CURRENT_YEAR = datetime.now().year

MAX_STUDENTS = 500

# ===============================
# STUDENT SETTINGS
# ===============================

MIN_AGE = 15
MAX_AGE = 60

MIN_GRADE = 0
MAX_GRADE = 100

PASS_MARK = 50

# ===============================
# MENU OPTIONS
# ===============================

MAIN_MENU = """
=========================================
      STUDENT MANAGEMENT SYSTEM
=========================================

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Statistics
7. Save Records
8. Load Records
9. Exit

=========================================
"""

# ===============================
# MESSAGES
# ===============================

WELCOME_MESSAGE = "Welcome to the Student Management System"

GOODBYE_MESSAGE = "Thank you for using the system."

SAVE_SUCCESS = "Student records saved successfully."

LOAD_SUCCESS = "Student records loaded successfully."

NO_RECORDS = "No student records found."

INVALID_OPTION = "Invalid menu option."

STUDENT_NOT_FOUND = "Student not found."