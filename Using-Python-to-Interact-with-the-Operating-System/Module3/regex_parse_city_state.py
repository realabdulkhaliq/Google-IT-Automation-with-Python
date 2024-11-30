# You are working with a dataset on customer orders. This dataset includes a 
# field that contains information on both city and state. You would like to separate 
# this field into two fields, a city field and a state field. In the current field, 
# city and state are separated by either a comma, or a period. Complete the function 
# parse_city_state() to split city and state into two strings and return only the state.
import re

def parse_city_state(text):
 pattern = r"[,.]" #enter the regex pattern here
 result = re.split(pattern, text) #enter the re method  here
 if len(result) != 2:
  return ""
 return result[1] #return the correct capturing group


print(parse_city_state("Hamilton, MN")) # should return MN
print(parse_city_state("Albuquerque, New Mexico")) # should return New Mexico
print(parse_city_state("Portland. Oregon")) # should return Oregon