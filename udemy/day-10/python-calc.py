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

def master_calculator():
    '''Use users numerical values and operation of choice along with the operational dictionary to
        perform the necessary calculations. Print output of operation so that the user can visualize the arithmetic that's taking place programmatically.'''
    accumulate_val = True

    # Store functions into dictionary based on specific operators
    operation_dict = {'+': add,
                    '-': subtract,
                    '*': multiply,
                    '/': divide}
    # request first input value
    input1 = float(input("\nWhat's the first number?: "))

    # continue calculating value as long as the user wants to accumulate values
    while accumulate_val:

        # cycle through all operator options in dict
        for symbol in operation_dict:
            # output only available operators to user 
            print(symbol)

        # Prompt user for additional operations and values
        user_operation = input("Pick an operation: ")
        input2 = float(input("What's the second number?: "))
        
        # check if operation is in operation_dict
        if user_operation in operation_dict:
            # pull function from dict and pass respective inputs to finalize calc
            operation_answer = operation_dict[user_operation](input1, input2)

            # produce output of calculation to user  
            print(f"{input1} {user_operation} {input2} = {operation_answer}\n")
            
            # if more calcs requested, proceed with another round of questions
            next_choice = input(f"Type 'y' to continue calculating with {operation_answer}, or type 'n' to start a new calculation: ")

            if next_choice == 'y':
                input1 = operation_answer

            else:
                # if reset of values is requested, then reset first input number
                accumulate_val = False

                # start func from start user wants to reset calc
                master_calculator()

        else:
            # error track in case user provides operator that isn't available
            print("Your operator selection isn't an option. Please select one of the available options.")

# initiate master_calculator function for user to input respective values
master_calculator()