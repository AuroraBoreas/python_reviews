
from typing import Callable

class WhatIHave:
    def provided_func_01(self): pass
    def provided_func_02(self): pass

class WhatIWant:
    def required_func(self): pass

class Adapter:
    def __init__(self, what_i_have:WhatIHave, required_func:Callable):
        self.what_i_have = what_i_have
        self.required_func = required_func

    def __getattr__(self, attr:str):
        return getattr(self.what_i_have, attr)

if __name__ == '__main__':
    wih = WhatIHave()
    wiw = WhatIWant().required_func

    a = Adapter(wih, wiw)
    a.provided_func_01()
    a.provided_func_02()
    a.required_func()