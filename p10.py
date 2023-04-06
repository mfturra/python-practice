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

# Elegant solution from example
value_int = int(value)

# Join values and convert to integer
x1 = int("%s" % value_int)
x2 = int("%s%s" % (value_int, value_int))
x3 = int("%s%s%s" % (value_int, value_int, value_int))

# Combine values together
calc_val2 = x1 + x2 + x3

# Print calculated output
print("\nComputed value: " + str(calc_val2))
