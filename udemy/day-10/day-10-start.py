# Create a function with outputs

def format_name(first_name, last_name):
    # return statement workflow when no names are provided
    if first_name == "" or last_name == "":
        return "Valid inputs were not provided"

    formatted_fname = first_name.title()
    formatted_lname = last_name.title()

    # return output using print
    # print(f"{formatted_fname} {formatted_lname}")

    #return output using return statement
    return f"\n{formatted_fname} {formatted_lname}"

# gather inputs from user
first_name = input("\nWhat's the first name?:\n")
last_name = input("What's the last name?:\n")

formatted_string = format_name(first_name, last_name)

print(formatted_string)
# output = f_name