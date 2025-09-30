def get_student_details():
    """
    Collects student details from the user and displays them.
    """
    print("--- Enter Student Details ---")
    name = input("Enter student's name: ")
    roll_number = input("Enter student's roll number: ")
    grade = input("Enter student's grade: ")
    major = input("Enter student's major: ")
    college = input("Enter student's college name: ")
    
    print("\n--- Student Details ---")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Grade: {grade}")
    print(f"Major: {major}")
    print(f"College: {college}")
    
# Call the function to execute the program
get_student_details()

