# 

import json
from typing import Dict, List

class Flyweight:
    def __init__(self, shared_state:str) -> None:
        pass

    def operation(self, unique_state:str)->None:
        pass


class FlyweightFactory:
    _flyweights:Dict[str, Flyweight] = {}

    def __init__(self, init_flyweights:List) -> None:
        for state in init_flyweights:
            self._flyweights[self.get_state(state)] = Flyweight(state)

    def get_state(self, shared_state:List)->str:
        return '_'.join(sorted(shared_state))

    def get_flyweight(self, shared_state:List)->str:
        key = self.get_state(shared_state)
        if not self._flyweights.get(key):
            print(f'{self.__class__}: {shared_state} not found, creating a new one..')
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print(f'{self.__class__}: resuing the existing one..')
        return self._flyweights[key]

    def list_flyweights(self)->None:
        print(f'{self}')
        pass