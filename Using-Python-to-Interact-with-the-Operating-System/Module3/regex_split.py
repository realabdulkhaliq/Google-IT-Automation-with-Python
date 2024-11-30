# We want to split a piece of text by either the word "a" or "the", as implemented 
# in the following code. What is the resulting split list?

import re
re.split(r"the|a", "One sentence. Another one? And the last one!")

# This regular expression uses "the" and "a" as delimiters, no matter where they are 
# in the text, even in the middle of other words like "Another" and "last".