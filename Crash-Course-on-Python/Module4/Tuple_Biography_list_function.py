# Fill in the blanks to complete the “biography_list” function. 
# The “biography_list” function reads in a list of tuples “people”, 
# which contains the name, age, and profession of each “person”. 
# Then, prints the sentence "__ is _ years old and works as __.". 
# For example, “biography_list([("Ira", 30, "a Chef")])” 
# should print: “Ira is 30 years old and works as a Chef.” 

def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples. 
    for p in people:

        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"   
        (name, age, profession) = p 


        # Format the required sentence and place the 3 variables 
        # in the correct placeholders using the .format() method.
        print("{} is {} years old and works as {}".format(name, age, profession))



# Call to the function:
biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])


# Click Run to submit code


# Output should match:
# Ira is 30 years old and works as a Chef
# Raj is 35 years old and works as a Lawyer
# Maria is 25 years old and works as an Engineer