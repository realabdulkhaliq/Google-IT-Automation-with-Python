# The function accepts two parameters: a start year and an end year
def list_years(start, end):
# It returns a list comprehension that creates a list of years in a for
# loop using a range from the start year to the end year (inclusive of 
# the upper range year, using end+1).
  return [year for year in range(start, end+1)]

# Call the list_years() function with two parameters.
print(list_years(1972, 1975)) 
# Should print [1972, 1973, 1974, 1975]
