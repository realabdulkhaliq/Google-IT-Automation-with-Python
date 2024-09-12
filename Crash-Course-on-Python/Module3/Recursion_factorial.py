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