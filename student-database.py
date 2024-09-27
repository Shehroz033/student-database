def manage_student_database():
    students = []  # List to store student tuples
    student_id = 1  # Start student ID from 1
    
    while True:
        name = input("Enter student name (or type 'stop' to finish): ").strip()
        if name.lower() == 'stop':
            break
        # Check for duplicate names
        if any(student[1] == name for student in students):
            print(f"Student '{name}' already exists in the database. Please enter a different name.")
        else:
            students.append((student_id, name))  # Add student tuple (ID, Name) to list
            student_id += 1  # Increment student ID
    
    # Display the complete list of student tuples
    print("\nComplete List of Students (ID, Name):")
    for student in students:
        print(student)
    
    # Display each student's ID and name individually
    print("\nStudent Details:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")
    
    # Total number of students
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")
    
    if total_students > 0:
        # Calculate total length of all student names combined
        total_name_length = sum(len(student[1]) for student in students)
        print(f"Total length of all student names combined: {total_name_length}")
        
        # Identify the student with the longest and shortest name
        longest_name_student = max(students, key=lambda student: len(student[1]))
        shortest_name_student = min(students, key=lambda student: len(student[1]))
        
        print(f"Student with the longest name: {longest_name_student[1]} (ID: {longest_name_student[0]})")
        print(f"Student with the shortest name: {shortest_name_student[1]} (ID: {shortest_name_student[0]})")
    else:
        print("No students in the database.")
    
# Call the function to start the program
manage_student_database()
