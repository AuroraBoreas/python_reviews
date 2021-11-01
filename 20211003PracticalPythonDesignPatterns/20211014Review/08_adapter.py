
from typing import Callable


class WhatIHave:
    def __init__(self): pass
    def provided_func_01(self): pass
    def provided_func_02(self): pass

class WhatIWant:
    def __init__(self): pass
    def required_func(self): pass

#~ Inheritancce

class Adapter1(WhatIHave, WhatIWant):
    def __init__(self): pass

    def provided_func_01(self):
        return super().provided_func_01()

    def provided_func_02(self):
        return super().provided_func_02()

    def required_func(self):
        return super().required_func()

#~ Composite
...

#~ Dunder method

class Adapter2:
    def __init__(self, whatihave:WhatIHave, required_func:Callable) -> None:
        self.whatihave = whatihave
        self.required_func = required_func

    def __getattr__(self, attr)->object:
        return getattr(self.whatihave, attr)

if __name__ == '__main__':
    pass