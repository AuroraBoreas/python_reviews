"""
@ scoping rules
- follows normal name resolution rules(LEGB)
# ! but there are some special cases in static typechecking context

"""

from typing import TypeVar, Generic

# generic function
T = TypeVar('T')
def func1(x: T)->T: ...
def func2(x: T)->T: ...

# generic class, coincide, 
class MyClass(Generic[T]):
    def meth1(self, x: T)->T: ... # return_type T is bound to arg x: T
    def meth2(self, x: T)->T: ... # return_type T is bound to arg x: T

# generic class, not coincide,
U = TypeVar('U')

class Foo(Generic[T]):
    def meth1(self, x: T, y: U)->T: ...

if __name__ == "__main__":
    func1(1)
    func2('TS')

    a = MyClass() # type: MyClass[int] by default
    a.meth1(1)    # OK
    a.meth2('ts') # expressive error

    f = Foo() # type: Foo[int] by default
    y = f.meth1(0, 'abc') # inferred type of y is str