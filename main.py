from Services.file_handler import FileHandler
from Services.management import StudentManagementSystem
from Utils.helpers import (
    clear_screen,
    pause,
    print_header,
    get_menu_choice,
    confirm_action,
    print_menu,
    current_year,
    display_success,
    display_error
)
print("*"*30)
print("ENTER YEAR OF STUDENT ENROLLMENT")
print("*"*30,'\n')
year = int(input("Enter the Year of Admission:\n"))
file_handler = FileHandler(year)

system = StudentManagementSystem(file_handler,year)
file_handler.load_student_records()
while True:
    clear_screen()
    print("********************************************\n")
    print("************* WELCOME TO GCTU **************\n")
    print_header("STUDENT MANAGEMENT SYSTEM")
    print(f"*************** YEAR {year} *****************\n")
    print("***********OF STUDENT ENROLLMENT************\n")
    print("********************************************\n")

    print_menu()

    if print_menu.choice == "1":
        system.add_student()
        pause()
    elif print_menu.choice == "2":
        system.view_students()
        pause()
    elif print_menu.choice == "3":
        system.delete_student_record()
        file_handler.save_student_record(system.students)
        pause()
    elif print_menu.choice == "4":
        system.update_student_record()
        file_handler.save_student_record(system.students)
        pause()
    elif print_menu.choice == "5":
        system.summarize_Student_record()
        pause()
    elif print_menu.choice == "6":
        file_handler.save_student_record(system.students)
        pause()
    elif print_menu.choice == "7":
        confirm_action("Confirm Exiting of Program!!")
        print("Executing command to exit program....!!!\n")
        print("....please wait....!!!\n")
        display_success("...program exit successful>>.\n")
        pause()
        break
    else:
        display_error("INVALID CHOICE FOR COMMAND EXECUTION!!!\n")
        print("Please Enter a valid choice for command execution!!>>.")
        pause()
        break