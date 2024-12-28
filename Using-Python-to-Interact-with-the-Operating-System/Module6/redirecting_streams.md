cat stdout_example.py
#!/usr/bin/env python3
print("Don't mind me, just a bit of text here...")
./stdout_example.py
#Output: Don't mind me, just a bit of text here...

./stdout_example.py > new_file.txt
cat new_file.txt
#Output: Don't mind me, just a bit of text here...

./stdout_example.py >> new_file.txt
cat new_file.txt
#Output: Don't mind me, just a bit of text here...

#Don't mind me, just a bit of text here...
