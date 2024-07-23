---
layout: page
parent: Programming Basics
nav_order: 010
title: What's your name?
---

# What's your name?

In this exercise we use a variable to call the function
that you write, and concatenate strings.

In a file called `whats_your_name.py`, write a function
called `wyn` that returns `Hello, <x>!`, where `<x>` is
a name passed to the function via a _function argument_.

The skeleton or your code is similar to the one of the
[Hello, Python](./hello_python.html) exercise, but the function
takes an argument called `name`, as follows:

    def wyn(name):
      # function code

In the function, compute and return the value
specified above, using that `name` argument, which
becomes a local variable inside the function.

## Test code

To validate your code, download the test code below and run
it as explained on the [Hello, Python](./hello_python.html)
exercice page.

Test code:
[whats_your_name_test.py](./whats_your_name_test.py)