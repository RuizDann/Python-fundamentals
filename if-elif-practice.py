# Take an user's input and assign it to a variable named "student_grade_string"

# The user input comes in as a string so we have to cast it to a Int to a variable named "student_grade_int"

# Create an If statement with the appropriate Elif and Else statement for the following grading system.

"""
A : 90 - 100
B : 80 - 89
C : 70 - 79
D : 60 - 69
F : 0 - 59
"""

# Within each "block" print out the appropriate letter grade.

studentGradeString = input("Enter your grade: ")

studentGradeInt = int(studentGradeString)

if (studentGradeInt >= 90):
    print("A")
elif (studentGradeInt >= 80):
    print("B")
elif (studentGradeInt >= 70):
    print("C")
elif (studentGradeInt >= 60):
    print("D")
else:
    print("F")