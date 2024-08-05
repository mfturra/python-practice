def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
    # check if input year is a leap year
    if is_leap(year):
        # num days for leap years
        leap_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # return day in month for leap year
        days_for_month = leap_month_days[month - 1]
        return days_for_month

    else:
        # standard num days for non-leap years
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
        
        # return day in month for non-leap year 
        days_for_month = month_days[month - 1]
        return days_for_month
  
  
#🚨 Do NOT change any of the code below 
year = int(input("\nEnter the year that you want to check: ")) # Enter a year
month = int(input("Enter the month that you want to check: ")) # Enter a month
days = days_in_month(year, month)
print(days)