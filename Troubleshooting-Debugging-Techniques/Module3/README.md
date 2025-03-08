# Module 3

## Blue screen of death (BSoD)

A common disruption in computing systems is the kernel panic in Mac OS, also known as the notorious "Blue Screen of Death" (BSoD) in Windows, both of which require restarting the computer. Although rare, analyzing these occurrences is essential for uncovering OS issues. BSoDs are usually caused by hardware glitches, problematic drivers, or abrupt process terminations. These failure screens display error codes, memory locations, and technical insights related to the crash.

## Reading system logs

System logs are crucial for understanding and resolving issues across multiple operating systems. Whether you're using a Mac, Linux, or another system, delving into these logs can yield valuable insights. Analyzing logs is critical for identifying system errors and crashes on Windows computers. The Windows logs such as System and Application carefully record data retrieval events, providing insight into software, hardware, and user interaction.

### Mac System Logs

Mac system logs provide insights into system operations. By using the Console app, you can capture error messages, warnings, and interactions between hardware and software. These logs are especially useful when investigating system behavior.

### Linux System Logs

Linux system logs offer insights into troubleshooting. They give detailed information about the Linux environment, such as errors and hardware-software interactions. Using command-line utilities, you can access these logs to identify unusual behavior patterns. These logs provide a holistic overview of system performance.

## Process Monitor

Monitoring tools like Process Monitor in Windows provide real-time visibility into file system actions, registry changes, and process behavior. With features from legacy tools such as Regmon and Filemon, Process Monitor captures input/output parameters, uses non-destructive filtering, identifies root causes, and compiles comprehensive process data. This includes details such as image paths, commands, user information, and session IDs. The tool offers customizable columns, flexible filters, and scalable logging to enhance event management. Tooltips provide quick access to log files and reveal process relationships. It also records boot-time operations for comprehensive tracking, troubleshooting, malware detection, and system activity analysis.

## Linux strace command

You can use a Linux strace command to trace system calls and signals. It aids in debugging and diagnostics by analyzing application and process behavior. It captures system calls, pinpoints issues, optimizes code, and enhances system performance. You use strace by entering the program's name and any arguments at the command line. This tool logs detailed system call information, enabling you to analyze bottlenecks, unintended behaviors, and misconfigurations. The strace command contributes to a better understanding of OS and application interactions, ultimately leading to efficient software development and effective issue resolution.

## Tracing system calls

Tracing system calls on Linux is useful for identifying security risks and tracing system calls, which reveal the intricate interactions between processes and operating systems. You can trace a Linux system call using the ptrace API and the strace command, and you can trace a Mac OS X system call using the dtrace system. Windows uses the GUI tool Process Monitor, and additional projects enhance system call tracing. Tools like Logger, LogView, and NtTrace leverage Microsoft's Event Tracing for Windows (ETW) capabilities. Across operating systems, tracing system calls remains pivotal for development and monitoring, anchoring system analysis and optimization.

## Debugging with print

The print statement helps you figure out what is going on with your code. You can use the print command to send messages to the screen as your program executes to help you find out how far it’s getting before it crashes. Or you can print out the value of certain variables as the program runs, which might help explain what is going wrong. If your code has a loop that doesn’t seem to be executing correctly, try adding a print statement at the top of the loop. Print out the loop invariant and any other local variables that might help you figure out what’s going on.

## Debugging with assert

A developer’s worst nightmare is to spend hours and hours developing and writing code for a program, and right before they deploy it, the developer discovers multiple bugs and errors. Instead of waiting until the last minute to check the correctness of your code, you should test it and check it throughout the development and writing process.

### What are assertions?

Assertions are logical tests that developers use as a sanity check when writing code. In Python, you use an assert statement to write these sanity checks. When you write an assert statement, it is important to write it with one thing in mind: The condition you include with the assert statement should always be true. If the condition is false, you can use this information as a main indicator that the program has a bug. If the assert statement is false, it will automatically terminate the execution of the program and will display an error message. At this point, you can correct or fix the bug before continuing to write code to ensure you don’t introduce any additional bugs.

## Try and catch debugging

In Python, the “try and catch” mechanism is implemented using try and except blocks. When you anticipate that a certain segment of your code might produce an error, you enclose it within a try block. Following this block, one or more except blocks can be defined to catch specific exceptions.

### Why use try and catch debugging

Wrapping potentially problematic code using try and except blocks can help you debug in a number of ways:

Identify problems: By wrapping potentially problematic code in a try block, you can catch and print exceptions, helping to pinpoint which sections of your code are problematic.

Gain insight: When an exception is caught, you can access its message and type, providing insights into the nature of the error.

Fail gracefully: Like in the example code above, instead of crashing the entire application, you can provide users with a friendly error message or take alternative actions when an exception is raised.

Log errors: Combined with Python's logging module, exceptions can be logged for further analysis.

### When to use try and catch debugging

While try and except blocks don't "debug" in the traditional sense of stepping through code or setting breakpoints, they provide a framework to handle, understand, and ultimately resolve errors in a controlled and informed manner.

That said, while "try and catch" is a widely accepted best practice for handling exceptions, it's essential to use it judiciously. Overusing it can lead to "swallowing" exceptions, where errors are caught but not adequately handled or logged, leading to silent failures.

Proper exception handling involves not just catching exceptions but also taking appropriate action, whether that's logging the error, informing the user, or attempting a recovery action.

## Python logging module

The Python logging module is a built-in library designed to provide a flexible framework for creating log messages. Unlike the print() function, which is used for displaying output to the console, the logging module provides a way to configure and capture log messages at different severity levels.

With the logging module, you can categorize error messages based on their severity using levels such as DEBUG, INFO, WARNING, ERROR, and CRITICAL. This categorization helps in filtering and prioritizing issues.

```
import logging

logging.warning('This is a warning message')
logging.error('This is an error message')

logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.error('This is an error with a custom format')

---------------

def user_login(username, password):
    logging.info(f"Attempting to log in user: {username}")
    # ... (some code for authentication)
    if authentication_failed:
        logging.error(f"Login failed for user: {username}")
    else:
        logging.info(f"Successfully logged in user: {username}")
```

### Resources for more information

[Python Docs: Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)

[Python Docs: Logging facility for Python](https://docs.python.org/3/library/logging.html)

## Python debugging with pdb

What is pdb?
Imagine you're developing a Python application designed to analyze vast amounts of textual data to extract sentiment scores. As the application processes data, it occasionally encounters unexpected data formats, causing it to crash. Given the volume of data and the complexity of the application, identifying the root cause of these crashes using simple print() statements is becoming increasingly challenging. This is where Python's built-in interactive debugger, pdb, comes into play.

The acronym pdb stands for "Python DeBugger." It's an interactive debugger for Python programs, allowing you to:

Set breakpoints

Step through code

Inspect variables

Evaluate arbitrary Python expressions interactively

With pdb, you can pause your program at any point, inspect the values of variables, and even change those values if needed.
