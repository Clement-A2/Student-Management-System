import csv
Students = []

print("*"*30)
print("ENTER YEAR OF STUDENT ENROLLMENT")
print("*"*30,'\n')
year = int(input("Year of Addmissions:\n"))

def generate_student_id():
    if not Students:
        return int(f"{year}000001")
    
    highest_id= max(student["ID"] for student in Students) 
    return highest_id + 1     

def add_student():
    try:
        student_id=generate_student_id()
        print(f"Generated Student ID: {student_id}")
        length_of_id=10

        if(len(str(student_id)) > length_of_id):
            print("Lenth of the ID should not be greater than 10!!")
        elif(len(str(student_id)) < length_of_id):
            print("Length of Student ID should not be less than 10!!")
            return 0
        else:
            pass
        
        print(Students)

        for student in Students:
            if(student["ID"] == student_id):
                print(f"Student with the ID '{student_id}' already exits!!")
            else:
                pass

        student_YoE=int(input("Enter Year of Enrollment:\n"))
        if(year == student_YoE):
            student_name= input("Enter Student Name:\n")
            student_age=int(input("Enter Student Age:\n"))
            gender = input("Enter your Gender(Male or Female):\n")
            program=input("Enter Student Porgram of Study:\n")
            m_status=input("Enter current Marital Status:\n")
            p_status=input("Enter current physical status:\n")
            c_status=input("Do you have any mental Issues? Enter(Yes or No):\n")
            
            courses = []
            while True:
                course = input("Enter a course (or 'done' to finish):\n")

                if(course.lower() == "done"):
                    break

                courses.append(course)
            
            department=input("Enter Department of Association:\n")
        else:
            print(f"Student year of enrollment should be equal to the year of Addmission!!\n")
            return 0
        
        Students.append({"ID":student_id, "Name":student_name, "Age":student_age, "Gender":gender, "Department":department, "Program":program, "Courses":courses, "M_Status":m_status, "P_Status":p_status, "C_Status":c_status}) 
        print(f"Student with the ID: '{student_id}' has been added successfully!!")

    except ValueError:
        print("Enter a valid value for student ID.")

def view_students():
    if not Students:
        print(f"There are No student records for the year {year}.")

    else:
        print("*"*25)
        print("\n\t\t<<<<<*************OPTTIONS*************>>>>>>\t\t\n")
        print("1.\t View Student by ID\n")
        print("2.\t View Student by Name\n")
        print("3.\t View Student(s) by Department\n")
        print("4.\t View / list Student specific detail\n")
        print("5.\t All Students Recorded\n")
        print("6.\t Exit\n")
        print("*"*25,"\n")
        print("*"*25)

        choice = input("Enter your choice of action from the above: \n")
        if choice == "1":
            st_id = int(input("Enter Student ID: \n"))
            found = False

            for student in Students:
                if(student["ID"] == st_id):
                    print("<"*12.5,">"*12.5)
                    print("Student found!!\n")
                    print(f"Name: {student['Name']}\n")
                    print(f"ID: {student['ID']}\n")
                    print(f"Age: {student['Age']}\n")
                    print(f"Gender: {student['Gender']}\n")
                    print(f"Department: {student['Department']}\n")
                    print(f"Program: {student['Program']}\n")
                    print(f"Courses: {student['Courses']}\n")
                    print(f"Marital Status: {student['M_Status']}\n")
                    print(f"Phisical Status: {student['P_Status']}\n")
                    print(f"Mental Status: {student['C_Status']}\n")
                    print("<"*12.5,">"*12.5)
                    found = True
                    break

            if not found:
                print(f"Student with ID '{st_id}' does not exist")
        
        elif choice == "2":
            st_name = input("Enter the Name of the Student:\n")
            found = False
            
            for student in Students:
                if(student["Name"] == st_name):
                    print("<"*12.5,">"*12.5)
                    print("Student found!!\n")
                    print(f"Name: {student['Name']}\n")
                    print(f"ID: {student['ID']}\n")
                    print(f"Age: {student['Age']}\n")
                    print(f"Gender: {student['Gender']}\n")
                    print(f"Department: {student['Department']}\n")
                    print(f"Program: {student['Program']}\n")
                    print(f"Courses: {student['Courses']}\n")
                    print(f"Marital Status: {student['M_Status']}\n")
                    print(f"Phisical Status: {student['P_Status']}\n")
                    print(f"Mental Status: {student['C_Status']}\n")
                    print("<"*12.5,">"*12.5)
                    found = True
                    break

            if not found:
                print(f"Student with ID '{st_name}' does not exist")

        elif choice == "3":
            st_dept = input("Enter Department of Student Association:\n")
            num = 0
            for student in Students:
                if(student["Department"] == st_dept):
                    num += 1
                    
                    print("<"*12.5,">"*12.5,"\n")
                    print(num)
                    print(f"{st_dept} Department!\n")
                    print(f"Name: {student['Name']}\n")
                    print(f"ID: {student['ID']}\n")
                    print(f"Age: {student['Age']}\n")
                    print(f"Gender: {student['Gender']}\n")
                    print(f"Program: {student['Program']}\n")
                    print(f"Courses: {student['Courses']}\n")
                    print(f"Marital Status: {student['M_Status']}\n")
                    print(f"Phisical Status: {student['P_Status']}\n")
                    print(f"Mental Status: {student['C_Status']}\n")
                    print("<"*12.5,">"*12.5,"\n")

                else:
                    print(f"Associative Department '{st_dept}' can not be found!!\n")
        
        elif choice == "4":
            print("-"*15)
            print("\n*********OPTIONS*********\n")
            print("\n1. All Names in Records\n")
            print("\n2. All ID's Recorded\n")
            print("\n3. All Ages Recorded\n")
            print("\n4. Exit\n")
            p_choice = input("Please enter your choice from the Options above\n")

            if p_choice == "1":
                for i, student in enumerate(Students, start=1):
                    print(f"Student {i} Name: {student["Name"]}\n")
                    break
            elif p_choice == "2":
                for i, student in enumerate(Students, start=1):
                    print(f"Student {i} ID: {student["ID"]}\n")
                    break
            elif p_choice == "3":
                for i, student in enumerate(Students, start=1):
                    print(f"Age of Student {i}: {student["Age"]}\n")
                    break
            elif p_choice == "4":
                print("-"*15,"\n")
                print("."*6, "Exiting","."*6,"\n")
                print("Exit Successful! Thank you for your Patronage.\n")
                return
            else:
                print("Invalid choice! Enter a Valid choice from the list.💢💢💢")
                return
            
        elif choice == "5":
            print("Here is a Print-Out of all Students with available Records:\n")
            is_empty = False

            for i, student in enumerate(Students, start=1):
                while(is_empty != len(Students)):
                    print("*"*25)
                    print(f"Name: {student['Name']}\n")
                    print(f"ID: {student['ID']}\n")
                    print(f"Age: {student['Age']}\n")
                    print(f"Gender: {student['Gender']}\n")
                    print(f"Department: {student['Department']}\n")
                    print(f"Program: {student['Program']}\n")
                    print(f"Courses: {student['Courses']}\n")
                    print(f"Marital Status: {student['M_Status']}\n")
                    print(f"Phisical Status: {student['P_Status']}\n")
                    print(f"Mental Status: {student['C_Status']}\n")
                    print("*"*25)
                break
        
        elif choice == "6":
            print(".......Exiting the program to view Student Record(s)\n")
            print("......Exit Successful!!\n")
            return 0
        
        else:
            print("Invalid Choice!! Enter a valid choice.💢💢💢")
            return 0
        
def update_student_record():
    if not Students:
        print("No Student records Available \n")

    else:
        print("-"*17)
        print("\n**********OPTIONS**********\n")
        print("1. Update Student ID\n")
        print("2. Update Student Name\n")
        print("3. Update Student Age\n")
        print("4. Update Student Department\n")
        print("5. Update Student Record\n")
        print("6. Exit\n")
        print("*"*17)

        found = False
        choice = input("Enter your choice from the Above:\n")
        if choice == "1":
            search_name =input("Enter Student Name:\n")

            for student in Students:
                if(student["Name"] == search_name):
                    
                    print(f"ID: {student["ID"]}\n Name: {student["Name"]}\n Age: {student["Age"]}\n Department: {student["Department"]}")
                    print("*"*9)
                    print("\nOPTIONS\n")
                    print("1. Update ID\n")
                    print("2. Exit\n")

                    confirm_choice = input("Please enter your confirmed choice:\n")
                    if confirm_choice == "1":
                        update_id= int(input("Enter new ID:\n"))
                        
                        if(len(update_id) != 10):
                            student["ID"].remove()
                            student["ID"] == update_id
                        else:
                            print("Please a Student ID should not be less than or greater than 10\n")
                            return
                    elif confirm_choice == "2":
                        print(">>>Exiting>>>>\n")
                        return confirm_choice
                    else:
                        print("Invalid Choice!! Enter a valid choice.💢💢💢")
                        return 0
                
                if not found:
                    print(f"Student record with Student Name '{search_name}' does not exist!!\n")
                    return
            
        elif choice == "2":
            search_ID =input("Enter Student ID:\n")

            for student in Students:
                if(student["ID"] == search_ID):
                    print(f"ID: {student["ID"]}\n Name: {student["Name"]}\n Age: {student["Age"]}\n Department: {student["Department"]}")
                    print("*"*10)
                    print("\nOPTIONS\n")
                    print("1. Update Name\n")
                    print("2. Exit\n")

                    found = True
                    confirm_choice = input("Please enter your confirmed choice:\n")
                    if confirm_choice == "1":
                        update_name= input("Enter new ID:\n")
                        
                        student["Name"].remove()
                        student["Name"] == update_name
                    elif confirm_choice == "2":
                        print(">>>Exiting>>>>\n")
                        return confirm_choice
                    else:
                        print("Invalid Choice!! Enter a valid choice.💢💢💢")
                        return 0
                
                if not found:
                    print(f"Student record with Student ID '{search_ID}' does not exist!!\n")
                    return
        
        elif choice == "3":
            search_age =int(input("Enter Student Age:\n"))

            for student in Students:
                if(student["Age"] == search_age):
                    print(f"ID: {student["ID"]}\n Name: {student["Name"]}\n Age: {student["Age"]}\n Department: {student["Department"]}")
                    print("*"*18)
                    print("\nOPTIONS\n")
                    print("1. Update Student Age\n")
                    print("2. Exit\n")

                    found = True
                    confirm_choice = input("Please enter your confirmed choice:\n")
                    if confirm_choice == "1":
                        update_age= input("Enter new Age:\n")
                        
                        student["Age"].remove()
                        student["Age"] == update_age
                    elif confirm_choice == "2":
                        print(">>>Exiting>>>>\n")
                        return confirm_choice
                    else:
                        print("Invalid Choice!! Enter a valid choice.💢💢💢")
                        return 0
                
                if not found:
                    print(f"Student record with Student ID '{search_ID}' does not exist!!\n")
                    return 0
        
        elif choice == "4":
            search_ID =input("Enter Student ID:\n")

            for student in Students:
                if(student["ID"] == search_ID):
                    print(f"ID: {student["ID"]}\n Name: {student["Name"]}\n Age: {student["Age"]}\n Department: {student["Department"]}")
                    print("*"*7)
                    print("\nOPTIONS\n")
                    print("1. Update Department\n")
                    print("2. Exit\n")

                    found = True
                    confirm_choice = input("Please enter your confirmed choice:\n")
                    if confirm_choice == "1":
                        update_dept= input("Enter new Dept. Name:\n")
                        
                        student["Deparment"].remove()
                        student["Department"] == update_dept
                    elif confirm_choice == "2":
                        print(">>>Exiting>>>>\n")
                        return confirm_choice
                    else:
                        print("Invalid Choice!! Enter a valid choice.💢💢💢")
                        return 0
                
                if not found:
                    print(f"Student record with Student ID '{search_ID}' does not exist!!\n")
                    return 0
                
        elif choice == "5":
            print("....Executing Command to Update all info in a Student Record\n")
            print("Update All Info. i.e.(ID, Name, Age, Department, Program, Marital Status, Physical Status, Mental Status\n)")
            print("<>OPTIONS<>\n")
            print("1. Yes\n")
            print("2. No\n")

            choice = input("Enter your choice from the above options:\n")
            if choice == "1":
                student["ID"] = int(input("Enter New ID:\n"))
                student["Name"] = input("Enter New Name:\n")
                student["Age"] = int(input("Enter New Age:\n"))

                new_courses = []
                while True:
                    new_course = input("Enter a course (or 'done' to finish):\n")

                    if(new_course.lower() == "done"):
                        break

                    new_courses.append(new_course)
                
                student["Courses"] = new_courses
                student["Department"] = input("Enter New Department:\n")
                student["M_Status"] = input("Enter New Marital Status:\n")
                student["P_Status"] = input("Enter New Physical Status:\n")
                student["C_Status"] = input("Enter New Mental Status:\n")
            
            elif choice == "2":
                pass

            else:
                print("INVALID CHOICE!")
                return 0
            
        elif choice == "6":
            print(">>>Exiting>>>>\n")
            return 0
        else:
            print("Invalid choice!! Enter a valid choice💢💢💢\n")

def delete_student_record():
    view_students()
    if not Students:
        print("No Students recorded to proceed with deletion!!")
    else:
        print("<"*15,">"*15)
        print("\n<<<>>><<>>**********OPTIONS**********<<<>>><<>>\n")
        print("1. Delete Student Record by ID/Name\n")
        print("2. Delete Student Record by Department\n")
        print("3. Delete all Records of Students\n")
        print("4. Exit\n")
        print("<"*17,">"*17)
        
        choice = input("Enter your choice of Action:\n")
        if choice == "1":
            try:
                print("*"*8)
                print("\nSUB OPTIONS\n")
                print("1. Del by ID\n")
                print("2. Del by Name\n")
                print("*"*8)

                sub_choice = input("Enter a choice from the sub_choices above:\n")
                if sub_choice == "1":
                    print("Selected Deletion By ID!!\n")
                    search_id= int(input("Enter ID:\n"))
                    found = False

                    for i, student in Students:
                        if(student["ID"] == search_id):
                            print("Record Found!!\n")
                            print("*"*15)
                            print(f"Name: {student['Name']}, ID: {student['ID']}, Age: {student['Age']}, Department: {student['Department']}, Program: {student['Program']}, Courses: {student['Courses']}, Marital Status: {student['M_Status']}, Phisical Status: {student['P_Status']}, Mental Status: {student['C_Status']}\n")
                            print("*"*15)
                            
                            found = True
                            print("Do you wish to delete this record?")
                            print("\nMINI OPTIONS\n")
                            print("1. Yes\n")
                            print("2. No\n")

                            confirm_choice = input("Enter your choice:\n")
                            if confirm_choice == "1":
                                print("Executing.....!!\n")
                                print("...Deleting record from records...!\n")
                                del Students[i]
                                print(f"Record of the Student with the id '{search_id}' has been successfully deleted!!\n")
                                break
                            elif confirm_choice == "2":
                                print("Your choice has been acknowledged!!!\n")
                                return 0
                            else:
                                print("INVALID INPUT!! Enter a valid input for choice💢💢💢\n")
                                return
                            
                        else:
                            print("Wrong ID or ID does not correspond to any record present\n")
                            print("Please enter a valid ID number💢💢💢\n")
                            return 0
                    if not found:
                        print(f"Record with ID '{search_id}' can not be found!!")  
                        return 0
                      
                elif sub_choice == "2":
                    print("Selected Deletion By Name!!\n")
                    search_name= int(input("Enter Name:\n"))
                    found = False

                    for i, student in Students:
                        if(student["Name"] == search_name):
                            print("Record Found!!\n")
                            print("*"*15)
                            print(f"Name: {student['Name']}, ID: {student['ID']}, Age: {student['Age']}, Department: {student['Department']}, Program: {student['Program']}, Courses: {student['Courses']}, Marital Status: {student['M_Status']}, Phisical Status: {student['P_Status']}, Mental Status: {student['C_Status']}\n")
                            print("*"*15)

                            found = True
                            print("Do you wish to delete this record?")
                            print("\nMINI OPTIONS\n")
                            print("1. Yes\n")
                            print("2. No\n")

                            confirm_choice = input("Enter your choice:\n")
                            if confirm_choice == "1":
                                print("Executing.....!!\n")
                                print("...Deleting record from records...!👌👌\n")
                                del Students[i]
                                print(f"Record of the Student with the name '{search_name}' has been successfully deleted!!👌👌\n")
                                break
                            elif confirm_choice == "2":
                                print("Your choice has been acknowledged!!!\n")
                                return 0
                            else:
                                print("INVALID INPUT!! Enter a valid input for choice💢💢💢\n")
                                return 0
                            
                        else:
                            print("Wrong Name or Name does not correspond to any record present\n")
                            print("Please enter a valid Name💢💢💢\n")
                            return
                    if not found:
                        print(f"Record with ID '{search_id}' can not be found!!") 
                        return 0
                    
                else:
                    print("INVALID CHOICE!!\n")
                    return
                
            except ValueError:
                print("INVALID INPUT!! Please enter valid values for the appropriate choices!!💢💢💢")
        
        elif choice == "2":
            department_list=[]
            print("Chosen choice of Action: 'delete by department'.")
            search_dept = input("Enter Department Name:\n")
            dept_found = False

            for student in Students:
                if(student["Department"] == search_dept):
                    dept_found = True

                    print(f"CHOSEN DEPARTMENT:{search_dept}.\n")
                    department_list.append({{student['ID']},{student['Name']},{student['Age']},{student['Program']},{student['Courses']},{student['M_Status']},{student['P_Status']},{student['C_Status']}})

                    for dept in enumerate(department_list,start=1):
                        print(f"{student['ID']},{student['Name']},{student['Age']},{student['Program']},{student['Courses']},{student['M_Status']},{student['P_Status']},{student['C_Status']}\n")
                        print("*"*25)
            if not dept_found:
                print(f"No records exists within the {search_dept} Department")
                return 0

            print("\n","*"*25)
            print("\n\t<<<<>>>>OPTIONS<<<<>>>>\t\n")
            print("1. Delete a Student record within the Department\n")
            print("2. Delete all Student records within the Department\n")
            print("3. Exit\n")
            print("*"*25)

            del_choice=input("Enter your confirmed choice frome the above:\n")
            if del_choice == "1":
                confirm_id=int(input("Enter the ID of the desired record to delete\n"))
                is_found=False
                for i, dept in department_list:
                    for student["Department"] in Students == department_list:
                        if(student["ID"] == confirm_id):
                            is_found = True
                            print("Executing delete command....\n")
                            print(".....delete complete!!👌👌\n")
                            del Students[i]
                            del department_list[i]
                            print(f"Record with the ID: '{confirm_id}' has been removed from the Department records👌👌\n")
                            break
                if not is_found:
                    print(f"No record within the department has an ID of '{confirm_id}'!!")
                    return 0 

            elif del_choice == "2":
                print("Confirm your choice to delete all records of students within the department\n")
                print("1. Yes\n")
                print("2. No\n")
                print("3. Exit\n")
                

                del_confirm = input("Enter your choice for final confirmation:\n")
                if del_confirm == "1":
                    for i,student in Students:
                        if(student["Department"] == search_dept):
                            print("Executing command.... to delete all records within the department..!!!\n")
                            print(".....deletion complete!!👌👌\n")
                            del Students[i]
                            department_list.clear()
                            print(f"Record with the ID: '{confirm_id}' has been removed from the Department records👌👌\n")
                            break
                
                elif del_confirm == "3":
                    pass
                else:
                    return 0
                
            else:
                while(del_choice == "3"):
                    print("...Exiting program...!!!")
                    print("Program.. Exit.. Successful!!👌👌")
                    break
        
        elif choice == "3":
            print("********************************************\n")
            print("Confirm your choice to delete all records of students!!\n")
            print("1. Yes\n")
            print("2. No\n")
            print("3. Exit\n")
            print("********************************************\n")

            all_del=input("Enter your choice:\n")
            if all_del == "1":
                for student in Students:
                    print("Proceeding with the deletion of all Records present!!!\n")
                    print(".....please wait....!!!\n")
                    Students.clear()
                    print("...!! Deletion complete!!👌👌\n")
                    break

            elif all_del == "2":
                pass
            elif all_del == "3":
                while(all_del != "1"):
                    print("Breaking command chain!!!\n")
                    break

            else:
                print("INVALID CHOICE!!!\n")
                print("Please enter a valid choice input\n")
                return 0
            
        elif choice == "4":
            print("Proceeding with Program Exiting!!!\n")
            print(".....please wait...!!\n")
            print("Program exit successful!!👌👌\n")
            return 0
        
        else:
            print("INVALID CHOICE INPUT!!!❌❌")
            print("pleace enter a valid choice to proceed!!!❌❌")
            return 0
        
def summarize_Student_record():
    Department= input("Enter Department:")
    total = 0
    count = 0

    for student in Students:
        if (student["Department"] == Department):
            count += 1
            total = len(Students)
    
    print(f"Department: {Department}\n")
    print(f"Number of Students: {count}\n")
    print(f"Total Total Number of Students: {total}")

def save_student_record():
    filename = f"Student_Records_{year}.csv"
    with open(filename, "w") as file:
        fieldnames=["ID", "Name", "Age", "Gender", "Department", "Program", "Courses", "M_Status", "P_Status", "C_Status"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(Students)

def load_student_records():
    Students=[]
    filename =f"Student_Records_{year}.csv"
    try:
        with open(filename, "r", newline="") as file:
            reader= csv.DictReader(file)

            for row in reader:
                row["ID"] = int(row["ID"])
                row["Age"] = int(row["Age"])

                Students.append(row)
    except FileNotFoundError:
        print("No Student_Record file found! Starting with an empty list.")

    return Students

Students = load_student_records()

while True:
    print("********************************************\n")
    print("************* WELCOME TO GCTU **************\n")
    print("******** STUDENT MANAGEMENT SYSTEM *********\n")
    print(f"**************YEAR {year} *****************\n")
    print("***********OF STUDENT ENROLLMENT************\n")
    print("********************************************\n")

    print("*************EXECUTABLE COMMANDS*************\n")
    print("1.\t Add Student Record\n")
    print("2.\t View Student Record(s)\n")
    print("3.\t Delete Student Record(s)\n")
    print("4.\t Update Student Record(s)\n")
    print("5.\t Summarize Student Record(s)\n")
    print("6.\t Exit Program\n")
    print("*"*30,"\n")
    print("********************************************\n")

    choice = input("Enter your command of actions:\n")

    if choice == "1":
        add_student()
        save_student_record()
    elif choice == "2":
        view_students()
        save_student_record()
    elif choice == "3":
        delete_student_record()
        save_student_record()
    elif choice == "4":
        update_student_record()
        save_student_record()
    elif choice == "5":
        summarize_Student_record()
    elif choice == "6":
        print("Executing command to exit program....!!!\n")
        print("....please wait....!!!\n")
        print("...program exit successful>>.\n")
        break
    else:
        print("INVALID CHOICE FOR COMMAND EXECUTION!!!\n")
        print("Please Enter a valid choice for command execution!!>>.")
        break