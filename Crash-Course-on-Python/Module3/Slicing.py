string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”

# An optional way to slice an index is by the stride argument, indicated by using a double colon.

print(string1[0::2])  # Prints “Getns atlns”
print(string1[::-1])  # Prints “sgnilhtraE ,sgniteerG”