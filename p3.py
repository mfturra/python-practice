from datetime import datetime

# Print date
'''today = date.today()
print("Today's Date: ", today)'''

# Print current date and time
# Pull current date and time using library
current = datetime.now()

# Format date and time output
dt_string = current.strftime("%Y/%m/%d %H:%M:%S")

# Print output
print("Date and Time =", dt_string)
