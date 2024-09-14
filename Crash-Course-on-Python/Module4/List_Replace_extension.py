# Fill in the blank using a for loop. With the given list of "filenames", 
# this code should rename all files with the extension .hpp to the extension .h. 
# The code  should then generate a new list called "new_filenames" that contains the 
# file names with the new extension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        
        new_filenames.append(filename.replace("hpp","h"))
    else:
        new_filenames.append(filename)


print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]