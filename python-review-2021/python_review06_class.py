"""

D:\DevEnv\WPy32-3741\scripts>python
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> class A:
...     def __init__(self, number: int):
...             self.number = number
...     def __repr__(self):
...             return f"number: {self.number}"
...     def __add__(self, other):
...             return (self.number + other.number)
...     def __sub__(self, other):
...             return (self.number - other.number)
...     def __mul__(self, other):
...             return (self.number * other.number)
...
>>> a = A(1)
>>> b = A(2)
>>> a + b
3
>>> a * b
2
>>> a + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in __add__
AttributeError: 'int' object has no attribute 'number'
>>> # implicit type conversion failed
... # thus, we do it explicitly
...
>>> a + A(1)
2
>>> print(a)
number: 1
>>> a
number: 1
>>>


"""
