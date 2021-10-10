
class WhatIWant:
    def required_function(self): pass

class WhatIHave:
    def func_01(self): pass
    def func_02(self): pass

class Adapter(WhatIHave, WhatIWant):
    def __init__(self, what_i_have):
        self.what_i_have = what_i_have

    def func_01(self):
        self.what_i_have.func_01()

    def func_02(self):
        self.what_i_have.func_02()

    def required_function(self):
        self.func_01()
        self.func_02()

class Client:
    def __init__(self, what_i_want:Adapter):
        self.what_i_want = what_i_want
    def do_something(self):
        self.what_i_want.required_function()
