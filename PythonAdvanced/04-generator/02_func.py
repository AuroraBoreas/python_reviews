# python is a protocol orientated lang
# every top-level function has a corresponding dunder method

import time

# diff: func vs cls
def add(a, b):
    return a + b

# demo: eagerly evaluation
# behavior: user has no other choices rather than waiting until all return values are ready
# its blocking process;
def load_data():
    rv = []
    for i in range(10):
        rv.append(i)
        time.sleep(.5)
    return rv

if __name__ == '__main__':
    # print(add(3, 4))
    pass
