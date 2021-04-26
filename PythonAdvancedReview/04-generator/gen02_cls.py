"# python is a protocol orientated lang;\n # every top-level function has a corresponding dunder method implemented;" 

"""

[ lazy evaluation ]
===
* what?
A: instead of running till end of computation,
code has been divided into sub-blocks;

compiler returns evaluation result of each sub-block,
also return control to main,

it means this process is sequencing;

* why?
A: it keeps user not to wait till end of computation;

* how?
A: using __iter__, __next__


* note:

print(i, end=' ') may hinder the intension of this lazy evaluation;
why?
because of io.buffer mechanism when using paramter end=' ';


===

"""

import time

class Compute:
    def __iter__(self):
        self.last = 0
        return self
    
    def __next__(self):
        rv = self.last
        self.last += 1
        time.sleep(.5)
        if self.last > 10:
            raise StopIteration()
        return rv


if __name__ == '__main__':
    for i in Compute():
        print(i)