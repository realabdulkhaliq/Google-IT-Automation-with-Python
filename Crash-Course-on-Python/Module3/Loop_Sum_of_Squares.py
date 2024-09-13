# Write a Python function called sum_of_squares(n) that returns the sum of the squares 
# of all numbers from 1 to n. Use a for loop to iterate through the numbers.

def sum_of_squares(n):
    total = 0
    for i in range(1, n+1):
        total += i**2
        print(total)
    return total

print(sum_of_squares(4))