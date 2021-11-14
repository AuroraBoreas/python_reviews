# flyweight objects contain intrinsic fields only; extrinsic fields should be passed in via parameters
import json
from typing import Dict

class Flyweight:
    def __init__(self, shared_state:str)->None:
        self._shared_state = shared_state
    
    def operation(self, unique_state:str)->None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f'{self.__class__}: shared->({s}) and unique->({u})')

class FlyweightFactory:
    _flyweights:Dict[str, Flyweight] = {}
    
    def __init__(self, init_flyweights:Dict)->None:
        for state in init_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)
    
    def get_key(self, state:str)->str:
        return '_'.join(sorted(state))

    def __str__(self)->str:
        return (f'{self.__class__}: i have {len(self._flyweights)} flyweights\n') + '{}'.format('\n'.join(map(str, self._flyweights.keys())), end='')

    def get_flyweight(self, shared_state:str)->Flyweight:
        key = self.get_key(shared_state)
        if not self._flyweights.get(key):
            print(f'{self.__class__}: {shared_state} not found, creating a new one..')
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print(f'{self.__class__}: reusing the existing one..')
        return self._flyweights[key]

def client_code()->None:
    ff = FlyweightFactory([
        list('abc'),
        list('abd'),
        list('abe'),
        list('123'),
    ])

    print(ff)

    flyweight = ff.get_flyweight(list('abx'))
    flyweight.operation(list('cy'))

    print(ff)

if __name__ == '__main__':
    client_code()