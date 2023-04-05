# Acquire int from user and conduct computation
# Prompt user for input
value = (input("Please provide us with an integer: "))

# Modify values to calculable totals
first_value = int(value)
second_value = int(value+value)
third_value = int(value+value+value)
calc_val = first_value + second_value + third_value
#cal_val = str(value + value**2 + value**3)

# Print calculated output
print("\nComputed value: " + str(calc_val))
