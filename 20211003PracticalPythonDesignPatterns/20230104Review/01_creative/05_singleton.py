"#" 
from dataclasses import dataclass
from typing import Self, Any
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

class Singleton:
    @dataclass
    class __Singleton:
        def __init__(self) -> None:
            self._val: int = None

        def __str__(self) -> str:
            return f"{self.__class__} : {self._val}"

    __obj: __Singleton = None

    def __new__(cls: type[Self]) -> Self:
        if not Singleton.__obj:
            Singleton.__obj = Singleton.__Singleton()
        return Singleton.__obj

    def __getattr__(self, attr: str) -> Any:
        return getattr(self.__obj, attr)

def main() -> None:
    s1: Singleton = Singleton()
    s1._val = 1
    s2: Singleton = Singleton()
    s2._val = 2
    logging.info(s1)

if __name__ == '__main__':
    main()
