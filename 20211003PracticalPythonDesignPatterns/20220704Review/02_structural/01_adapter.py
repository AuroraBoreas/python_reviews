"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 

from typing import Any, Callable


class WhatIHave:
    def provided_function_01(self) -> Any:
        pass
    def provided_function_02(self) -> Any:
        pass

class WhatIWant:
    def required_function_01(self) -> Any:
        pass
    def required_function_02(self) -> Any:
        pass

class Adapter:
    def __init__(self, wih:WhatIHave, func:Callable) -> None:
        self._wih = wih
        self.func = func

    def __getattr__(self, attr:str) -> Any:
        return getattr(self._wih, attr)

def client_code() -> None:
    adapter = Adapter(WhatIHave(), WhatIWant().required_function_01)
    getattr(adapter, "provided_function_01")