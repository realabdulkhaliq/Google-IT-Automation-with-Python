# The datetime module supplies classes for manipulating dates and times, and contains many types, 
# objects, and methods. You've seen some of them used in the dow function, which returns the day 
# of the week for a specific date. We'll use them again in the next_date function, which takes the 
# date_string parameter in the format of "year-month-day", and uses the add_year function to 
# calculate the next year that this date will occur (it's 4 years later for the 29th of February 
# during Leap Year, and 1 year later for all other dates). Then it returns the value in the same 
# format as it receives the date: "year-month-day".

# Can you find the error in the code? Is it in the next_date function or the add_year function? 
# How can you determine if the add_year function returns what it's supposed to? Add debug lines 
# as necessary to find the problems, then fix the code to work as indicated above.  
# 

import datetime
from datetime import date

def add_year(date_obj):
    """Add 1 year to the date unless it's Feb 29 in a leap year, then add 4 years."""
    try:
        # Attempt to add 1 year
        new_date_obj = date_obj.replace(year=date_obj.year + 1)
    except ValueError:
        # This happens if the date is February 29 and the new year is not a leap year
        new_date_obj = date_obj.replace(year=date_obj.year + 4)
    
    return new_date_obj

def next_date(date_string):
    """Convert a date string to a new date string with an updated year."""
    # Convert string to a date object
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    
    # Compute next occurrence of the date
    next_date_obj = add_year(date_obj)
    
    # Convert back to string in "YYYY-MM-DD" format
    next_date_string = next_date_obj.strftime("%Y-%m-%d")
    
    return next_date_string

# Test cases
today = date.today()  # Get today's date
print(next_date(str(today)))  # Should return next year's date

print(next_date("2021-01-01"))  # Should return 2022-01-01
print(next_date("2020-02-29"))  # Should return 2024-02-29
