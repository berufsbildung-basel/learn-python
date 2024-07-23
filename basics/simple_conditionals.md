---
layout: page
parent: Programming Basics
nav_order: 030
title: Simple Conditionals
---

# Simple Conditionals: if, elif

In this exercise we use _simple conditionals_,
`if` and `elif` to classify numbers.

In a file called `simple_conditionals.py`, write
a function called `classify` that receives a number as
an argument and works as follows:

- Returns the string 'Negative' if the number is less than zero
- Returns the string 'Small' if the number is between zero and 5 included
- Returns the string 'Zero' if the number is zero
- Returns the string 'Large' if the number is more than 9362
- Returns the string 'Medium' if the number is between 6 and 9362 included

## Mentoring topics

Try to write your code in an elegant and efficient way, and review it
with your programming mentor to get advice on efficiency and style.

You can also discuss how to write extensive automated tests for such
a function, which might involve [Fuzzing](https://en.wikipedia.org/wiki/Fuzzing).

## Test code

To validate your code, download the test code below and run
it as explained on the [Hello, Python](./hello_python.html)
exercice page.

Test code:
[simple_conditionals_test.py](./simple_conditionals_test.py)