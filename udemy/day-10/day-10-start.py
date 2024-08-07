# TASK
# 1. Create a function with outputs and print the output

def format_name(first_name, last_name):
    """Modify the first and last name inputs to camel case
    independent of case structure that was provided."""

    # error handling workflow when no names are provided
    if first_name == "" or last_name == "":
        return "Valid inputs were not provided"

    # format inputs to camel case
    formatted_fname = first_name.title()
    formatted_lname = last_name.title()

    # produce output using print
    # print(f"{formatted_fname} {formatted_lname}")

    # produce output using return statement
    return f"\n{formatted_fname} {formatted_lname}"

# gather inputs from user
first_name = input("\nWhat's the first name?:\n")
last_name = input("What's the last name?:\n")

# store output of function into a var
formatted_string = format_name(first_name, last_name)

# print function variable output
print(formatted_string)
