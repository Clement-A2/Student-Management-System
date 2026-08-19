import os

def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Pauses the program until the user presses Enter."""
    input("\nPress Enter to continue...")

def print_header(title):
    """Prints a formatted header."""
    print("=" * 45)
    print(title.center(45))
    print("=" * 45,"\n")

def print_line():
    """Prints a separator line."""
    print("-" * 50)

def print_menu():
    """Prints a menu dropdown."""
    print("*************EXECUTABLE COMMANDS*************\n")
    print("1.\t Add Student Record\n")
    print("2.\t View Student Record(s)\n")
    print("3.\t Delete Student Record(s)\n")
    print("4.\t Update Student Record(s)\n")
    print("5.\t Summarize Student Record(s)\n")
    print("6.\t Save Records\n")
    print("7.\t Exit Program\n")
    print("*"*30,"\n")
    print("********************************************\n")

    choice = input("Enter your choice of action:\n")

def get_menu_choice(min_choice, max_choice):
    """Gets a valid menu choice from the user."""
    while True:
        try:
            choice = int(input("Enter your choice: "))

            if min_choice <= choice <= max_choice:
                return choice

            print(f"Please enter a number between {min_choice} and {max_choice}.")

        except ValueError:
            print("Invalid input. Please enter a number.")

def confirm_action(message):
    """Ask the user to confirm an action."""
    answer = input(f"{message} (Y/N): ").strip().upper()
    return answer == "Y"

def format_name(name):
    """Format a name consistently."""
    return name.title().strip()

def current_year():
    """Return the current year."""
    from datetime import datetime
    return datetime.now().year

def display_success(message):
    print(f"\n✓ {message}")

def display_error(message):
    print(f"\n✗ {message}")