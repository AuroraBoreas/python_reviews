# python is a protocol orientated lang
# every top-level function has a corresponding dunder method

import time

# __iter__()
# __next__()

# to

# yield()

# yield() is not only simplified


def compute():
    for i in range(10):
        yield i
        time.sleep(.5)

class API:
    def do_stuff(self):
        print("step 1")
        yield
        print("step 2")
        yield
        print("step 3")
