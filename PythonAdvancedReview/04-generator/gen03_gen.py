"# python is a protocol orientated lang;\n# every top-level function has a corresponding dunder method implemented; " 


"""
[ generator ]
===
* concept:
A: in essence, there is no big difference btw gen02_cls.py and gen03_gen.py;

* effort:
A: it takes little effort to wirte code :^D
it is nicer and more beautiful;

===

"""

import time

def compute():
    for i in range(10):
        yield i
        time.sleep(.5)


if __name__ == '__main__':
    for i in compute():
        print(i)