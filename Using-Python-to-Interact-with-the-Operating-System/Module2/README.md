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

Resources for more information
More information about reading and writing files can be found in Built-in Functions:

https://docs.python.org/3/library/functions.html#open

There are several ways to manage files and directories in Python. One way is to use low-level functions in the OS and SYS modules that closely mimic standard Linux commands. Another way is to utilize the Pathlib module, which provides an object-oriented interface to working with the file systems.

Resources for more information
More information about files and directories can be found in several resources provided below:

https://docs.python.org/3/library/os.html

https://docs.python.org/3/library/os.path.html

https://en.wikipedia.org/wiki/Unix_time

### Module contents

The .csv module is a built-in Python functionality used to read and work with .csv files. Let’s look at how the .csv module defines some of these functions:

csv.reader This function returns a reader object that iterates over lines in the .csv file.

csv.writer This function returns a writer object that’s responsible for converting the user’s data into delimited strings on the given file-like object.

class csv.DictReader This function creates an object that functions as a regular reader but maps the information in each row to a dictionary whose keys are given by the optional fieldname parameters.

Dialects and formatting parameters
Dialects are rules that define how a .csv file is structured, and parameters are formed to control the behavior of the .csv reader and writer and live within dialects. The following features are supported by dialects:

Dialect.delimiter This attribute is a one-character string used to separate fields and defaults to a comma.

Dialect.quotechar This attribute is a one-character string used to quote fields containing special characters and defaults to ‘ ‘’ ‘.

Dialect.strict This attribute’s default is False, but when True, exception csv.Error will be raised if an error is detected.

Reader objects
A reader object contains the following public methods and attributes:

csvreader._next_() This method returns the next row of the reader’s iterable object as a list or a dictionary, parsed properly to the current dialect. Typically, you would call this next(reader).

csvreader.dialect This attribute is a read-only description of the dialect in use by the parser.

Writer objects
Writer objects provide you the capability to write data to a .csv file. Let’s look at a couple of public methods and attributes for writer objects:

csvwriter.writerows(rows) This method writes all elements in rows to the writer’s file object and formats following the current dialect.

csvwriter.dialect This attribute is a read-only description of the dialect being used by the writer.

Key takeaways
If you haven’t worked with .csv files yet, it’s only a matter of time. Become familiar with the .csv module’s reader and writer objects to work more efficiently with .csv files. The modules, features, and attributes in this reading are only some of the commands that can be used while working with .csv files.

Resources for more information
This [document](https://docs.python.org/3/library/csv.html) provides additional information on how to read and write functions using .csv files.

This[document](https://realpython.com/python-csv/) provides additional information on what a .csv file is, how to parse .csv files with Python’s built-in .csv library, and how to parse .csv files with the pandas library.

### Terms and definitions from Course 2, Module 2

Absolute path: A full path to the resource in the file system

Comma separated values (CSV): A very common data format used to store data as segment of text separated by commas

Dialects: Rules that define how a CSV file is structured

File systems: Methods and structures used to organize and control how data is stored and accessed

Mode: The format controlling what you can do with a recently opened file

Qwiklabs: An online learning environment or virtual machine to simulate real-world scenarios

Reader objects: Object that represents an element or entity within a scene that needs to be rendered to the screen

Relative path: A portion of a path to show where the resource is located in relation to the current working directory

Virtual machine (VM): A computer simulated through software

Writer objects: The capability to write data to a CSV file
