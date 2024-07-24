---
layout: page
parent: Programming Basics
nav_order: 080
title: Using Sets
---

# Using Sets

Sets are another important data structure, found in many
programming languages and libraries. Here we use a Set
to remove duplicates in a list of Strings.

In a file named `using_sets.py`, write a function named
`dedup` that:

- Takes a variable number of arguments
- Ignores arguments which are not Strings
- Returns a List of the remaining arguments, with no duplicate values, sorted by value

Calling `dedup('one',2,'three',True,'three')` returns `['one','three']`, for example

## Hints

- Using a Set as an intermediate data structure is a good way of removing
duplicate values.
- You will probably need to use the `sorted()` and `isinstance()` functions.

## Test code

To validate your code, download the test code below and run
it as explained on the [Hello, Python](./hello_python.html)
exercise page.

Test code:
[using_sets_test.py](./using_sets_test.py)

