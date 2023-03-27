# 

import json
from typing import Any


class Flyweight:
    def __init__(self, shared: str) -> None:
        self._shared = shared

    def operate(self, unique: str) -> None:
        s = json.dumps(self._shared)
        u = json.dumps(unique)
        print(f'{self.__class__}: shared -> ({s}), unique -> ({u})')

class FlyweightFactory:
    _flyweights: dict[str,Flyweight] = list()

    def __init__(self, init_flyweights: list[Any]) -> None:
        for flyweight in init_flyweights:
            self._flyweights[self.get_state(flyweight)] = Flyweight(flyweight)

    def get_state(self, shared: list[Any]) -> str:
        return '_'.join(sorted(shared))

    def get_flyweight(self, shared: list[Any]) -> Flyweight:
        key = self.get_state(shared)
        if key not in self._flyweights:
            print(f'{self.__class__}: {shared} not found and creat a new one...')
            self._flyweights[key] = Flyweight(shared)
        else:
            print(f'{self.__class__}: using the existing one...')
        return self._flyweights[key]
    
    def display_history(self) -> str:
        return 'flyweight list:\n{}'.format('\n'.join(map(str, self._flyweights.keys())))