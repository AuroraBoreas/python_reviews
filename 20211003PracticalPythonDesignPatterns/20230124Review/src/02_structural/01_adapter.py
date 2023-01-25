from typing import Any, Callable


class WhatIHave:
    def existed_func01(self) -> None:
        pass
    def existed_func02(self) -> None:
        pass

class WhatIWant:
    def required_func01(self) -> None:
        pass
    def required_func02(self) -> None:
        pass

class Adapter:
    def __init__(self, wih: WhatIHave, func: Callable) -> None:
        self._wih = wih
        self.func = func

    def __getattr__(self, attr: str) -> Any:
        return getattr(self._wih, attr)

def main() -> None:
    a1: Adapter = Adapter(WhatIHave(), WhatIWant().required_func01)
    a1.existed_func01()
    a1.existed_func02()
    a1.func()

if __name__ == '__main__':
    main()
