# Step 1: Create dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

# Step 2: Ask user for student name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")