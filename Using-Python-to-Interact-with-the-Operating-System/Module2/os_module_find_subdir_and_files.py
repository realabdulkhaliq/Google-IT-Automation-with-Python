import os
dir = "website"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name) # join files with its directory
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))


# Output:
# website\index.html is a file
# website\input.txt is a file