
class SingletonObject:
    class __SingletonObject:
        def __init__(self):
            self.val = None

        def __str__(self):
            return '{0!r} {1}'.format(self, self.val)

    instance = None

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()
        return SingletonObject.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

if __name__ == '__main__':
    s1 = SingletonObject()
    s1.val = 'obj val 1'
    print(s1)
    print('------')
    s2 = SingletonObject()
    s2.val = 'obj val 2'
    print(s1)
    print(s2)
