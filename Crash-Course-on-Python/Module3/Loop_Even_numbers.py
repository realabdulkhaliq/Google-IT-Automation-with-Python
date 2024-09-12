# This for loop iterates through the numbers 0 to 6. The if statement
# uses the modulo operator to test if the "x" variable is divisible by
# 2. If True, the if statement will print the value of "x" and exit
# back into the for loop for the next iteration of "x". Since no 
# incremental value is specified in the range() parameters, the default
# increment is +1. 

for x in range(7):
    if x % 2 == 0:
        print(x)

# The loop should print 0, 2, 4, 6

# As a list comprehension:
even_numbers = [x for x in range(7) if x % 2 == 0]
print(even_numbers)

# With a list comprehension, you could achieve the same result in a more concise way:
sequence = range(10)
new_list = [x for x in sequence if x % 2 == 0]
print(new_list)