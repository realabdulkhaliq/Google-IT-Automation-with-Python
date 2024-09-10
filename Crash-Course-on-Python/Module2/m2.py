#1
print("2 + 2 = " + str(2 + 2))

#2
bill = 47.28 # Assign "bill" variable with bill amount
tip = bill * 0.15 # Multiply by stated tip rate 
total = bill + tip # Sum the "total" of the "bill" and "tip"
share = total/2 # Divide "total" by number of friends dining
print("Each person needs to pay:" + str(share)) # Enter the required string and "share" 
# Hint: Remember to convert incompatible data types


#3
month = "September"
print("Investigate failed login attempts during", month, "if more than", 100)
month = "October"
print("Investigate failed login attempts during" + month + "if more than" + 100)
# error due to + above example is fine, 100 is not a string 100 needs to be converted to a string
print("Investigate failed login attempts during" + month + "if more than" + str(100)) # correct way to convert 100 to a string


#4
print(1 < "1") # TypeError: '<' not supported between instances of 'int' and 'str'
print(1 == "1") # False
print(1 > "1") # False