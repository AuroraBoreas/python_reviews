"""

>>> # statement
... # keyowrd: assert, bin, abs, ...
... # expression
... # a = 1, b = 2
... # nameing conflition
... # naming styles
... # pass
...
>>> a = 1
>>> b = 2
>>> c = 3, d = 4
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> c = 3; d = 4
>>> a
1
>>> b
2
>>> c
3
>>> d
4
>>> e, f = 6, 7
>>> e
6
>>> f
7
>>> e, f = f, e
>>> e
7
>>> f
6
>>> # swap
... # Ref

"""
