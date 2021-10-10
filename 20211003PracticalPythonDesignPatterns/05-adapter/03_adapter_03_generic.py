
class WhatIHave:
    def func_01(self): pass
    def func_02(self): pass

class WhatIWant:
    def required_function(self): pass

class Adapter:
    def __init__(self, what_i_have:WhatIHave, required_function):
        self.what_i_have = what_i_have
        self.required_function = required_function

    def __getattr__(self, attr):
        return getattr(self.what_i_have, attr)

class Client:
    def __init__(self, adapter:Adapter):
        self.adapter = adapter

    def do_something(self):
        self.adapter.func_01()
        self.adapter.required_function()
