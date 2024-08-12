def is_leap_year(year):
    """Take input year and doing multiple checks, evaluate whether it qualifies as a 
    leap year or not. The functions output states whether the input is a leap year or not."""
    
    # check if year input is divisible by 4
    if year % 4 == 0:
        
        # check if year input is divisible by 100
        if year % 100 == 0:

            # check if year input is divisible by 400
            if year % 400 == 0:
                return True
            
            # if year not divisible by 400 then not leap year
            else:
                return False
        
        return True        
        
# gather input from user
year_check = int(input("Please provide me with a year to check: "))

# use is_leap_year to eval if year_check is a leap year
if is_leap_year(year_check):
    print("You found a leap year!")
else:
    print("Your year is not a leap year")
