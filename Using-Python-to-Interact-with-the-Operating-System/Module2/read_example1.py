file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()

with open("spider.txt") as file:
    print(file.readline())

# The readline() method reads a single line from the current position, 
# the read() method reads from the current position until the end of the file.

# Using a "with" block is a good way to open and work on a single file then have the 
# file automatically closed at the end of the block.