greeting = 'Hello'
for char in greeting:
	print(char)

print("==========")

for i in range(len(greeting)):
	print(i)

print("==========")

greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1
	
# In any while loop, you can add conditional statements and stop the iteration process early 
# so that the loop does not examine every character.
