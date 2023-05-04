# 

from typing import Dict, List
import json

class Flyweight:
    def __init__(self, s:str) -> None:
        self._shared_state = s

    def operate(self, unique_state:str) -> str:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        return f'{self.__class__} : shared -> ({s}), unique -> ({u})'

class FlyweightFactory:
    _flyweights:Dict[str, Flyweight] = dict()

    def __init__(self, init_flyweights:List) -> None:
        for state in init_flyweights:
            self._flyweights[self.get_state(state)] = Flyweight(state)

    def get_state(self, shared_state:List) -> str:
        return '_'.join(sorted(shared_state))

    def get_flyweight(self, shared_state:List) -> Flyweight:
        key = self.get_state(shared_state)
        if not key in self._flyweights:
            print(f'{self.__class__} : {shared_state} not found, creating a new one..')
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print(f'{self.__class__} : reusing the existing one...')
        return self._flyweights[key]

    def list_flyweight(self) -> str:
        return f'flyweight list: {"\n".join(map(str, self._flyweights.keys()))}'