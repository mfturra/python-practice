# Preliminary Code
student_scores = input(
    'Input a list of student scores (separating values with a space) \n').split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Compare scores with one another to evaluate which are greater and print to terminal
max_score = 0
for score in student_scores:
    # current_score = score
    # max_score = score
    if score > max_score:
        max_score = score
    else:
        pass
print(f"The highest score in the class is {max_score}")
