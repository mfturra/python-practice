# Extract output file extension based on filename from user
# Import required libraries
import os

# Acquire user's file name and file extension
user_input = input(
    "Please provide us with your file name (extension included): ")

# splitext separates root name and extension name into separate variables
file_name, file_extension = os.path.splitext(user_input)

# Output file extension
print(file_extension)
