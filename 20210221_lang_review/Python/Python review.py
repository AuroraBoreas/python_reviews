"""

this module is to review meta-language of python

@ZL, 20210221

[meta-element]
----

* variable
    - data types
    - type traits
    - type conversion

* functions
    - function definition (return_type, args, params, val or ref as args)
    - function inside function
    - [x] overload

    - lambda-expr

    - generator

    - iterator(relate to iterable)

    - decorator

    - built-in functions

* statement, expression
    - operators
    - reserved keywords

* control flow
    - if...elif...else
    - try...except...finally

* loop
    - for loop
    - list expression
    - while loop

* class
    - A E I P
    - S O L I D
    - MRO

* containers
    - list
    - tuple
    - dictionary
    - set
    - frozenset

* io
    - file io

----

"""

# variable
def variable_demo():
    # declare and initialize
    print("\n--- declare and initialie ---")
    x = 42
    y = 11
    z = 3.14
    s = "hello world!"
    print(x, y, z, s, end=" ")
    
    print("\n--- data types ---")
    print("data types in python: int, float, string")
    
    print("\n--- type traits ---")
    print("x: {0}, type: {1}".format(x, type(x)))
    print("z: {0}, type: {1}".format(z, type(z)))
    print("s: {0}, type: {1}".format(s, type(s)))
    print("y: {0}, is None: {1}".format(y, y is None))
    # print("y: {0}, is subclass: {1}".format(y, issubclass(y, int)))
    print("y: {0}, is instance: {1}".format(y, isinstance(y, float)))

    print("\n--- type conversion ---")
    print(f"x: {x}, type: {type(x)}, to string: {str(x)}")
    print(f"y: {y}, type: {type(y)}, to string: {str(y)}")
    print(f"{'3.41'}, type: {type('3.14')}, to float: {str('3.14')}")

    return

def function_demo():
    print("\n--- function definition ---")
    def add(x: int, y: int) -> int: return x + y;
    def sub(x: int, y: int) -> int: return x - y;
    def fibonacci(n: int) -> int: return 1 if (n<2) else fibonacci(n-1) + fibonacci(n-2);
    def factorial(n: int) -> int: return 1 if (n<2) else n * factorial(n-1);
    # callable
    print("add(1, 2) = ", add(1, 2)) # 3
    print("sub(4, 5) = ", sub(4, 5)) # -1
    print("fibonacci(3) = ", fibonacci(3)) # 3
    print("factorial(5) = ", factorial(5)) # 120

    print("\n--- function inside function ---")
    print("dynamic langs(Python, JS) have this feature")

    print("\n--- params ---")
    def func1(*args) -> None:
        for arg in args:
            print(arg, end=" ")
        return

    def func2(**kwargs) -> None:
        for k, v in kwargs.items():
            print(k, v)
        return

    func1(1, 2, 3, 4)
    func2(name="ZL", age=35, sex="male")

    print("\n--- lambda expr ---")
    f = lambda x, y: x * y;
    print("lambda function f(3, 4) = ", f(3, 4)) # 12
    print("lambda expr(immediate) = ", (lambda x, y: x / y)(10, 2)) # 5.0
    
    print("\n--- generator ---")
    def gen(n: int) -> int:
        while True:
            n += 1;
            yield n;
    g = gen(10)
    print("next(g) = ", next(g))
    print("next(g) = ", next(g))
    print("next(g) = ", next(g))

    print("\n--- generator expr ---")
    gen_expr = (pow(i, 3) for i in [2, 3, 4])
    print("next(gen_expr) = ", next(gen_expr))
    print("next(gen_expr) = ", next(gen_expr))
    print("next(gen_expr) = ", next(gen_expr))

    print("\n--- iterator ---")
    h = iter("hello world")
    print("iterator demo: ", next(h))
    print("iterator demo: ", next(h))
    print("iterator demo: ", next(h))

    print("\n--- decorator ---")
    def dec(func: callable) -> callable:
        def inner(*args, **kwargs):
            print("at inner function block")
            return func(*args, **kwargs)
        return inner
    
    @dec
    def greet(name: str) -> None:
        print("hello " + name)
    
    greet("ZL")

    print("\n--- built-in functions ---")
    builtin_funcs = [
        abs,
        all,
        any,
        ascii,

        bin,
        breakpoint,

        delattr,
        
        callable,
        chr,
        compile,
        
        eval,
        exec,
        
        format,
        
        globals,
        getattr,
        
        hex,
        hash,
        hasattr,

        input,
        issubclass,
        isinstance,

        iter,
        id,
        
        locals,

        map,
        min,
        max,
        
        next,
        
        ord,
        oct,
        open,
        
        pow,
        print,

        range,
        repr,
        round,
        
        setattr,
        sorted,
        sum,
        
        vars,        
    ]
    for i, f in enumerate(builtin_funcs):
        print(i, f.__name__)
    

    return

def statement_demo():
    print("\n--- arithmetics ---")
    x = 42; y = 11
    print("x = {}, y = {}, x + y = {}".format(x, y, x + y))
    print("x = {}, y = {}, x - y = {}".format(x, y, x - y))
    print("x = {}, y = {}, x * y = {}".format(x, y, x * y))
    print("x = {}, y = {}, x / y = {}".format(x, y, x / y))
    print("x = {}, y = {}, x // y = {}".format(x, y, x // y))
    print("x = {}, y = {}, x % y = {}".format(x, y, x % y))

    print("\n--- relational ---")
    print("x = {}, y = {}, x == y: {}".format(x, y, x == y))
    print("x = {}, y = {}, x != y: {}".format(x, y, x != y))
    print("x = {}, y = {}, x > y: {}".format(x, y, x > y))
    print("x = {}, y = {}, x >= y: {}".format(x, y, x>= y))
    print("x = {}, y = {}, x < y: {}".format(x, y, x < y))
    print("x = {}, y = {}, x <= y: {}".format(x, y, x<= y))

    print("\n--- logic ---")
    print("x = {}, y = {}, not y: {}".format(x, y, not y))
    print("x = {}, y = {}, x and y: {}".format(x, y, x and y))
    print("x = {}, y = {}, x or y: {}".format(x, y, x or y))
    
    print("\n--- access ---")
    print("int class: {}, {}, {}".format(int.numerator, int.denominator, int.mro))

    print("\n--- bitwise ---")
    print("x = {0}, x in binary: {1:b}".format(x, x))
    print("y = {0}, y in binary: {1:b}".format(y, y))
    x <<= 2;
    print("x << 2, x = {}".format(x))
    x = 42; x >>= 2
    print("x >> 2, x = {}".format(x))
    x = 42; x = ~x
    print("~x, x = {}".format(x))
    x = 42;
    print("x = {0:b}, y = {1:b}, x & y = {2:b}".format(x, y, x & y))
    print("x = {0:b}, y = {1:b}, x | y = {2:b}".format(x, y, x | y))
    print("x = {0:b}, y = {1:b}, x ^ y = {2:b}".format(x, y, x ^ y))
    
    
    print("\n--- assignment ---")
    a = 42;
    a = int(a);
    print("a = 42, ", a)
    print("a = int(42), ", a)
    return

def controlflow_demo():
    print("\n--- ifelse ---")
    
    def ifelse_demo(n):
        if n % 3:
            return "foo"
        elif n % 5:
            return "bar"
        elif n % 7:
            return "baz"
        else:
            return
    
    for i in range(10):
        print(ifelse_demo(i), end=" ")

    print("\n--- tryexcept ---")
    def tryexcept_demo(x, y):
        try:
            res = x / y
            print(res)
        except ZeroDivisionError as ex:
            print(ex)
        except TypeError as ex:
            print(ex)
        finally:
            # raise ValueError("argument error")
            print(x, y)

    tryexcept_demo(10, 0)

    return

def loop_demo():
    print("\n--- for loop ---")
    for i in range(10): print(i, end=" ");
    print()
    for _ in range(5): print("hello", end=" ");

    print("\n--- while loop ---")
    i = 0
    while i < 5:
        print(i, end=" ")
        i += 1

    print("\n--- simulate do...while loop ---")
    condi = True
    while condi:
        print("do something")
        print("evaluate condi")
        condi = False
        if not condi:
            print("break")
            break
    
    print("\n--- list expr ---")
    numbers = [1, 2, 3, 4]
    print("before +1 : ", numbers)
    increased_one = [ i + 1 for i in numbers ]
    print("after +1 : ", increased_one)
    return

def class_demo():

    print("\n--- class ---")
    class Point:
        def __init__(self, x: int, y: int):
            self._x = x; self._y = y
        def __repr__(self):
            return f"[{self._x}, {self._y}]"
        def X(self): return self._x;
        def Y(self): return self._y;
        def __add__(self, other):
                return Point(self._x + other._x, self._y + other._y)
        def __sub__(self, other):
                return Point(self._x - other._x, self._y - other._y)
        def __eq__(self, other):
                return self.__repr__() == other.__repr__()
        def __gt__(self, other):
                return self.__repr__() > other.__repr__()
    
    class PointCollection(Point):
        def __init__(self, point_collections=None):
            if point_collections != None:
                self._point_collections = point_collections
            else:
                self._point_collections = []

        def __getitem__(self, index: int):
            return self._point_collections[index]

        def __setitem__(self, index: int, val):
            self._point_collections[index] = val

    p1 = Point(1, 2)
    p2 = Point(3, 4)

    pcols = PointCollection([
        p1,
        p2,
        Point(12, 33),
        Point(8, 10)
    ])

    for pcol in pcols:
        print(pcol, end=" ")
    print()    
    return

def container_demo():
    print("\n--- list ---")
    mylist: list = [2, 3, 4, 5]
    print("process with CRUD(ICAMLOBP): ")
    print("iterator: ")
    for i in mylist: print(i, end=" ")
    print("\ncapacity, len(mylist)", len(mylist))
    print("access, mylist[-1] = ", mylist[-1])
    mylist[0] = 42
    print("modifier, mylist[0] = 42", mylist[0])
    a, b, *_ = mylist
    print("unpack a, b, *_ = mylist, a = {}, b = {}".format(a, b))

    print("\n--- tuple ---")
    mytuple = (2, 3)

    print("\n--- dictionary ---")
    mydict1 = { 1:"a", 2:"b", 3:"c" }
    mydict2 = dict(zip([1, 2, 3], list("abc")))
    assert mydict1 == mydict2, "messed up"

    print("\n--- set ---")
    mysetA = {1, 2, 3}
    mysetB = {3, 4, 5}
    print("union: ", mysetA | mysetB)
    print("intersection: ", mysetA & mysetB)
    print("symmetricDifference: ", mysetA ^ mysetB)
    print("difference: ", mysetA - mysetB)

    print("\n--- frozenset ---")
    fset = frozenset([3, 4, 1, 2])
    print("frozenset: ", fset)
    return

def fileio_demo():
    fp = "./Python/myfile"
    with open(fp, 'w', encoding="utf-8") as f:
        f.writelines("hello\n")
        f.writelines("world\n")
        f.writelines("from\n")
        f.writelines("ZL\n")

    with open(fp, 'r', encoding="utf-8") as f:
        content = f.readlines()
        print("file content: ", content)
    return
        

def main():
    variable_demo()
    function_demo()
    statement_demo()
    controlflow_demo()
    loop_demo()
    class_demo()
    container_demo()
    fileio_demo()

if __name__ == '__main__':
    main()