# Range Key takeaways

The roles of the range(start, stop, step) function parameters are:

- Start - Beginning of range

  - value included in range

  - default = 0

- Stop - End of range

  - value excluded from range (to include, use stop+1)

  - no default

  - must provide the ending index number

- Step - Incremental value

  - default = 1

### `range(x,y,z)`

- x = Start - Starting index position of the range

  - Default index position is 0.

  - The starting index position is included in the range.

  - Example syntax: `range(2, y, z)` or `range(x+3, y, z)`

- y = Stop - Ending index position of range

  - No default index position. Must include the ending index position in the range() parameters.

  - Example syntax: `range(y)`

  - The value of the ending index position is excluded from the range.

  - To include the ending index number, use the expression: y+1 (index + 1)

  - Example syntax: `range(x, y+1, z)`

  - Alternatively, if y = 10, you can write: `range(x, 11, z)`

- z = Step - Incremental value

## Resources for more information

[Python range() function](https://www.geeksforgeeks.org/python-range-function/)

- This site provides some helpful visualizations for the range index positions. It also offers multiple for x in range() examples and practice exercises.

For additional Python practice, the following links will take you to several popular online interpreters and codepads:

[Welcome to Python](https://www.python.org/shell/)

[Online Python Interpreter](https://www.onlinegdb.com/online_python_interpreter)

[Create a new Repl](https://repl.it/languages/python3)

[Online Python-3 Compiler (Interpreter)](https://www.tutorialspoint.com/execute_python3_online.php)

[Compile Python 3 Online](https://rextester.com/l/python3_online_compiler)

[Your Python Trinket](https://trinket.io/python3)

## Additional advanced string loop techniques

There are additional ways to loop over a string in Python that you should learn, practice, and master. These additional looping techniques include the generator functions, `map()`, and `zip()`. The `map()` and `zip()` functions are extremely powerful string manipulation tools that demonstrate functional programming concepts. To learn more about these advanced techniques, see these resources:

- [Python - map() function](https://www.tutorialsteacher.com/python/python-map-function)

- [Python zip() method](https://www.tutorialsteacher.com/python/zip-method)

Pro Tip: Looping over multiple strings at once can push the limits of for loops. Because of this, it’s important to be aware of other alternatives to simplify a for or while loop.
