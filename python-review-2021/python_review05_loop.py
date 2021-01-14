"""

D:\DevEnv\WPy32-3741\scripts>python
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> # loop
... # for loop
... # while loop
... # no do ... while ... loop
... # which is not good
...
>>> # but we can mimic it in python
...
>>> condition = True
>>> condition
True
>>> condition == 1
True
>>> while condition:
...     print(condition)
...     condition = True if (1==2) else False
...
True
>>> # so, the pattern of the mimic do...while loop is:
... # condition = true
... # while condition:
... #   # statement
... #   # condition = test_condition()
...
>>>


"""
