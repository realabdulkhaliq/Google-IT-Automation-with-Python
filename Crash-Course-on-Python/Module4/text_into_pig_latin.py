# Create a function that turns text into pig latin. 
# Pig latin is a simple text transformation that modifies each word by:
# moving the first character to the end of each word;
# then appending the letters "ay" to the end of each word.
# For example, python ends up as ythonpay.

def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  
  for word in words:
    # Create the pig latin word and add it to the list
    word = word[1:] + word[0] + "ay"
    say += word + " "
    # Turn the list back into a phrase
  return say
    
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"