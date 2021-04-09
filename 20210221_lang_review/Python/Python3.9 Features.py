"""

Python 3.9 features

@ZL, 20210302

"""

# 1, dict merge, union, inplace union
def dict_merge():
    d1: dict = {a=1, b=2, c=3}
    d2: dict = {c=3, d=4, e=5}
    d3: dict = d1 | d2
    print(d3)
    d1 =| d2
    print(d1)

# 2, string.removeprefix(prefix), string.removesuffix(suffix)
def str_xxxfix():
    s1: str = "hello world.xlsx"
    s2: str = "xxx hello ZL.txt"
    print(s1.removesuffix(".xlsx"))
    print(s2.removeprefix("xxx"))

def main():
    dict_merge()
    str_xxxfix()

if __name__ == '__main__':
    main()