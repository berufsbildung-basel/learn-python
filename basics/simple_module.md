---
layout: page
parent: Programming Basics
nav_order: 090
title: A Simple Module
---

# A Simple Module

Modules are used in most programming languages, in one form
or another, to isolate parts of the code and hide the details
to the outside world.

In this exercise you will write a module file named `simple_module.py`
that provides the following functions:

- `set` takes an integer value and stores it in a variable that's private to the module
- `get` returns the last value set, or -1 if not value was set yet
- `count` returns the number of times the `set` function was called
- `clear` resets the module to its initial state

## Hints

You will need to use the `global` keyword in your module to refer to
the variables that store the current value and count.

## Mentoring topics

Discuss the benefits of encapsulation and how clean module interfaces
foster the durability and ease of maintenance of your code.

## Test code

To validate your code, download the test code below and run
it as explained on the [Hello, Python](./hello_python.html)
exercise page.

Test code:
[simple_module_test.py](./simple_module_test.py)

