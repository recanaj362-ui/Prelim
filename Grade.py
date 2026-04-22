
# Student Grade Management System
# Prelim Exam - 2nd Year IT

def get_letter_grade(grade):
    # Logic to convert numerical score to a letter grade
    if grade >= 90:
        return "A"
    elif grade >= 85:
        return "B"
    elif grade >= 75:
        return "C"
    elif grade >= 70:
        return "D"
    else:
        return "F"

def check_pass_or_fail(grade):
    # Logic to determine if the student passed or failed
    if grade >= 60:
        return "CONGRATSTIOLATIONS YOU ARE PASSED"
    else:
        return "FAILED"

def save_student_record(first_name, last_name, grade, letter_grade, status):
    # Logic to record the data permanently
    # Using 'a' mode (append) so it doesn't overwrite existing records
    with open('grades_record.txt', 'a') as file:
        file.write(f"Name: {first_name} {last_name} | Grade: {grade} | Letter: {letter_grade} | Status: {status}\n")

while True:
    # INPUT SECTION: Collect names and numerical grade
    print("\n--- Enter Student Details ---")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    
    try:
        grade = float(input("Enter Numerical Grade: "))
    except ValueError:
        print("Invalid input. Please enter a number for the grade.")
        continue

    # PROCESSING SECTION: Call the logic functions above
    letter_grade = get_letter_grade(grade)
    status = check_pass_or_fail(grade)

    # OUTPUT SECTION: Print results and commit to file
    print(f"\nResult for {first_name} {last_name}:")
    print(f"Letter Grade: {letter_grade}")
    print(f"Status: {status}")
    
    save_student_record(first_name, last_name, grade, letter_grade, status)
    print("Record saved successfully!")

    choice = input("\nDo you want to add another student? (yes/no): ").lower()
    if choice != "yes":
        # EXIT SECTION
        print("Exiting system. Goodbye!")
        break