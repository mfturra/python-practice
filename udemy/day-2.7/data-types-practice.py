
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
grading_program = False
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


# problem #23, day 9
dict_in_list = True
if dict_in_list:
    country = input('Please name the country that you visited: ') # Add country name
    visits = int(input('Please input the number of places that you visited: ')) # Number of visits
    list_of_cities = eval(input('Please list out the number of cities that you visited separating it with a comma: ')) # create list from formatted string

    travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
    ]

    def add_new_country(country, times_visits, cities_visited):
        extended_trip = {}
        extended_trip = {
            'country': country,
            'visits': times_visits,
            'cities': cities_visited,
        }

        # Modify dictionary by adding new country's entries 
        travel_log.append(extended_trip)

    # function output
    add_new_country(country, visits, list_of_cities)
    print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
    print(f"My favorite cities were {travel_log[2]['cities'][0]}.")