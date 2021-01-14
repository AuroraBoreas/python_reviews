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
>>> # why using class?
... # A
... # E
... # I
... # P
... # simulate things in real life
...
>>> # why?
... # we have a better understanding about things
... # and manipulate them during programming
... # to make ::sense::
...
>>> class B(A):
...     def __gt__(self, other):
...             return (self.number > other.number)
...     def __eq__(self, other):
...             return (self.number == other.number)
...
>>> b1 = B(10)
>>> b2 = B(12)
>>> b1 < b2
True
>>> b1 == b2
False
>>> b1 > b2
False
>>> # it is more like a "generic thing" contains everything in real life
... # life changes, programming must change as well
...
>>> b1 != b2
True
>>> # Abstraction
... # we need a concept to generate a series of thing
... # we must observe the thing and read its characteristics and behaviors
... # the concept covers almost everything we concern about the things
...
>>> # inheritance
... # flexible and extensible
... # variant
... # DRY
...
>>> # Encapsulation
... # i dont want to know the details of the things
... # all i need is to ask the things to be done
...
>>> # Polymorphism
... # obj of this kind of things may have different forms to behave
... # the behaviors are abstracted already
... # we may use the same behaviors to manipulate separate objects
...
>>> # ABS
... # unlike C/C++ and many other languages, python hides ABS from programmers
... # u may use abs library to declare your own ABS class
... # but PEP does not recommend
... # anyways
...
>>> class Animal:
...     def __init__(self, *args):
...             self.name, self.breed, self.age = *args
...     def __repr__(self):
...             return f"{self.name}, {self.breed}, {self.age}"
...     def make_sound(self):
...             print(f"{self.name} makes sound")
...
  File "<stdin>", line 3
SyntaxError: can't use starred expression here
>>> class Animal:
...     def __init__(self, *args):
...             self.name, self.breed, self.age = args
...     def __repr__(self):
...             return f"{self.name}, {self.breed}, {self.age}"
...     def make_sound(self):
...             print(f"{self.name} makes sound")
...
>>> a1 = Animal("SCY", "dog", 3)
>>> a1
SCY, dog, 3
>>> a1.make_sound()
SCY makes sound
>>> class Dog(Animal):
...     def make_sound(self):
...             print("f{self.name} is barking")
...
>>> b1 = Dog("LL", "dog", 4)
>>> b1.make_sound()
f{self.name} is barking
>>> class Cat(Animal):
...     def make_sound(self):
...             print(f"{self.name} is moewing")
...
>>> c1 = Cat("LM", "cat", 5)
>>> c1.make_sound()
LM is moewing
>>> animals = [a1, b1, c1]
>>> for animal in animals:
...     animal.make_sound()
...
SCY makes sound
f{self.name} is barking
LM is moewing
>>> # inheritance
... # there something important to know when using inheritance
... # - constructor or initializer
... # - method resolution order
...
>>> class Bee(Animal):
...     def __init__(self, *args):
...             super(),__init__(args)
...             self.weight = args[-1]
...     def make_sound(self):
...             return f"{self.name} is wenwenwen"
...
>>> d1 = Bee("TXY', "Bee", 5, 11.3)
  File "<stdin>", line 1
    d1 = Bee("TXY', "Bee", 5, 11.3)
                       ^
SyntaxError: invalid syntax
>>> d1 = Bee("TXY", "Bee", 5, 11.3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in __init__
NameError: name '__init__' is not defined
>>> class Bee(Animal):
...     def __init__(self, *args):
...             super().__init__(args)
...             self.weight = args[-1]
...     def make_sound(self):
...             return f"{self.name} is wenwenwen"
...
>>> d1 = Bee("TXY", "Bee", 5, 11.3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in __init__
  File "<stdin>", line 3, in __init__
ValueError: not enough values to unpack (expected 3, got 1)
>>> class Bee(Animal):
...     def __init__(self, *args):
...             super().__init__(args[0], args[1], args[2])
...             self.weight = args[-1]
...     def make_sound(self):
...             return f"{self.name} is wenwenwen"
...
>>> d1 = Bee("TXY", "Bee", 5, 11.3)
>>> d1
TXY, Bee, 5
>>> d1.make_sound()
'TXY is wenwenwen'
>>>


"""
