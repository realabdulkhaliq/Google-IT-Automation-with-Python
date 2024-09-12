def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(6): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(x): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


rows_asterisks(5)
# Should print the asterisk rows shown above
