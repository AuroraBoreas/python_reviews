"""
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.

>>> var = 10
>>> type(var)
<class 'int'>
>>> var = 'c'
>>> type(var)
<class 'str'>
>>> var = 3.1415926
>>> type(var)
<class 'float'>
>>> 10 ^ 19
25
>>> # overflow
...
>>> float(10) ^19
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>> float(1)
1.0
>>> float(10)
10.0
>>> 10 ** 19
10000000000000000000
>>> 10 ** 199
10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> # safe?
...
>>> 1 % 2
1
>>> 2 % 2
0
>>> 1 % 31
1
>>> 2 % 31
2
>>> 3 % 31
3
>>> 10000 % 31
18
>>> 100 % 31
7
>>> 10 % 31
10
>>> 31 % 31
0
>>> 31 % 31
0
>>> 32 % 31
1
>>> # func: first-class resident
...
>>> def add(a, b): return (a + b)
...
>>> add(3, 4)
7
>>> add("hello", " world!")
'hello world!'
>>> add(2.718, 3.141)
5.859
>>> def sub():
...     return -1
...
>>> sub
<function sub at 0x03203A50>
>>> sub()
-1
>>> add(sub(), 11)
10
>>> # overload is not allowed
...
>>> def add(); return 1
  File "<stdin>", line 1
    def add(); return 1
             ^
SyntaxError: invalid syntax
>>> def add(): return 1
...
>>> add()
1
>>> add(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() takes 0 positional arguments but 2 were given
>>> add
<function add at 0x03218FA8>
>>> def add(x, y): return x + y
...
>>> add
<function add at 0x02F80978>
>>> # create functions inside of a function? supported
...
>>> def hello(name: str):
...     def func1(x, y):
...             return (x + y)
...     def func2(x, y, z):
...             return (x * y * z)
...     return f"hello {name}, func1 res: {func1(1, 2)}, func2 res: {func2(2, 3, 4)}"
...
>>> hello("ZL")
'hello ZL, func1 res: 3, func2 res: 24'
>>> hello("Monkey")
'hello Monkey, func1 res: 3, func2 res: 24'
>>> # but u can't access func1, func2 outside of hello()
...
>>> func1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'func1' is not defined
>>> func2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'func2' is not defined
>>> # environment comes in. everything lives in an environment, even though the thing itself does not be aware of this fact.
... # enivronment affects the thing every now and on
... # the thing interacts with environment for sure
... # environment has its space. i say namespace
... # namespace is hidden in python
... # under the hood, namespace has four categories:
...     # Local
...     # Global
...     # Enclosure
...     # Builtin
... # B penetrates every namespace
... # Globals are in certain files
... # Locals are limited in a class or function
... # enclosure are binded with blocks
...
>>> # let's talk about args
... # by default, functions take V (deep copy mode)
... # also, in python, functions take Ref of containers to handle thigns
... # pointer concepts and resource management are hidden from python programmers
... # pros: no need to worry about memory leak
... # cons: no ability to control memory by programmers themselve
...
>>> def factorial(n):
...     return 1 if n < 2 else n * factorial(n-1) # recursion :)
...
>>> factorial(3)
6
>>> factorial(5)
120
>>> # so far so good
... # factorial takes n as V
... # this operation is deep copy
...
>>> def display_elements(seq: list): for i in seq: print(i, sep=" ")
  File "<stdin>", line 1
    def display_elements(seq: list): for i in seq: print(i, sep=" ")
                                       ^
SyntaxError: invalid syntax
>>> def display_elements(seq: list):
...     for i in seq:
...             print(i, seq=" ")
...
>>> la = list("bonjour tout le monde!")
>>> display_elements(la)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in display_elements
TypeError: 'seq' is an invalid keyword argument for print()
>>> def display_elements(seq: list):
...     for i in seq:
...             print(i, sep=" ")
...
>>> display_elements(la)
b
o
n
j
o
u
r

t
o
u
t

l
e

m
o
n
d
e
!
>>> la
['b', 'o', 'n', 'j', 'o', 'u', 'r', ' ', 't', 'o', 'u', 't', ' ', 'l', 'e', ' ', 'm', 'o', 'n', 'd', 'e', '!']
>>> def change_elements(seq: list):
...     for i in seq:
...             seq[0] = i * 2
...
>>> la
['b', 'o', 'n', 'j', 'o', 'u', 'r', ' ', 't', 'o', 'u', 't', ' ', 'l', 'e', ' ', 'm', 'o', 'n', 'd', 'e', '!']
>>> change_elements(la)
>>> la
['!!', 'o', 'n', 'j', 'o', 'u', 'r', ' ', 't', 'o', 'u', 't', ' ', 'l', 'e', ' ', 'm', 'o', 'n', 'd', 'e', '!']
>>> # change_element function take arg as Ref
... # if the arg is not not changed in bitwise in memory
... # but we change elements inside the args
... # then global args are changede too
...
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'datetime': <module 'datetime' from 'D:\\DevEnv\\WPy32-3741\\python-3.7.4\\lib\\datetime.py'>, 'time': <module 'time' (built-in)>, 'var': 3.1415926, 'add': <function add at 0x02F80978>, 'sub': <function sub at 0x03203A50>, 'hello': <function hello at 0x03218FA8>, 'factorial': <function factorial at 0x010E02B8>, 'display_elements': <function display_elements at 0x03295780>, 'la': ['!!', 'o', 'n', 'j', 'o', 'u', 'r', ' ', 't', 'o', 'u', 't', ' ', 'l', 'e', ' ', 'm', 'o', 'n', 'd', 'e', '!'], 'change_elements': <function change_elements at 0x03295738>}
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'datetime': <module 'datetime' from 'D:\\DevEnv\\WPy32-3741\\python-3.7.4\\lib\\datetime.py'>, 'time': <module 'time' (built-in)>, 'var': 3.1415926, 'add': <function add at 0x02F80978>, 'sub': <function sub at 0x03203A50>, 'hello': <function hello at 0x03218FA8>, 'factorial': <function factorial at 0x010E02B8>, 'display_elements': <function display_elements at 0x03295780>, 'la': ['!!', 'o', 'n', 'j', 'o', 'u', 'r', ' ', 't', 'o', 'u', 't', ' ', 'l', 'e', ' ', 'm', 'o', 'n', 'd', 'e', '!'], 'change_elements': <function change_elements at 0x03295738>}
>>> builtin
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'builtin' is not defined
>>> builtin()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'builtin' is not defined
>>> builtins()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'builtins' is not defined
>>> # reflection mechanism: python can reflect itself and recognize things inside of it
... # refer to meta-programming for details
...
>>> # as a python programmer, u must be cautious when passing containers to functions
... # or using containers as args, something may happen out of your expectations
...
>>> def sum(seq: list):
...     ttl = 0
...     for i in seq:
...             ttl += i
...     return ttl
...
>>> def sum2(seq=[]):
...     for i in seq:
...             seq[0] = i + 2
...
>>>
>>> sum2([1,2,3])
>>> lb = [1,2,3]
>>> sum2(lb)
>>> lb
[5, 2, 3]
>>> def sum3(seq=[]):
...     seq.extend([1, 2])
...
>>> lb
[5, 2, 3]
>>> sum3(lb)
>>> lb
[5, 2, 3, 1, 2]
>>> sum3(lb)
>>> lb
[5, 2, 3, 1, 2, 1, 2]
>>> # yes, fabulously strange
... # it may not work as you expect
...
>>> # paramarray in python
... # using *args to capture position args
... # using **kwargs to capture default args
...
>>> def do_sth(*args, **kwargs):
...     for i in args:
...             print(i)
...     for k, v in kwargs:
...             print(k, v, end="")
...
>>> do_sth(lb, hello="world!")
[5, 2, 3, 1, 2, 1, 2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in do_sth
ValueError: too many values to unpack (expected 2)
>>> do_sth(lb, {1: 'a', 2: 'b'})
[5, 2, 3, 1, 2, 1, 2]
{1: 'a', 2: 'b'}
>>> do_sth(*lb, **{1: 'a', 2: 'b'})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: do_sth() keywords must be strings
>>> do_sth(*lb, {1: 'a', 2: 'b'})
5
2
3
1
2
1
2
{1: 'a', 2: 'b'}
>>> la
['!!', 'o', 'n', 'j', 'o', 'u', 'r', ' ', 't', 'o', 'u', 't', ' ', 'l', 'e', ' ', 'm', 'o', 'n', 'd', 'e', '!']
>>> da = dict(zip(list("hello world"), range(10))
... )
>>> da
{'h': 0, 'e': 1, 'l': 9, 'o': 7, ' ': 5, 'w': 6, 'r': 8}
>>> do_sth(*la, **da)
!!
o
n
j
o
u
r

t
o
u
t

l
e

m
o
n
d
e
!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in do_sth
ValueError: not enough values to unpack (expected 2, got 1)
>>> do_sth(*la, da)
!!
o
n
j
o
u
r

t
o
u
t

l
e

m
o
n
d
e
!
{'h': 0, 'e': 1, 'l': 9, 'o': 7, ' ': 5, 'w': 6, 'r': 8}
>>> do_sth(*la, hello=1, world=2)
!!
o
n
j
o
u
r

t
o
u
t

l
e

m
o
n
d
e
!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in do_sth
ValueError: too many values to unpack (expected 2)
>>> do_sth(1, 2, 3, hello="world", bonjour="tout le monde!")
1
2
3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in do_sth
ValueError: too many values to unpack (expected 2)
>>> for k, v in da:
...     print(k, v, end=" ")
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 2, got 1)
>>>     print(k, v, end=" ")
"""
