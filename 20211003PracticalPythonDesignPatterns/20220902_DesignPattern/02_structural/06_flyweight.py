"#" 

import json
from typing import Dict, List

class Flyweight:
    def __init__(self, shared:str) -> None:
        self._shared = shared

    def operate(self, unique:str) -> None:
        s = json.dumps(self._shared)
        u = json.dumps(unique)
        print(f'{self.__class__} : shared -> ({s}), unique -> ({u})')

class FlyweightFactory:
    flyweights:Dict[Flyweight] = {}
    
    def __init__(self, init_flyweights:List) -> None:
        for state in init_flyweights:
            self.flyweights[self.get_state(state)] = Flyweight(state)
    
    def get_state(self, shared:List) -> str:
        return ''.join(sorted(shared))

    def get_flyweight(self, shared:List) -> str:
        key = self.get_state(shared)
        if not key in self.flyweights:
            print(f'{self.__class__} : {key} not found, creating a new one..')
            self.flyweights[key] = Flyweight(shared)
        else:
            print(f'{self.__class__} : reusing the existing one..')
        return self.flyweights[key]

    def show_flyweights(self) -> None:
        return f'flyweights : {"\n".join([str(i) for i in self.flyweights.items()])}'
    