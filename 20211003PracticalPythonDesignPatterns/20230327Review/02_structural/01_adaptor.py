# 

from typing import Any, Callable

class WhatIHave:
    def existed_function_01(self) -> Any: pass
    def existed_function_02(self) -> Any: pass

class WhatIWant:
    def requested_function_01(self) -> Any: pass
    def requested_function_02(self) -> Any: pass

class Adaptor:
    def __init__(self, wih: WhatIHave, func: Callable) -> None:
        self._wih = wih
        self.func = func

    def __getattr__(self, attr: str) -> None:
        return getattr(self._wih, attr)