import random

# Gather list of names
names_string = input(
    "Provide me with everyone's names, separated by a comma: ")
names = names_string.split(", ")

# Identify the number of names provided
num_names = len(names)

# Generate a random number from 1 to num_names
tip_id = random.randint(1, num_names)

# Print name based on random number generated
print(f"{names[tip_id]} is going to buy the meal today!")
