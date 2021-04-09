"""

[delegate]
===

* what
    a function pointer in C++, but safe use in C#;
    note: function pointer is a type in C++;

* why
    a versatile way to generalize functions with a certain type;

* howto
    ```C++
    #include <iostream>
    // generic pattern
    // typedef U (*func_ptr)(T arg);
    typedef void (*func_ptr)(char*);
    
    inline void hello(char* s)
    { std::cout << s << std::endl; }
    
    int main()
    {
        func_ptr fp = hello;
        char s[] = "hello ZL";
        fp(s);

        return 0;
    }

    ```

    ```C#
    using System;
    
    namespace ZL
    {
        class Demo
        {
            static void Main(string[] s)
            {
                delegate void func_name(string s);
                func_name = Hello;
                string s = "hello ZL";
                func_name(s);
            }

            private static void Hello(string s)
            {
                Console.writeline(s);
            } 
        }
    }

    ```
===

# wait, this is no function template feature in Python;
# but Python has decorator. it may implement a similar mechnism :D

# Event, EventHandler;

"""

import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s -- %(threadName)s -- %(message)s")

registry = set()

def register(active=True):
    def dec(func):
        if active:
            registry.add(func)
        else:
            registry.discard(func)
    return dec

"""
Q: why does direct-decorator on a recursive function raise NoneType Error?
A: 
    The original factorial is recursive and therefore the decorated version is recursive too. 
    And so you get the timing data printed for each recursive call - the decorated factorial calls itself, not the original version, 
    
    because the name factorial now refers to the decorated version.

S:
    to work around, here is a solution; (or using functools.wraps)

"""

def fibonacci(n: int)->int:
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)

@register(active=True)
def nr_fibonacci(n: int)->int:
    return fibonacci(n)

def factorial(n: int)->int:
    return 1 if n < 2 else n * factorial(n-1)
    
@register(active=False)
def nr_factorial(n: int)->int:
    return factorial(n)

@register(active=True)
def square(n: int)->int:
    return n * n

@register(active=False)
def hello(n: int):
    print(f"hello {n}")

class Point:
    def __init__(self, x, y):
        self._x = x; self._y = y;

    def __str__(self):
        return f"[{self._x}, {self._y}]"
    
    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)
    
    def increase(self, delta):
        while (self._x + self._y < 10):
            self._x = self._x + delta
            self._y = self._y + delta
            logging.debug("result {}".format([f(self._x + self._y) for f in registry]))

if __name__ == '__main__':
    # assert len(registry) == 2, "you fucked up"
    # print(len(registry))
    # n = 4
    # # [ print(func(n)) for func in registry]
    # for func in registry:
    #     print(func.__name__)
    #     print(func(n))
    
    p1 = Point(3, 4)
    delta = 1
    p1.increase(delta)

