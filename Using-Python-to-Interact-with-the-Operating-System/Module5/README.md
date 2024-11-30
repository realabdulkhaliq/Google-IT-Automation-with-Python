# Testing in Python

In this module, you’ll learn how to create tests in Python. We’ll cover what testing is all about and dive into the differences between manual versus automated testing. Next, we’ll explore what unit tests are intended to do and how to write them. Then, we’ll learn about other test concepts like black box versus white box tests and how test-driven development can frame how you design and write your code. Finally, you’ll learn about errors and exceptions, and how to combat them.

## unittest

A unittest provides developers with a set of tools to construct and run tests. These tests can be run on individual components or by isolating units of code to ensure their correctness. By running unittests, developers can identify and fix any bugs that appear, creating a more reliable code. In this reading, you will learn about unittest concepts, how to use and when to use them, and view an example along the way.

Concepts
Unittest relies on the following concepts:

Test fixture: This refers to preparing to perform one or more tests. In addition, test fixtures also include any actions involved in testing cleanup. This could involve creating temporary or proxy databases, directories, or starting a server process.

Test case: This is the individual unit of testing that looks for a specific response to a set of inputs. If needed, TestCase is a base class provided by unittest and can be used to create new test cases.

Test suite: This is a collection of test cases, test suites, or a combination of both. It is used to compile tests that should be executed together.

Test runner: This runs the test and provides developers with the outcome’s data. The test runner can use different interfaces, like graphical or textual, to provide the developer with the test results. It can also provide a special value to developers to communicate the test results.

### Comparing unittest and pytest

Both unittest and pytest provide developers with tools to create robust and reliable code through different forms of tests. Both can be used while creating programs within Python, and it is the developer’s preference on which type they want to use.

In this reading, you will learn about the differences between unittest and pytest, and when to use them.

Key differences
Unittest is a tool that is built directly into Python, while pytest must be imported from outside your script. Test discovery acts differently for each test type. Unittest has the functionality to automatically detect test cases within an application, but it must be called from the command line. Pytests are performed automatically using the prefix test\_. Unittests use an object-oriented approach to write tests, while pytests use a functional approach. Pytests use built-in assert statements, making tests easier to read and write. On the other hand, unittests provide special assert methods like assertEqual() or assertTrue().

Backward compatibility exists between unittest and pytest. Because unittest is built directly into Python, these test suites are more easily executed. But that doesn’t mean that pytest cannot be executed. Because of backward compatibility, the unittest framework can be seamlessly executed using the pytest framework without major modifications. This allows developers to adopt pytest gradually and integrate them into their code.
