"""
# python is a protocol orientated lang
# every top-level function has a corresponding dunder method implemented

[ data model method ]
===
* what?
A: dunder methods are very similar to operator overloading in C/C++ or C# etc;
But Python pushed it further;

Python makes it almost universal over its ecosystem;
You may see it everywhere and everyday;

* why to use?
A: it is a builtin feature and "protocol";
by using it beforehand, you must have a comprehensive understanding on it;
it demands a profound knowladge to get the gist of it in essence;

* how to use?
A: it is pretty easy to use.
Just like a normal function, except "func name" in between dunder symbols;

===


@ZL, 20210426

"""

class Polynomial:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return "Polynomial{!r}".format(self.args)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.args, other.args)))

    def __call__(self):
        pass

if __name__ == '__main__':
    p1 = Polynomial(1, 2, 3)
    p2 = Polynomial(2, 3, 4)
    print(p1)
    print(p2)
    print(p1 + p2)