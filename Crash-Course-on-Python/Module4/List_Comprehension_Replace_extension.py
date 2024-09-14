# Fill in the blank using a list comprehension. With the given list of "filenames", 
# this code should rename all files with the extension .hpp to the extension .h. 
# The code function should then generate a new list called "new_filenames" that 
# contains the filenames with the new extension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_filenames = [filename.replace(".hpp", ".h") for filename in filenames]  # Start your code here


print(new_filenames) 
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]