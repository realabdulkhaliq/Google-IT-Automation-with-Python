# The check_time() function checks for the time format of a 12-hour clock, as follows: the hour 
# is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, 
# then an optional space, and then AM or PM, in upper or lower case. Fill in the regular e
# xpression to do that. How many of the concepts that you just learned can you use here?

import re
def check_time(text):
    pattern = r"^(1[0-2]|[1-9]):[0-5][0-9]\s?(AM|PM|am|pm)$"
    result = re.search(pattern, text)
    return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False

# ^ asserts the start of the string.
# (1[0-2]|[1-9]) matches the hour part. It allows numbers from 1 to 12:
# 1[0-2] matches 10, 11, or 12.
# [1-9] matches any number from 1 to 9 without a leading zero.
# : matches the colon separator.
# [0-5][0-9] matches the minutes part, from 00 to 59.
# \s? optionally matches a space character (\s matches whitespace; ? makes it optional).
# (AM|PM|am|pm) matches "AM", "PM", "am", or "pm".
# $ asserts the end of the string.