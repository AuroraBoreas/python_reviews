# python is a protocol orientated lang
# every top-level function has a corresponding dunder method

import time

# diff: func vs lcs
class Add:
    def __call__(self, a, b):
        return a + b

# demo: lazy evaluation
class Loader:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        time.sleep(.5)
        return rv


if __name__ == '__main__':
    # a1 = Add()
    # print(a1(3, 4))
    pass
