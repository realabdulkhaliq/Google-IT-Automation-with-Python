# 1. Write a recursive function to calculate the factorial of a number.
def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n-1)
    
print(factorial1(4))
    
def factorial2(n):
  if n < 2:
    return 1
  return n * factorial2(n-1)
print(factorial2(4))

def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

factorial(4)

def factorial3(n):
    result = n
    start = n
    n -= 1
    while n>0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n -= 1 # Decrement the appropriate variable by -1
    return result


print(factorial3(3)) # Should print 6
print(factorial3(9)) # Should print 362880
print(factorial3(1)) # Should print 1