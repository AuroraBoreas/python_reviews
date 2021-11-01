#~ share is care

from typing import Any

class SingletonDemo:
    class __SingletonObject:
        def __init__(self)->None:
            self.val = None

        def tostring(self)->str:
            return '{0!r} {1}'.format(self, self.val)

    instance:__SingletonObject = None

    def __new__(cls):
        if not SingletonDemo.instance:
            SingletonDemo.instance = SingletonDemo.__SingletonObject()
        return SingletonDemo.instance

    def __getattr__(self, attr):
        return getattr(self.instance, attr)

    def __setattr__(self, attr):
        return setattr(self.instance, attr)

if __name__ == '__main__':
    s1 = SingletonDemo()
    s1.val = 'obj val 1'
    print(s1.tostring())

    print('---------------')

    s2 = SingletonDemo()
    s2.val = 'obj val 2'
    print(s1.tostring())
    print(s2.tostring())
    print(s1 is s2)
    