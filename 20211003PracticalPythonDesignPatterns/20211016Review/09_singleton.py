
class SingletonDemo:
    class __SingletonObject:
        def __init__(self):
            self.val = None
            
        def __str__(self):
            return '{!r} {}'.format(self, self.val)

    instance:__SingletonObject = None

    def __new__(cls):
        if not SingletonDemo.instance:
            SingletonDemo.instance = SingletonDemo.__SingletonObject()
        return SingletonDemo.instance

    def __setatt__(self, attr):
        setattr(self.instance, attr)

    def __getattr__(self, attr):
        return getattr(self.instance, attr)

if __name__ == '__main__':
    s1 = SingletonDemo()
    s1.val = 'object val 1'

    s2 = SingletonDemo()
    s2.val = 'Object val 2'
    print(s1)
    print(s2)
    print(s1 is s2)