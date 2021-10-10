# alter what we want to fit what we have
# constraints: one or two system due to nature of if-else statementVoluptate est laborum proident eu in non proident in sunt fugiat commodo ad.

class WhatIHave:
    def provided_function_1(self): pass
    def provided_function_2(self): pass

class WhatIWant:
    def required_function(self): pass

class Client:
    def __init__(self, some_object):
        self.some_object = some_object

    def do_something(self):
        if self.some_object.__class__ == WhatIHave:
            self.some_object.provided_function_1()
            self.some_object.provided_function_2()
        elif self.some_object.__class__ == WhatIWant:
            self.some_object.required_function()
        else:
            print('Class of self.some_object not recognized')
