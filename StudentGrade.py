
students = {}

while True:
    print("\n--- Student Grade Manager ---")
    print("1. Add Student")
    print("2. Update Student Grade")
    print("3. Print All Students")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        students[name] = grade
        print(f"{name} added successfully.")

    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated.")
        else:
            print("Student not found.")

    elif choice == '3':
        if not students:
            print("No student records found.")
        else:
            print("\nStudent Grades:")
            for name, grade in students.items():
                print(f"{name} : {grade}")

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
~                                                     
