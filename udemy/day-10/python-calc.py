# TO DO: Create functions that simulate addition, subtraction, and multiplication
# addition func
def add(n1, n2):
    '''Receives two inputs and adds them'''
    # output values using return function
    return n1 + n2

# subtraction func
def subtract(n1, n2):
    '''Receives two inputs and subtracts them'''
    # output values using return function
    return n1 - n2

# multiplication func
def multiply(n1, n2):
    '''Receives two inputs and multiplies them'''
    # output values using return function
    return n1 * n2

# divide func
def divide(n1, n2):
    '''Receives two inputs and divides them'''
    # output values using return function
    return n1 / n2


# TO DO: prompt user for numbers
user_n1 = float(input("\nWhat's the first number?: "))


# TO DO: Build function that uses dictionary operations to perform calculations. Starting with multiply
# check if operation is in operation_dict
def operation_matrix(input1):
    '''Use users numerical values and operation of choice along with the operational dictionary to
    perform the necessary calculations. Print output of operation so that the user can visualize the arithmetic that's taking place programmatically.'''
    
    # Store functions into dictionary based on specific operators
    operation_dict = {'+': add,
                      '-': subtract,
                      '*': multiply,
                      '/': divide}

    # Output available operator options
    input_operation_opts = "\n+ \n- \n* \n/"
    print(input_operation_opts)

    # Prompt user for additional operations and values
    user_operation = input("Pick an operation: ")
    input2 = float(input("What's the second number?: "))
    
    if user_operation in operation_dict:
        # pull function from dict
        operation_choice = operation_dict[user_operation](input1, input2)

        # operation found in dict should be used to modify user inputs
        print(f"{input1} {user_operation} {input2} = {operation_choice}\n")
        return operation_choice

    else:
        print("Your operator selection isn't an option. Please select one of the available options")

# store output into operational_output var
operational_output = operation_matrix(user_n1)

# TO DO: Prompt user for more calculations
cont_operation_status = str(input(f"Type 'y' to continue calculating with {operational_output}, or type 'n' to start a new calculation: "))

# if more calcs requested, proceed with another round of questions
if cont_operation_status == 'y':
    new_output = operation_matrix(operational_output)
    
    cont_operation_status = str(input(f"Type 'y' to continue calculating with {new_output}, or type 'n' to start a new calculation: "))

elif cont_operation_status == 'n':
    user_n1 = float(input("\nWhat's the first number?: "))

    operational_output = operation_matrix(user_n1)
    

# # TO DO: Build workflow that, depending on the operator picked, it'll output a modified value 
# if user_operation == "+":
#     input_mod = add

#     # store value of operation in new calc_output
#     calc_output = input_mod(user_n1, user_n2)
    
#     # output operation taking place based on inputs
#     print(f"{user_n1} + {user_n2} = {calc_output}\n")

# elif user_operation == "-":
#     input_mod = subtract

#     # store value of operation in new calc_output
#     calc_output = input_mod(user_n1, user_n2)

#     # output operation taking place based on inputs
#     print(f"{user_n1} - {user_n2} = {calc_output}\n")


# elif operation_dict == 'x':
#     input_mod = multiply

#     # store value of operation in new calc_output
#     calc_output = input_mod(user_n1, user_n2)

#     # output operation taking place based on inputs
#     print(f"{user_n1} * {user_n2} = {calc_output}\n")


# elif user_operation == '/':
#     input_mod = divide

#     # store value of operation in new calc_output
#     calc_output = input_mod(user_n1, user_n2)

#     # output operation taking place based on inputs
#     print(f"{user_n1} * {user_n2} = {calc_output}\n")


