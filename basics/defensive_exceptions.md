---
layout: page
parent: Programming Basics
nav_order: 040
title: Defensive Programming
---

# Defensive Programming: using Exceptions

In the [Calculator exercice](./calculator_function.html) we
didn't handle exceptional cases such as an invalid operator
being passed to the `calc` function, or a division by zero.

We will address this now using some _defensive programming_ 
concepts, where you make your code more robust by handling
unexpected values or states.

In a file called `defensive_exceptions.py`, write a `divide`
function that divides two numbers. If called like `divide(8,4)`
it will return `2`.

However, your `divide` function has some constraints:

- If the second argument is less than zero, it raises a `ValueError` exception.
- If the second argument is zero, it raises a `ZeroDivisionError`. That's a default Python behavior, you don't need to implement anything for that, but the test will check it.
- If both arguments have the same value, it also raises a `ValueError` exception, with a message saying `Arguments cannot be equal`

To implement these constraints, you'll need some `if` statements
along with the
[raise](https://docs.python.org/3/tutorial/errors.html#raising-exceptions) statement
and
[built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).

## Mentoring topics

Discuss the benefits of using Exceptions as opposed to returning
"result codes" to indicate problems.

## Test code

To validate your code, download the test code below and run
it as explained on the [Hello, Python](./hello_python.html)
exercice page.

Test code:
[defensive_exceptions_test.py](./defensive_exceptions_test.py)

