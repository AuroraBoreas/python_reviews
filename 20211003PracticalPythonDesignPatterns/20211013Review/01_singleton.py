
from typing import Any


class SingletonDemo:
    class __SingletonObject:
        def __init__(self):
            self.val = None

        def __str__(self):
            return '{0!r} {1}'.format(self, self.val)

    instance = None

    def __new__(cls):
        if not SingletonDemo.instance:
            return SingletonDemo.__SingletonObject()
        return SingletonDemo.instance

    def __getattr__(self, attr):
        return getattr(self.instance, attr)

    def __setatt__(self, attr):
        return setattr(self.instance, attr)

if __name__ == '__main__':
    s1 = SingletonDemo()
    s1.val = 42
    s2 = SingletonDemo()

    print(s1)
    print(s2)
    print(s1 is s2)