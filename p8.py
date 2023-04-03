# Acquire color list from user and output first and last colors

# Acquire input from user
raw_colors = input(
    "\nPlease provide us with a list of colors separated by comma's: ")

# Split inputs into a list
colors = raw_colors.split(", ")

# list slicing involves slicing based on the following format: list[initial:end:IndexJump]
# By not including a value for one of the elements, the default becomes first, last, and 1
# colors list starts at colors[0] and steps to colors[last] to output first and last element
color_index = colors[::(len(colors)-1)]

# Output first and last element in an organized string format
print("\nThe first color provided was: " + str(color_index) + "\n")
