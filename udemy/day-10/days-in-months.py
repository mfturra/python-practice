def is_leap(year):
  """Receive year input and check to see whether it's a leap year or not."""
  # check if year is divisible by 4
  if year % 4 == 0:
    
    # check if year is divisible by 100
    if year % 100 == 0:

      # if year is divisible by 100 and 400 with no remainder then year is a leap year
      if year % 400 == 0:
        # output should be True, producing a confirmation that leap year was found
        return True
      
      # if year is divisible by 100 with no remainder and not by 400 then year is not a leap year
      else:
        # output should be False, producing a confirmation that leap year wasn't found
        return False

    else:
      # output should be True, producing a confirmation that leap year was found
      return True

  else:
    # output should be False, producing a confirmation that leap year wasn't found
    return False
  
def days_in_month(year, month):
    """Receive input of year and month. Proceed to use is_leap to check if year is a
    leap year. If so, output the num of days in month of leap year based on list. If year 
    input is not of a leap year, then the output of the number of days should change 
    accordingly."""

    # use is_leap function to check if input year is a leap year
    if is_leap(year):
        # num days for leap years
        leap_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # select month entry in respective list
        days_for_month = leap_month_days[month - 1]
        
        # return day in month for leap year
        return days_for_month

    else:
        # standard num days for non-leap years
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
        
        # select month entry in respective list
        days_for_month = month_days[month - 1]

        # return day in month for non-leap year 
        return days_for_month
  
# gather inputs for function usage
year = int(input("\nEnter the year that you want to check: ")) # Enter a year
month = int(input("Enter the month that you want to check: ")) # Enter a month

# utilize multiple functions to check month days based on whether input is leap year or not
days = days_in_month(year, month)

# output num of days in month of leap or non-leap year
print(days)