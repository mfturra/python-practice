# Utilize internal library to output current date and time.
# Import necessary libraries
from datetime import datetime

'''# Version 1: Print date
today = date.today()
print("Today's Date: ", today)'''

# Version 2: Pull current date and time using library
current = datetime.now()

# Format date and time output
dt_string = current.strftime("%Y/%m/%d %H:%M:%S")

# Print output
print("Date and Time =", dt_string)
