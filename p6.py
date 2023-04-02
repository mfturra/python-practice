# Receive a comma-separated inputs and generate a list and tuple
#  Accept input from user
raw_string = input("Please provide us with a list of comma-separated values: ")

# Convert string into list of values
user_list = raw_string.split(", ")

# Print values in list and tuple format
print("List: ", user_list)
print("Tuple: ", tuple(user_list))
