class WhatIHave:
    def func_01(self): pass
    def func_02(self): pass

class WhatIWant:
    def required_func(self): pass

class ISuperClass:
    pass

class Adapter(ISuperClass):
    def __init__(self, what_i_have:WhatIHave):
        self.what_i_have = what_i_have

    def required_func(self):
        return self.what_i_have.func_01()

    def __getattr__(self, attr):
        return getattr(self.what_i_have, attr)
