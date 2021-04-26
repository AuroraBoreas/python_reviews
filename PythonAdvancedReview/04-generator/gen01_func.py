"# python is a protocol orientated lang;\n # every top-level function has a corresponding dunder method implemented;" 

"""

[ eager evaluation ]
===
* what?
A: eager evaluation means: in function definition, 
user is blocked and waiting till all results are ready;

* why?
A: it is the nature of eager evaluation;

* how?
A: regular functions have this attribute;


* note:
in this case, 

__iter__
__next__

===

"""

import time

def func():
    rv = []
    for i in range(10):
        rv.append(i)
        time.sleep(.5)
    return rv


if __name__ == '__main__':
    print(func())