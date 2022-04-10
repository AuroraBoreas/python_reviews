"#" 

import json
from typing import Dict, List

class Flyweight:
    def __init__(self, shared:str) -> None:
        self._shared = shared

    def operation(self, unique:str)->None:
        s = json.dumps(self._shared)
        u = json.dumps(unique)
        print(f'{self!r}: shared => ({s}), unique => ({u});')

class FlyweightFactory:
    _flyweights:Dict[Flyweight] = {}

    def __init__(self, init_flyweights:List[str]) -> None:
        for flyweight in init_flyweights:
            self._flyweights[self.get_shared(flyweight)] = Flyweight(flyweight)

    def get_shared(self, shared:List[str])->str:
        return '_'.join(sorted(shared))

    def get_flyweight(self, shared:List[str])->Flyweight:
        key = self.get_shared(shared)
        if not self._flyweights.get(key):
            print(f'{self!r} : {shared} not found; creating a new one..')
            self._flyweights[key] = Flyweight(shared)
        else:
            print(f'{self!r} : resuing the existing one..')
        return self._flyweights[key]

    def list_flyweights(self)->str:
        return f'{self!r} : {"\n".join(map(str, self._flyweights.keys()))}'