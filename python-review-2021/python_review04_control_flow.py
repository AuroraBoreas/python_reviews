"""

D:\DevEnv\WPy32-3741\scripts>python
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> # control flow:
... # if elif else
... # not switch case
... # try ... except ... finally
...
>>> a = 1 if True else False
>>> a
1
>>> b = 2 if (a == 1) else 4
>>> b
2
>>> var = 10
>>> if var < 11:
...     print(var)
... elif var < 11:
...     print(var + 1)
... elif var < 13:
...     print(var + 2)
... else
  File "<stdin>", line 7
    else
       ^
SyntaxError: invalid syntax
>>> if var < 10:
...     print(var)
... elif var >= 10 and var < 20:
...     print(var)
... elif var > 20 and var < 30:
...     print(var)
... else:
...     print(var)
...
10
>>> try:
...     res = var / 0
... except ZeroDivisionError:
...     print("dont do it")
... finally:
...     print("do right things")
...
dont do it
do right things
>>>


"""
