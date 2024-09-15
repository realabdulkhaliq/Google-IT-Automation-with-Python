# Consider the following scenario about using Python dictionaries:
# A teacher is using a dictionary to store student grades. 
# The grades are stored as a point value out of 100.  
# Currently, the teacher has a dictionary setup for Term 1 grades and 
# wants to duplicate it for Term 2. The student name keys in the dictionary 
# should stay the same, but the grade values should be reset to 0.

# Complete the “setup_gradebook” function so that input like “{"James": 93, "Felicity": 98, 
# "Barakaa": 80}” will produce a resulting dictionary that contains  “{"James": 0, "Felicity": 0, 
# "Barakaa": 0}”. This function should: 

# accept a dictionary “old_gradebook” variable through the function’s parameters;

# make a copy of the “old_gradebook” dictionary;

# iterate over each key and value pair in the new dictionary;

# replace the value for each key with the number 0;

# return the new dictionary.

def setup_gradebook(old_gradebook):
    # Use a dictionary method to create a new copy of the "old_gradebook".
    new_gradebook = old_gradebook.copy() 
    # Complete the for loop to iterate over the new gradebook. 
    for student in new_gradebook:
        # Use a dictionary operation to reset the grade values to 0.
        new_gradebook[student] = 0
    return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}
