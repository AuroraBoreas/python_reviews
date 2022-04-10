"#" 

class Singleton:
    class __Singleton:
        def __init__(self) -> None:
            self._val:int = None

        def __str__(self) -> str:
            return f'{self!r} : {self._val}'

    instance:__Singleton = None

    def __new__(cls: type) -> type:
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance