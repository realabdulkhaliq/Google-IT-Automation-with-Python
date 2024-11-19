# Module 3 Regular Expressions

In this module, you’ll learn about what a regular expression is and why you would use one. We’ll dive into the basics of regular expressions and give examples of wildcards, repetition qualifiers, escapare characters, and more. Next up, we’ll explore advanced regular expressions and deep dive on repetition qualifiers. You’ll tackle new exercises like capturing groups and extracting PIDs using regexes. Finally, we’ll provide a study guide to serve as your go-to guide for regular expressions.
**Learning Objectives**
Define what a regular expression is and describe why it is useful
Use basic regular expressions including simple matching, wildcard, and character classes
Explain repetition qualifiers
Use advanced regular expressions

## Regular expressions

A regular expression—sometimes called regex—is a string of characters that specifies a pattern to match against some text. In addition to matching patterns, they can search to extract specific parts of text, validate input data, and are supported by code editors and integrated development environments (IDEs). In this reading, you will look at some examples of common regexes used in coding.

### Regex examples

r”\d{3}-\d{3}-\d{4}” This line of code matches U.S. phone numbers in the format 111-222-3333.

r”^-?\d\*(\.\d+)?$” This line of code matches any positive or negative number, with or without decimal places.

r”^(.+)\/([^\/]+)\/” This line of code matches any path and filename.

Helpful tool
Sometimes regexes can be complex and difficult to read and understand—even for experienced programmers! There are tools available to help break down the regex and explain what each part of the expression does. A common tool that you can use to help with understanding each stage of a regular expression is:

https://regex101.com/

Key takeaways
Regular expressions offer powerful capabilities to programmers but, at times, can be complex and difficult to understand. The more you code with regular expressions, the more comfortable you will be using and understanding them. For more information on regex, check out the following links:

https://docs.python.org/3/howto/regex.html

https://docs.python.org/3/library/re.html

https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy

## Advanced regular expressions

Advanced regular expressions—commonly referred to as advanced regexes—are used by developers to execute complicated pattern matching against strings. In this reading, you will learn about some of the common examples of advanced regular expressions.

Alterations
An alteration matches any one of the alternatives separated by the pipe | symbol. Let’s look at an example:

r"location.\*(London|Berlin|Madrid)"

This line of code will match the text string location is London, location is Berlin, or location is Madrid.

Matching only at the beginning or end
If you use the circumflex symbol (also known as a caret symbol) ^ as the first character of your regex, it will match only if the pattern occurs at the start of the string. Alternatively, if you use the dollar sign symbol $ at the end of a regex, it will match only if the pattern occurs at the end. Let’s look at an example:

r”^My name is (\w+)”

This line of code will match My name is Asha but not Hello. My name is Asha.

Character ranges
Character ranges can be used to match a single character against a set of possibilities. Let’s look at a couple of examples:

r”[A-Z] This will match a single uppercase letter.

r”[0-9$-,.] This will match any of the digits zero through nine, or the dollar sign, hyphen, comma, or period.

The two examples above are often combined with the repetition qualifiers. Let’s look at one more example:

r”([0-9]{3}-[0-9]{3}-[0-9]{4})”

This line of code will match a U.S. phone number such as 888-123-7612.

Backreferences
A backreference is used when using re.sub() to substitute the value of a capture group into the output. Let’s look at an example:

> > > re.sub(r”([A-Z])\.\s+(\w+)”, r”Ms. \2”, “A. Weber and B. Bellmas have joined the team.”)

This line of code will produce Ms. Weber and Ms. Bellmas have joined the team.

Lookahead
A lookahead matches a pattern only if it’s followed by another pattern. Let’s look at an example:

If the regex was r”(Test\d)-(?=Passed)” and the string was “Test1-Passed, Test2-Passed, Test3-Failed, Test4-Passed, Test5-Failed” the output would be:

Test1, Test2, Test4

Key takeaways
The types of advanced regular expressions explained in this reading are just some of the more commonly used ones by developers. They are beneficial in pattern matching, text manipulation, and data validation. For more information, check out the following link:

https://regexcrossword.com/
