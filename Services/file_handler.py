import csv
import ast
from Models.student import Student
class FileHandler:

    def __init__(self,year=None,filename=None):
        if filename is not None:
            self.filename = filename
        elif year is not None:
            self.filename=f"Student_Records_{year}.csv"
        else:
            self.filename = "Student_Records.csv"

    def save_student_record(self,students):
        with open(self.filename, "w", newline="") as file:
            fieldnames=["ID", "Name", "Age", "Gender", "Department", "Program", "Courses", "M_Status", "P_Status", "C_Status"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in students:
                writer.writerow({
                    "ID":student.ID,
                    "Name":student.Name, 
                    "Age":student.Age, 
                    "Gender":student.Gender,
                    "Department":student.Department, 
                    "Program":student.Program, 
                    "Courses":student.Courses, 
                    "M_Status":student.M_Status, 
                    "P_Status":student.P_Status, 
                    "C_Status":student.C_Status
                    })

    def load_student_records(self):
        students=[]
        try:
            with open(self.filename, "r", newline="") as file:
                reader= csv.DictReader(file)

                for row in reader:
                    student = Student(
                        int(row["ID"]),
                        row["Name"],
                        int(row["Age"]),
                        row["Gender"],
                        row["Department"],
                        row["Program"],
                        ast.literal_eval(row["Courses"]),
                        row["M_Status"],
                        row["P_Status"],
                        row["c_Status"]
                    )

                students.append(student)
        except FileNotFoundError:
            print("No Student_Record file found! Starting with an empty list.")

        return students