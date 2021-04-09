"""

Python 3.8 features

@ZL, 20210302

"""

# 1, positional-only parameters
def func(a, b, /, *kwargs) -> None:
    print(a + b)
    for k, v in kwargs:
        print(k, v)
    return

def myFunc(a, b, /, c, d, *, e, f) -> None:
    return

# 2, :=
def func3()->str:
    a: int = 69
    if (b:=a) > 10:
        return f"the value of {b} > 10"
    return ""

# 3, F-string, self-express
def func4()->float:
    a: float = 3.141
    b: float = 2.718
    print(f"{a + b =}")
    print(f"{c:= a - b}")
    return c

# 4, reversed() works with dictionary
def reverse_dict(d: dict):
    reversed(d)
    print(d)

def main():
    func(1, 2, x=1.618, y=2.718, z=3.14)
    myFunc(1, 2, 3.14, 2.718, hello="world", name="ZL")
    func3()
    func4()
    d: dict = dict(zip(range(3), list("abc")))
    reversed_dict(d)

if __name__ == '__main__':
    main()