from Models.student import Student 
class StudentManagementSystem:
    def __init__(self,filehandler,year):
        self.students=[]
        self.filehandler=filehandler
        self.year= year
    
    def generate_student_id(self):
        if not self.students:
            return int(f"{self.year}000001")
        
        highest_id= max(student.ID for student in self.students) 
        return highest_id + 1     

    def add_student(self):
        try:
            student_id=self.generate_student_id()
            print(f"Generated Student ID: {student_id}")
            length_of_id=10

            if len(str(student_id)) != length_of_id:
                print("Lenth of the ID should not be greater than 10!!")
                return
            
            print(self.students)

            for student in self.students:
                if(student.ID == student_id):
                    print(f"Student with the ID '{student_id}' already exits!!")
                    return

            student_YoE=int(input("Enter Year of Enrollment:\n"))
            if(self.year == student_YoE):
                student_name= input("Enter Student Name:\n")
                student_age=int(input("Enter Student Age:\n"))
                gender = input("Enter your Gender, (M or m) for male or (F or f) for female:\n")
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
            
            student = Student(
                ID=student_id,
                Name=student_name,
                Age=student_age,
                Gender=gender,
                Department=department,
                Program=program,
                Courses=courses,
                M_Status=m_status,
                P_Status=p_status,
                C_Status=c_status
            )
            
            self.students.append(student) 
            print(f"Student with the ID: '{student.ID}' has been added successfully!!")

            self.filehandler.save_student_record(self.students) 
        
        except ValueError:
            print("Enter a valid value for student ID.")

    def view_students(self):
    
        if not self.students:
            print(f"There are No student records for the year {self.year}.")

        else:
            print("*"*25)
            print("\n<<<<<***********OPTTIONS***********>>>>>>\t\n")
            print("1.\t View Student by ID\n")
            print("2.\t View Student by Name\n")
            print("3.\t View Student(s) by Department\n")
            print("4.\t View specific detail\n")
            print("5.\t All Students Recorded\n")
            print("6.\t Exit\n")
            print("*"*25,"\n")

            choice = input("Enter your choice of action from the above: \n")
            if choice == "1":
                self._view_by_id()
                
            elif choice == "2":
                self._view_by_name()

            elif choice == "3":
                self._view_by_department()

            elif choice == "4":
                self._view_specific_detail()
                
            elif choice == "5":
                self._view_all_students()

            elif choice == "6":
                print(".......Exiting the program to view Student Record(s)\n")
                print("......Exit Successful!!\n")
                return 0
            
            else:
                print("Invalid Choice!! Enter a valid choice.💢💢💢")
                return 0
    def _display_student_record(self):
        for student in self.students:
            print("*"*30)
            print(student.Name)
            print(student.ID)
            print(student.Age)
            print(student.Gender)
            print(student.Department)
            print(student.Program)
            print(student.Courses)
            print(student.M_Status)
            print(student.P_Status)
            print(student.C_Status)
            print("*"*30)   
    def _view_by_id(self):
        try:
            st_id = int(input("Enter Student ID: \n"))
            found = False

            for student in enumerate(self.students):
                if(student.ID == st_id):
                    print("<"*12.5,">"*12.5)
                    self._display_student_record(student)
                    print("<"*12.5,">"*12.5)
                    found = True
                    break

            if not found:
                print(f"Student with ID '{st_id}' does not exist")
        except ValueError:
            print("Invalid ID.")
            return
    def _view_by_name(self):
        st_name = input("Enter the Name of the Student:\n")
        found = False
        
        for student in self.students:
            if(student.Name.lower() == st_name.lower()):
                print("<"*12.5,">"*12.5)
                print("Student found!!\n")
                self._display_student_record(student)
                print("<"*12.5,">"*12.5)
                found = True
                break

        if not found:
            print(f"Student with Name '{st_name}' does not exist")
    def _view_by_department(self):
        st_dept = input("Enter Department of Student Association:\n")
        num = 0
        found = False
        for student in self.students:
            if(student.Department == st_dept):
                num += 1
                
                print("<"*12.5,">"*12.5,"\n")
                print(num)
                self._display_student_record(student)
                found = True
                print("*"*25)
                
        if not found:
            print(f"Associative Department '{st_dept}' can not be found!!\n")
    def _view_specific_detail(self):
        print("-"*15)
        print("\n*********OPTIONS*********\n")
        print("\n1. All Names in Records\n")
        print("\n2. All ID's Recorded\n")
        print("\n3. All Ages Recorded\n")
        print("\n4. Exit\n")
        p_choice = input("Please enter your choice from the Options above\n")

        if p_choice == "1":
            for i, student in enumerate(self.students, start=1):
                print(f"Student {i} Name: {student.Name}\n")
                
        elif p_choice == "2":
            for i, student in enumerate(self.students, start=1):
                print(f"Student {i} ID: {student.ID}\n")

        elif p_choice == "3":
            for i, student in enumerate(self.students, start=1):
                print(f"Age of Student {i}: {student.Age}\n")

        elif p_choice == "4":
            print("-"*15,"\n")
            print("."*6, "Exiting","."*6,"\n")
            print("Exit Successful! Thank you for your Patronage.\n")
            return
        else:
            print("Invalid choice! Enter a Valid choice from the list.💢💢💢")
            return
    def _view_all_students(self):
        print("Here is a Print-Out of all Students with available Records:\n")
        found = False

        for student in enumerate(self.students, start=1):
                print("*"*25)
                self._display_student_record(student)
                print("*"*25)
                found = True

        if not found:
            print("No records exist in the file\n")    
            return

    def delete_student_record(self):
        self._view_all_students()
        if not self.students:
            print("No Students recorded to proceed with deletion!!")
        else:
            print("*"*25)
            print("\n<<<>>><<>>**********OPTIONS**********<<<>>><<>>\n")
            print("1. Delete Student Record by ID/Name\n")
            print("2. Delete Student Record by Department\n")
            print("3. Delete all Records of Students\n")
            print("4. Exit\n")
            print("*"*25)
            
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
                        self._delete_by_id() 
                    elif sub_choice == "2":
                        self._delete_by_name()  
                    else:
                        print("INVALID CHOICE!!\n")
                        return
                except ValueError:
                    print("INVALID INPUT!! Please enter valid values for the appropriate choices!!💢💢💢")
            elif choice == "2":
                self._delete_by_department()
            elif choice == "3":
                self._delete_all_student_records()
            elif choice == "4":
                print("Proceeding with Program Exiting!!!\n")
                print(".....please wait...!!\n")
                print("Program exit successful!!👌👌\n")
                return 0
            else:
                print("INVALID CHOICE INPUT!!!❌❌")
                print("pleace enter a valid choice to proceed!!!❌❌")
                return 0    
    def _delete_by_id(self):
        
        print("Selected Deletion By ID!!\n")
        try:
            search_id= int(input("Enter ID:\n"))
            found = False

            for i, student in enumerate(self.students):
                if(student.ID == search_id):
                    found = True
                    print("Record Found!!\n")
                    print("*"*15)
                    self._display_student_record(student)
                    print("*"*15)
                    
                    print("Do you wish to delete this record?")
                    print("\nMINI OPTIONS\n")
                    self._confirm_delete()

                    choice =self._confirm_delete()
                    if choice == "1":
                        print("Executing.....!!\n")
                        print("...Deleting record from records...!\n")
                        del self.students[i]
                        print(f"Record of the Student with the id '{search_id}' has been successfully deleted!!\n")
                        break
                    elif choice == "2":
                        print("Your choice has been acknowledged!!!\n")
                        pass
                    elif choice == "3":
                        print("Exiting....\n")
                        print("Exit successful\n")
                        break
                    else:
                        print("INVALID INPUT!! Enter a valid input for choice💢💢💢\n")
                        return
                    break
            if not found:
                print(f"Record with ID '{search_id}' not be found!!")  
                return 0
        except ValueError:
            print("Invalid ID format")
            return
    def _delete_by_name(self):
        print("Selected Deletion By Name!!\n")
        search_name= input("Enter Name:\n")
        found = False

        for i, student in enumerate(self.students):
            if(student.Name == search_name):
                print("Record Found!!\n")
                print("*"*15)
                self._display_student_record(student)
                print("*"*15)

                found = True
                print("Do you wish to delete this record?")
                print("\nMINI OPTIONS\n")
                self._confirm_delete()

                choice =self._confirm_delete()
                if choice == "1":
                    print("Executing.....!!\n")
                    print("...Deleting record from records...!👌👌\n")
                    del self.students[i]
                    print(f"Record of the Student with the name '{search_name}' has been successfully deleted!!👌👌\n")
                    break
                elif choice == "2":
                    return 
                elif choice == "3":
                    print("Exiting....\n")
                    print("Exit successful\n")
                    return
                else:
                    print("INVALID INPUT!! Enter a valid input for choice💢💢💢\n")
                    return 0        
        else:
            print("Wrong Name or Name does not correspond to any record present\n")
            print("Please enter a valid Name💢💢💢\n")
            return 0
        if not found:
            print(f"Record with Name '{search_name}' not found!!") 
            return 0
    def _delete_by_department(self):
        print("Chosen choice of Action: 'delete by department'.")
        search_dept = input("Enter Department Name:\n")
        dept_found = False

        for i,student in enumerate(self.students):
            if(student.Department == search_dept):
                dept_found = True

                print(f"CHOSEN DEPARTMENT:{search_dept}.\n")
                print(i,student)

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
            department = input("Enter department:\n")
            student_id = input("Enter student ID to delete:\n")

            for i,student in enumerate(self.students):
                if student.Department == department and student.ID == student_id:
                    self.students.remove(i)
                    print("Student record deleted successfully.\n")
                    return
            print("Student not found!\n")
        elif del_choice == "2":
            department = input("Enter department to delete:\n")

            old_count=len(self.students)

            self.students = [student for student in self.students if student.Department != department]

            deleted_count = old_count - len(self.students)

            if deleted_count > 0:
                print(f"{deleted_count} student(s) deleted from {department} department.")
            else:
                print("No students found in that department\n")
        elif del_choice == "3":
            print("Exiting....\n")
            print("done.")
        else:
            print("Invalid choice\n")     
    def _delete_all_student_records(self):
        print("********************************************\n")
        print("Confirm your choice to delete all records of Students!!\n")
        self._confirm_delete()
        print("********************************************\n")

        choice = self._confirm_delete()
        if choice == "1":
            print("Proceeding with the deletion of all Records present!!!\n")
            print(".....please wait....!!!\n")
            self.students.clear()
            self
            print("...!! Deletion complete!!👌👌\n")
        elif choice == "2":
            print("Deletion cancelled!!\n")
        elif choice == "3":
            print("Exiting...!!!\n")
            print("Exit complete!!")
        else:
            print("INVALID CHOICE!!!\n")
            print("Please enter a valid choice input\n")
            return 0    
    def _confirm_delete(self):
        print("1. Yes\n")
        print("2. No\n")
        print("3. Exit\n")

        return input("Enter choice:\n")

    def update_student_record(self):
        if not self.students:
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

            choice = input("Enter your choice from the Above:\n")
            if choice == "1":
                self._update_id()
            elif choice == "2":
                self._update_name()
            elif choice == "3":
                self._update_age()
            elif choice == "4":
                self._update_department()
            elif choice == "5":
                self._update_record()
            elif choice == "6":
                print(">>>Exiting>>>>\n")
                return 0
            else:
                print("Invalid choice!! Enter a valid choice💢💢💢\n")
    def _confirm_update(self):
        print("1. Yes\n")
        print("2. No\n")
        print("3. Exit\n")

        return input("Enter choice:\n")
    def _update_name(self):
        search_name =input("Enter Student Name:\n")
        found = False

        for student in self.students:
            if(student.Name == search_name):
                
                print(f"ID: {student.ID}\n Name: {student.Name}\n Age: {student.Age}\n Department: {student.Department}")
                print("*"*9)
                print("\nOPTIONS\n")
                print("1. Update ID\n")
                print("2. Exit\n")

                confirm_choice = input("Please enter your confirmed choice:\n")
                if confirm_choice == "1":
                    updated_id= int(input("Enter new ID:\n"))
                    
                    if(len(updated_id) != 10):
                        student.ID.remove()
                        student.ID == updated_id
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
            return 0
    def _update_id(self):
        search_ID =input("Enter Student ID:\n")
        found = False

        for student in self.students:
            if(student.ID == search_ID):
                print(f"ID: {student.ID}\n Name: {student.Name}\n Age: {student.Age}\n Department: {student.Department}")
                print("*"*10)
                print("\nOPTIONS\n")
                print("1. Update Name\n")
                print("2. Exit\n")

                found = True
                confirm_choice = input("Please enter your confirmed choice:\n")
                if confirm_choice == "1":
                    update_name= input("Enter new ID:\n")
                    
                    student.Name.remove()
                    student.Name == update_name
                elif confirm_choice == "2":
                    print(">>>Exiting>>>>\n")
                    return confirm_choice
                else:
                    print("Invalid Choice!! Enter a valid choice.💢💢💢")
                    return 0
            
        if not found:
            print(f"Student record with Student ID '{search_ID}' does not exist!!\n")
            return 0
    def _update_age(self):
        search_age =int(input("Enter Student Age:\n"))
        found = False

        for student in self.students:
            if(student.Age == search_age):
                print(f"ID: {student.ID}\n Name: {student.Name}\n Age: {student.Age}\n Department: {student.Department}")
                print("*"*18)
                print("\nOPTIONS\n")
                print("1. Update Student Age\n")
                print("2. Exit\n")

                found = True
                confirm_choice = input("Please enter your confirmed choice:\n")
                if confirm_choice == "1":
                    update_age= input("Enter new Age:\n")
                    
                    student.Age.remove()
                    student.Age == update_age
                elif confirm_choice == "2":
                    print(">>>Exiting>>>>\n")
                    return confirm_choice
                else:
                    print("Invalid Choice!! Enter a valid choice.💢💢💢")
                    return 0
            
        if not found:
            print(f"Student record with Student ID '{student.ID}' does not exist!!\n")
            return 0
    def _update_department(self):
        search_ID =input("Enter Student ID:\n")
        found = False

        for student in self.students:
            if(student.ID == search_ID):
                print(f"ID: {student.ID}\n Name: {student.Name}\n Age: {student.Age}\n Department: {student.Department}")
                print("*"*7)
                print("\nOPTIONS\n")
                print("1. Update Department\n")
                print("2. Exit\n")

                found = True
                confirm_choice = input("Please enter your confirmed choice:\n")
                if confirm_choice == "1":
                    update_dept= input("Enter new Dept. Name:\n")
                    
                    student.Deparment.remove()
                    student.Department == update_dept
                elif confirm_choice == "2":
                    print(">>>Exiting>>>>\n")
                    return confirm_choice
                else:
                    print("Invalid Choice!! Enter a valid choice.💢💢💢")
                    return 0
            
        if not found:
            print(f"Student record with Student ID '{search_ID}' does not exist!!\n")
            return 0
    def _update_record(self):
        print("....Executing Command to Update all info in a Student Record\n")
        print("Update All Info. i.e.(ID, Name, Age, Department, Program, Marital Status, Physical Status, Mental Status\n)")
        choice=self._confirm_update()
        if choice == "1":
            for student in self.students:
                student.ID = int(input("Enter New ID:\n"))
                student.Name = input("Enter New Name:\n")
                student.Age = int(input("Enter New Age:\n"))

                new_courses = []
                while True:
                    new_course = input("Enter new courses (or 'done' to finish):\n")

                    if(new_course.lower() == "done"):
                        break

                    new_courses.append(new_course)
                
                student.Courses = new_courses
                student.Department = input("Enter New Department:\n")
                student.M_Status = input("Enter New Marital Status:\n")
                student.P_Status = input("Enter New Physical Status:\n")
                student.C_Status = input("Enter New Mental Status:\n")
                print("All details of the Student record has been updated!!\n")
        
        elif choice == "2":
            pass
        else:
            print("INVALID CHOICE!")
            return 0

    def summarize_Student_record(self):
        Department= input("Enter Department:")
        total = 0
        count = 0

        for i,student in self.students:
            if (student["Department"] == Department):
                count += 1
                total += i
        
        print(f"Department: {Department}\n")
        print(f"Number of Students in the Department: {count}\n")
        print(f"Total Number of Students in the {self.year}: {total}\n") 