import os

students = [] # Initialize the students list

def display_menu():
    """Show banner and menu options"""
    print("-" * 33)
    print("*** Student Management System ***")
    print("-" * 33)
    print("""Select option below
    1. Add a Student
    2. Search Student
    3. Display Students By Grade
    4. Delete a Student
    0. Quit""")
    print("-" * 33)

def is_empty_input(input_data):
    """Check for empty user input."""
    return True if input_data == '' else False

def add_student(student_number, student_surname, student_given_name, unit_mark):
    """Add student record to the system."""
    student = {
        "student_number": student_number,
        "student_surname": student_surname,
        "student_given_name": student_given_name,
        "unit_mark": unit_mark,
    }
    students.append(student)

def search_students(search_key):
    """Search student(s) by number or or partial name match."""
    search_results = []
    for student in students:
        if str(student["student_number"]) == search_key or search_key.lower() in student["student_surname"].lower() or search_key.lower() in student["student_given_name"].lower():
            search_results.append(student)
    return search_results

def student_exists(student_number):
    # Check if student exists in the list
    for student in students:
        if student["student_number"] == student_number:
            return True
    return False

def calculate_student_grade(mark):
    if mark >= 80:
        return 'HD'
    elif mark >= 70:
        return 'D'
    elif mark >= 60:
        return 'C'
    elif mark >= 50:
        return 'P'
    else:
        return 'N'

def display_students_by_grade(grade):
    """Display the names of students who achieved the specified grade for the unit."""
    results = []
    for student in students:
        student_mark = student['unit_mark']
        student_grade = calculate_student_grade(student_mark)
        if student_grade == grade:
            results.append(student)
    return results

def delete_student(student_number):
    """Remove a student record from the system."""
    for student in students:
        if student["student_number"] == student_number:
            students.remove(student)
            return True
    return False

def main():
    while True:
        os.system("clear") # for clearing screen
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Enter student details below.")

            # Get student number
            while True:
                try:
                    student_number = int(input("Student Number: "))
                    if student_number <= 0:
                        print("\nError: invalid student number. Try again!\n")
                    elif student_exists(student_number):
                        print(f"\nStudent number '{student_number}' already exists. Try again.\n")
                    else:
                        break
                except ValueError:
                    print("\nError: invalid student number. Try again!\n")
            
            # Get student surname
            student_surname = input("Student Surname: ")

            # Get student given name
            while True:
                student_given_name = input("Student Given Name: ")
                if is_empty_input(student_given_name):
                    print("\nError: given name cannot be empty. Try again.\n")
                else:
                    break
            
            # Get unit mark
            while True:
                try:
                    unit_mark = float(input("Unit Mark: "))
                    if unit_mark >= 0:
                        break
                    else:
                        print("\nError: invalid mark. Try again.\n")
                except ValueError:
                    print("\nError: invalid mark. Try again.\n")
            add_student(student_number, student_surname, student_given_name, unit_mark)
            print("\nStudent record added to the system successfully.")
            input("\nPress enter to continue...")
        elif choice == "2":
            while True:
                search_key = input("Enter student number or name: ")
                
                if is_empty_input(search_key):
                    print("\nError: search keyword cannot be blank. Try again!\n")
                else:
                    break
            
            search_results = search_students(search_key)
            num_results = len(search_results)

            if num_results > 0:
                print(f"\n{num_results} result(s) found.\n")
                print("{:<20} {:<30} {:<10}".format("Student Number", "Student Name", "Unit Mark"))
                print("-" * 65)
                for result in search_results:
                    print("{:<20} {:<30} {:<10}".format(
                        result['student_number'],
                        result['student_given_name']+" "+result['student_surname'],
                        result['unit_mark']
                    ))
                print("-" * 65)
            else:
                print("\nNo students found with matching keyword.")
            input("\nPress enter to continue...")
        elif choice =="3":
            grades_list = ['HD', 'D', 'C', 'P', 'N']
            grade = input("Enter unit grade (HD, D, C, P, N): ").upper()
            
            if grade not in grades_list:
                print(f"\nInvalid grade: {grade}")
            else:
                results = display_students_by_grade(grade)
                num_results = len(results)

                if num_results > 0:
                    print(f"\n{num_results} student(s) achieved a grade of '{grade}'.\n")
                    print("Student Name")
                    print("-" * 30)
                    for student in results:
                        print(f'{student["student_given_name"]} {student["student_surname"]}')
                    print("-" * 30)
                else:
                    print("\nNo student record found.")
            input("\nPress enter to continue...")
        elif choice == "4":
            while True:
                try:
                    student_number = int(input("Enter Student Number: "))
                    break
                except ValueError:
                    print("\nError: invalid student number. Try again!\n")
            
            if delete_student(student_number):
                print("\nStudent record deleted successfully.")
            else:
                print(f"\nStudent record with number '{student_number}' does not exist.")
            
            input("\nPress enter to continue...")
        elif choice == "0":
            print("\nExiting program...\n")
            break
        else:
            input("\nInvalid Choice! Try Again.")

if __name__ == "__main__":
    main()