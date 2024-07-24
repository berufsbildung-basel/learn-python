---
layout: page
parent: Programming Basics
nav_order: 095
title: "Using the HTTP library"
---

# Using the HTTP library

Most programming languages provide _libraries_, additional modules that perform specific tasks, 
while not being part of the core language.

As a "batteries included" language, Python provides
a lot of functionality as part of its
[Python Standard Library](https://docs.python.org/3/library/index.html).

In this exercise we will use the _http.client_ library, as
an example, to retrieve content from websites.

In a file named `using_libs_http.py`, write a function named `get_content` that takes two arguments:

- A String which is the URL to retrieve
- A String that is expected to be included in the retrieved content

The function returns `True` if the retrieved content includes
the specified String, and `False` otherwise.

Errors such as invalid URL or connection error are not handled
by your function, it just passes them on to the caller.

Calling `get_content('apache.org','ASF')`, for example,
returns `True`.

## Test code

To validate your code, download the test code below and run
it as explained on the [Hello, Python](./hello_python.html)
exercise page.

Test code:
[using_libs_http_test.py](./using_libs_http_test.py)

