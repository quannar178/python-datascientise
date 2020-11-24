# Numpy library

## Summary

`Numpy` is a python library used for working with arrays.

It provide an array object that is up to 50x faster that traditional Python lists. 

Why Numpy arrays are faster than Python lists:

* An array is a collection of homogeneous data-types that are store in contigous memory location. On the other hand, a list in Python is a collection of heterogeneous data types stored in non-contigous memory location.
  * Fater to read less bytes of memory.
  * No type checking when iterating through objects.
* The Numpy package breaks down a task into multiple fragments and then processes all the fragments parallelly.
* The Numpy package integrates C, C++ and Fortran codes in Python. These programming languages have very litle execution time compared to Python.