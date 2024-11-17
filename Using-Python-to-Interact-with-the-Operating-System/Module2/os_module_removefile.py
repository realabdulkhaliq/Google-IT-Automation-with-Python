import os
os.remove("demofile.txt")

# It remove/delete the file.
# If we try to remove the file that doesn't exist, the function will raise an error.


os.rename("old_name.txt", "new_name.txt")
os.path.exists("demofile.txt")

os.path.getsize("spider.txt")
#This code will provide the file size

os.path.abspath("spider.txt")
#This code takes the file name and turns it into an absolute path