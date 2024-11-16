# Managing Files with Python

In this module, you’ll learn about reading and writing to files and the commands that will enable you to do this. We’ll learn the importance of managing files and how we can navigate through different directories. You’ll understand how to work with files and how there is a layer of abstraction between Python and the operating system. Finally, we’ll dive into learning about CSV files and how to best utilize them.
Learning Objectives
Read, write, and iterate through files
Manage files by moving, deleting, and renaming files
Create and navigate through directories
Define what CSV files are and read from them
Write and make edits to CSV files within directories

Mode
The mode argument is optional, and it specifies the mode in which the file is opened. If omitted, it defaults to ”r” and that means opening for reading in text mode. The common modes include:

“r” open for reading (default)

“w” open for writing, truncating the file first

“x” open for exclusive creation, failing if the file already exists

“a” open for writing, appending to the end of the file if it exists

“+” open for both reading and writing

Attempting to write to a file opened for read (“r”) will cause a runtime error.
