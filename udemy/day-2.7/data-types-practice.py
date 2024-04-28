
# problem #5
output_data_types_prac = False
if output_data_types_prac:
    # Ingest a number with two digits
    two_digit_number = input('\nInput two numbers: ') # state: str

    print(f'The combination of the number that you provided is: {int(two_digit_number[0]) + int(two_digit_number[1])}\n')

# problem #6
BMI_calc = False
if BMI_calc:
    height = input('\nWhat is your height in meters: ')
    weight = input('What is your weight in kilograms: ')

    # BMI calculation
    BMI_value = int(round(int(weight)/ ((float(height))**2), 0))

    print(f'\nYour BMI value is: {BMI_value}')

# problem #22, day 9
grading_program = True
if grading_program:
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99, 
        "Draco": 74,
        "Neville": 62,
        }
    # assign empty dict
    student_grades = {}

    # iterate through student_scores and store respective values with grade in student_grades
    for keys in student_scores:
        # Scores 90 - 100: Grade = "Outstanding"
        if student_scores[keys] >= 91:
            student_grades[keys] = 'Outstanding'
        
        # Scores 81 - 90: Grade = "Exceeds Expectations"
        elif student_scores[keys] < 91 and student_scores[keys] >= 81:
            student_grades[keys] = 'Exceeds Expectations'
        
        # Scores 71 - 80: Grade = "Acceptable"
        elif student_scores[keys] <= 80 and student_scores[keys] >= 71:
            student_grades[keys] = 'Acceptable'
        
        # Scores 70 or lower: Grade = "Fail"
        elif student_scores[keys] <= 70:
            student_grades[keys] = 'Fail'
        else:
            continue

    print(f'{student_grades}')

