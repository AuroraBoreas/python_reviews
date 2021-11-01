
from typing import Callable


class WhatIHave:
    def __init__(self): pass
    def provided_function_01(self): pass
    def provided_function_02(self): pass

class WhatIWant:
    def __init__(self): pass
    def required_function(self): return NotImplementedError()

class AdapterDemo1(WhatIHave, WhatIWant):
    def __init__(self, what_i_have:WhatIHave):
        self.what_i_have = what_i_have

    def provided_function_01(self):
        self.what_i_have.provided_function_01()
    
    def provided_function_02(self):
        self.what_i_have.provided_function_02()

    def required_function(self):
        self.provided_function_01()
        self.provided_function_01()

class AdapterDemo:
    def __init__(self, what_i_have:WhatIHave, required_function:Callable):
        self.what_i_have = what_i_have
        self.required_function = required_function

    def __getattr__(self, attr):
        return getattr(self.what_i_have, attr)

class Client:
    def __init__(self, adapter:AdapterDemo)->None:
        self.adapter = adapter

    def do_something(self):
        self.adapter.provided_function_01()
        self.adapter.provided_function_02()
        self.adapter.required_function()

if __name__ == '__main__':
    c = Client(AdapterDemo(WhatIHave(), print))
    c.do_something()