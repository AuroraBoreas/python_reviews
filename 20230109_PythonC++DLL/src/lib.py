import ctypes

lib = ctypes.cdll.LoadLibrary('./bin/Release/Test.dll')

def Add(a: int, b: int) -> int:
    """Return the sum of two integers

    Example
    -------
    >>> Add(1, 2)
    >>> 3

    """
    lib.Add.argtypes = [ctypes.c_int, ctypes.c_int]
    lib.Add.restype  = ctypes.c_int
    return lib.Add(a, b)

def sinh_impl(n: float) -> float:
    """Return sinh of n

    Example
    -------
    >>> sinh_impl(1.1)
    >>> 830402176

    """
    return lib.sinh_impl(ctypes.c_double(n))

def Sum(arr: list[int]) -> int:
    """Return the sum of a list with element of integers

    Example
    -------
    >>> Sum([1, 2, 3])
    >>> 6
    >>> Sum(range(10))
    >>> 45

    """
    if not arr:
        raise ValueError('arr must not be None')

    if not isinstance(arr[0], int):
        raise ValueError('arr must be a list of integers')

    size: int = len(arr)
    IntArray = ctypes.c_int * size # max size is 32 though otherwise stackoverflow occurs
    numbers = IntArray(*arr)
    return lib.Sum(numbers, size)

def Fib(n: int) -> int:
    """Return Fibonacci number of a given integer

    Example
    -------
    >>> Fib(5)
    >>> 8

    """
    lib.Fib.argtypes = [ctypes.c_long]
    lib.Fib.restype = ctypes.c_long
    return lib.Fib(n)

def Factorial(n: int, tail: int = 1) -> int:
    """Return factorial of a given integer, using tail recursion

    Examples
    --------
    >>> Factorial(3)
    >>> 6
    
    """
    lib.Factorial.argtypes = [ctypes.c_long, ctypes.c_long]
    lib.Factorial.restype = ctypes.c_long
    return lib.Factorial(n, tail)

class Foo:
    """Create an object of Foo

    Example
    -------
    >>> f: Foo = Foo(5)
    >>> f.add(5)
    >>> 10

    """
    def __init__(self, n: int) -> None:
        lib.Foo_new.argtypes = [ctypes.c_int]
        lib.Foo_new.restype = ctypes.c_void_p

        lib.Foo_bar.argtypes = [ctypes.c_void_p]
        lib.Foo_bar.restype = ctypes.c_void_p

        lib.Foo_add.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.Foo_add.restype = ctypes.c_int

        lib.Foo_del.argtypes = [ctypes.c_void_p]
        lib.Foo_del.restype = ctypes.c_void_p

        self.obj = lib.Foo_new(n)

    def bar(self) -> None:
        lib.Foo_bar(self.obj)

    def add(self, val: int) -> int:
        return lib.Foo_add(self.obj, val)

    def __del__(self) -> None:
        lib.Foo_del(self.obj)