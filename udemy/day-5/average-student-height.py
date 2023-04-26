# Preliminary code
student_heights = input(
    "Input a list of student heights (with a space and comma separating each): ").split(', ')
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)

# Set global variables to be used later
heights_total = 0
num_students = 0


# Considering the length of the list do something
for students in student_heights:
    # Add up iteratively the student height to heights_total variable
    heights_total += students

    # Iteratively add to the num_students based on loop index location
    num_students += 1

# Calculate average height based on number of students
print(
    f'\nThe average height of all inputted student heights is: {round(heights_total/num_students)}\n')
