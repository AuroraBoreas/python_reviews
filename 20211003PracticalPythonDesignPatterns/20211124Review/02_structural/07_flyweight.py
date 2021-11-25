# 

from typing import Dict, List
import json

class Flyweight:
    def __init__(self, shared_state:str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state:str)->None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f'{self.__class__}: shared->({s}); unique->({u})')

class FlyweightFactory:
    _fyweights:Dict[str, Flyweight] = {}

    def __init__(self, init_flyweights:Dict) -> None:
        for state in init_flyweights:
            self._fyweights[self.get_state(state)] = Flyweight(state)

    def get_state(self, shared_state:List)->str:
        return '_'.join(sorted(shared_state))

    def get_flyweight(self, shared_state:List)->Flyweight:
        key = self.get_state(shared_state)
        if not self._fyweights.get(key):
            print(f'{self.__class__}: {shared_state} not found, creating a new one..')
            self._fyweights[key] = Flyweight(shared_state)
        else:
            print(f'{self.__class__}: resuing the existing one')

    def list_flyweigts(self)->str:
        print(f'{self.__class__}: i have the {len(self.get_flyweight)} flyweights:')
        return '\n'.join(map(str, self._fyweights.keys()))
