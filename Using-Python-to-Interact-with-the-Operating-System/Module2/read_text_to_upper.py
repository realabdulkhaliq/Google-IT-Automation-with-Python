with open("spider.txt") as file:
    for line in file:
        print(line.upper())


# Python reads the file line by line, the line variable will always have a new line character 
# at the end. In other words, the newline character is not removed when calling read line. 
# When we ask Python to print the line, the print function adds another new line character, 
# creating an empty line.


with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())